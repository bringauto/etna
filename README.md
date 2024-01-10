
# BringAuto virtual development platform

It's intended to simplify development for [Fleet] and The Autonomy developers.

The system can be used by docker-compose stored at the git root of this repository.

There are multiple containers

- Mosquitto MQTT broker (bringauto-mosquitto)
- Virtual Vehicle Utility - Mission module client implementation (it connects to Module Gateway and simulates an Mission module's autonomy device)
- Virtual PLC - IO module client
- Module Gateway - cpp implementation of Module Gateway with Mission, IO and example module support
- External server - server implementation with Mission, IO and example module support
- HTTP API Server - tool for communication with final endpoint, used by mission module
- PostgreSQL database - storage of the HTTP API api keys and the messages sent via the API

To read more about the system architecture look at Fleet Protocol v2 documentation:
- [Summary]
- [Internal Client]
- [Module Gateway]
- [External Server]
- [Modules]
- [Internal Client design]
- [Module Gateway design]
- [External Server design]

## Requirements

- install Docker (version >= 20.10)
- install docker compose (version >= 1.29)

## Usage


Docker compose file has multiple profiles so the developer can disable/enable parts of the system he needs

- all - start all containers including MQTT, virtual vehicle, daemon, and virtual fleet
- without-module-gateway - do not start Module Gateway
- without-external-server - do not start External Server
- without-devices - do not start internal clients
- core - start only internal clients and Module Gateway
- virtual-vehicle-utility - start only Virtual Vehicle Utility
- virtual-plc - start only Virtual PLC
- mosquitto - start only MQTT mosquitto broker
- module-gateway - start only Module Gateway
- http-api -  start HTTP API server and the related PostgreSQL database

Now you can run `docker-compose --profile=<profile> up` where `profile` is the name of the profile above.

To run components with different arguments you can edit the configuration files placed under configuration/<component>

### HTTP API
To show the OpenAPI specification (the service must be running), visit http://localhost:8080/openapi.json. 
To explore the API endpoints and entities, visit http://localhost:8080/ui. More on Swagger UI is [here](https://swagger.io/tools/swagger-ui/).

The HTTP API requires authentication via API keys. To access all its endpoints, you can use the key `StaticAccessKeyToBeUsedByDevelopersOnEtna`.

The database access information and message cleanup can be set in the `configuration/http-api/config.json` (this config overwrites the original config from the http-api image).

## MQTT IP and Port
The MQTT uses a standard plain (not encrypted) connection on port 1883 and an SSL encrypted connection on port 8883.

There are [pregenerated certificate files] for both, server and client, however, it is not recommended to use those, and they are there for Etna to work out-of-box.

If you generate new certificate files they must have the same name as the original, otherwise, you have to change the paths in file `configuration/mosquitto/mosquitto.conf`.

> Directory `configuration/mosquitto/certs`, include files `cacert.pem` (certificate authority), `server.crt` (signed certificate for the server) and `server.key` (servers private key).

## Topics to listen

Each MQTT topic consist from `company_name` and `car_name`.

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

In case of a problem please attach the `docker_volumes` directory to the Bug report.

## Example scripts

There are example scripts for sniffing communication and seeing the basics [scripts/]

## Bug solving
If your mosquitto logs contain lines as below, make sure mosquitto.conf file uses LF line ending. (CRLF doesn't work)
```
Error: Invalid require_certificate value (false
Error found at /mosquitto/config/mosquitto.conf:2.
```

[Fleet]: https://github.com/bringauto/fleet
[Google Artifacts Registry]: https://console.cloud.google.com/artifacts/docker/bringauto-infrastructure/europe-west1/virtual-platform?hl=cs&project=bringauto-infrastructure
[pregenerated certificate files]: configuration/mosquitto/certs
[scripts/]: scripts/
[Summary]: https://ref.bringautofleet.com/r/protocol/v2/summary
[Internal Client]: https://ref.bringautofleet.com/r/protocol/v2/internal-client
[Module Gateway]: https://ref.bringautofleet.com/r/protocol/v2/module-gateway
[External Server]: https://ref.bringautofleet.com/r/protocol/v2/external-server
[Modules]: https://ref.bringautofleet.com/r/protocol/v2/modules
[Internal Client design]: https://ref.bringautofleet.com/r/protocol/v2/internal-client-design 
[Module Gateway design]: https://ref.bringautofleet.com/r/protocol/v2/module-gateway-design
[External Server design]: https://ref.bringautofleet.com/r/protocol/v2/external-server-design
