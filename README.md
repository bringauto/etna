# BringAuto virtual development platform

It's intended to simplify development for [Fleet] and The Autonomy developers.

The system can be used by docker compose stored at the git root of this repository.

There are multiple containers:

- VerneMQ MQTT broker (bringauto/vernemq)
- Virtual Vehicle - Mission module client implementation (it connects to Module Gateway and simulates a Mission module's autonomy device)
- Virtual PLC - IO module client
- Module Gateway - cpp implementation of Module Gateway with Mission, IO and example module support
- External server - server implementation with Mission, IO and example module support
- HTTP API Server - tool for communication with final endpoint, used by mission module
- Integration layer - a bridge between the HTTP API and the Fleet Management API
- Fleet Management API - an API that handles creating orders for cars and displaying their state
- Virtual Fleet Management - application simulating Fleet Management. It creates orders for cars.
- PostgreSQL database - storage of the HTTP API keys and the messages sent via the API
- Mission Module Display Tool - a simple web server to display the positions of vehicles on a map

## Container Repositories

Below are the links to the repositories of the containers. Most of the containers are public on GitHub, but some are private.

- [VerneMQ docker repository](https://github.com/bringauto/vernemq-docker)
- [VerneMQ repository](https://github.com/bringauto/vernemq)
- [Virtual Vehicle repository](https://github.com/bringauto/virtual-vehicle)
- [Virtual PLC repository](https://gitlab.bringauto.com/bring-auto/hardware/firmware/virtual-plc-arduino-opta)
- [Module Gateway repository](https://github.com/bringauto/module-gateway)
- [External Server repository](https://github.com/bringauto/external-server)
- [HTTP API repository](https://github.com/bringauto/fleet-protocol-http-api)
- [Fleet Management API repository](https://github.com/bringauto/fleet-management-http-client-go)
- [Virtual Fleet Management repository](https://github.com/bringauto/virtual-fleet-management)
- [Mission Module Display Tool repository](https://github.com/bringauto/mission-module-display-tool)

## Fleet Protocol

To read more about the system architecture look at Fleet Protocol v2 documentation:

- [Summary]
- [Fleet Protocol Requirements]
- [Internal Client]
- [Module Gateway]
- [External Server]
- [Modules]
- [Message Structure]
- [Internal Client design]
- [Module Gateway design]
- [External Server design]
- [HTTP API]
- [HTTP API Wait Mechanism]

To use Fleet Protocol v1, use the latest v1 release on [GitHub](https://github.com/bringauto/etna/tree/v1.2.2).

## Requirements

- install Docker (version >= 20.10)
- install docker compose (version >= 1.29)

## Usage

Docker compose file has multiple profiles so the developer can disable/enable parts of the system he needs

### Docker compose profiles

#### Profiles that start logical groups of containers

- **all** - start all containers
- **for-virtual-fleet** - start the fleet protocol HTTP API server, the related PostgreSQL database, the fleet management integration layer, virtual fleet management, the fleet management HTTP API server and the mission module display tool
- **core** - start only internal clients and Module Gateway
- **http-api** - start fleet protocol HTTP API server and the related PostgreSQL database
- **cloud** - start all the cloud services (exclude components deployed on a car)

#### Profiles that start all containers except the ones specified

- **without-module-gateway** - do not start Module Gateway
- **without-external-server** - do not start External Server
- **without-devices** - do not start internal clients
- **without-fleet-management** - do not start Virtual Fleet Management

#### Profiles that start only one container

- **virtual-vehicle** - start only the Virtual Vehicle
- **virtual-plc** - start only the Virtual PLC
- **mqtt** - start only the MQTT vernemq broker
- **module-gateway** - start only the Module Gateway
- **external-server** - start only the External Server

Now you can run `docker compose --profile <profile> up` where `profile` is the name of the profile above.

To run components with different arguments you can edit the configuration files placed under `configuration/<component_name>/` where `component_name` is the name of the component.

### HTTP API

To show the OpenAPI specification (the service must be running), visit [http://localhost:8080/v2/protocol/openapi.json](http://localhost:8080/v2/protocol/openapi.json).
To explore the API endpoints and entities, visit [http://localhost:8080/v2/protocol/ui](http://localhost:8080/v2/protocol/ui). More on Swagger UI
is [here](https://swagger.io/tools/swagger-ui/).

The HTTP API requires authentication via API keys. To access all its endpoints, you can use the
key `ProtocolStaticAccessKey`.

The database access information and message cleanup can be set in the `configuration/http-api/config.json` (this config
overwrites the original config from the http-api image).

### Fleet Management API

To show the OpenAPI specification (the service must be running), visit [http://localhost:8081/v2/management/openapi.json](http://localhost:8081/v2/management/openapi.json).
To explore the API endpoints and entities, visit [http://localhost:8081/v2/management/ui](http://localhost:8081/v2/management/ui). More on Swagger UI
is [here](https://swagger.io/tools/swagger-ui/).

The Fleet Management API requires authentication via API keys. To access all its endpoints, you can use the
key `ManagementStaticAccessKey`.

The database access information and the number of stored states and orders can be set
in `configuration/management-api/config.json` (this config overwrites the original config from the management-api
image).

### Virtual Fleet Management

Simulates the Fleet Management ([documentation](https://github.com/bringauto/virtual-fleet-management/blob/main/README.md).

The Virtual Fleet Management uses `env` variables to set:

- **ETNA_VFM_SCENARIO** : Changes the scenario that the Virtual Fleet Management will use.
- **ETNA_VFM_CONFIG** : Changes the configuration of the Virtual Fleet Management.

All the scenarios and configurations must be stored in the `configuration/virtual-fleet-management` directory, so the docker container has access to it.
Both variables have default values, so the Virtual Fleet Management can be started without setting them.

### Mission module display tool

The Mission Module Display Tool runs a simple web server to display the positions of vehicles on a map. By default, the server is available at `http://localhost:5000`. It utilizes the fleet protocol HTTP API to retrieve vehicle positions. Comprehensive documentation can be found [here](https://github.com/bringauto/mission-module-display-tool/blob/main/README.md).

### Common Issues

- external-server and module-gateway connect sequence
  - mqtt tends to be unstable in some cases, which could lead to problems in ES and MG communication. Consider
      changing the mqtt_timeout in ES config if there are connection problems (numbers greater than 15 and no multiples
      of 15 should be used)
postgresql databases - are created only on container creation (if you have an old container, it needs to be deleted)
- http APIs
  - by default API containers wait for the postgresql database to be available. If the database fails to initialize,
      the containers won't start

## MQTT IP and Port

The MQTT uses a standard plain (not encrypted) connection on port 1883 and an SSL-encrypted connection on port 8883.

There are [pregenerated certificate files] for both, server and client, however, it is not recommended to use those, and
they are there for Etna to work out-of-box.

If you generate new certificate files they must have the same name as the original, otherwise, you have to change the
paths in file `configuration/mosquitto/mosquitto.conf`.

> Directory `configuration/mosquitto/certs`, include files `cacert.pem` (certificate authority), `server.crt` (signed
> certificate for the server) and `server.key` (servers private key).

## Topics to listen

Each MQTT topic consists of `company_name` and `car_name`.

BringAuto has the following MQTT topics

- \<company_name>/\<vehicle_name>/module_gateway
- \<company_name>/\<vehicle_name>/external_server

where each variable can be changed by the .env file, variable names to be saved there are in parentheses.

- `company_name` is by default set to "bringauto" (COMPANY)
- `vehicle_name` is by default set to "virtual_vehicle" (VEHICLE_NAME)

Actual MQTT topics to which developers can connect by default settings are:

- bringauto/virtual_vehicle/module_gateway
- bringauto/virtual_vehicle/external_server

## Logs

Logs for each component can be found in the `docker_volumes` directory.
> The component directories are pre-created in the repository to avoid permission problems associated with docker
> volumes.

In case of a problem, please attach the `docker_volumes` directory to the Bug report.

## Example scripts

There are example scripts for sniffing communication and seeing the basics [scripts/]

## Bug solving

Docker container can have error similar to this:

``` log
Error: Invalid require_certificate value (false
Error found at /mosquitto/config/mosquitto.conf:2.
```

If this happens, make sure the mentioned file uses LF line ending. (CRLF doesn't work)

[Fleet]: https://github.com/bringauto/fleet

[pregenerated certificate files]: configuration/mosquitto/certs

[scripts/]: scripts/

[Summary]: https://ref.bringautofleet.com/r/protocol/v2/2.0.1/summary

[Fleet Protocol Requirements]: https://ref.bringautofleet.com/r/protocol/v2/2.0.1/protocol-requirements

[Internal Client]: https://ref.bringautofleet.com/r/protocol/v2/2.0.1/internal-client

[Module Gateway]: https://ref.bringautofleet.com/r/protocol/v2/2.0.1/module-gateway

[External Server]: https://ref.bringautofleet.com/r/protocol/v2/2.0.1/external-server

[Modules]: https://ref.bringautofleet.com/r/protocol/v2/2.0.1/modules

[Message Structure]: https://ref.bringautofleet.com/r/protocol/v2/2.0.1/message-structure

[Internal Client design]: https://ref.bringautofleet.com/r/protocol/v2/2.0.1/internal-client-design

[Module Gateway design]: https://ref.bringautofleet.com/r/protocol/v2/2.0.1/module-gateway-design

[External Server design]: https://ref.bringautofleet.com/r/protocol/v2/2.0.1/external-server-design

[HTTP API]: https://ref.bringautofleet.com/r/protocol/http-api/1.0.0/http-api

[HTTP API Wait Mechanism]: https://ref.bringautofleet.com/r/protocol/http-api/1.0.0/wait-mechanism
