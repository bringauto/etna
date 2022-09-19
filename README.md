
# BringAuto virtual development platform

It's intended to simplify development for [Fleet](https://github.com/bringauto/fleet) and The Autonomy developers.

The system can be used by docker-compose stored at the git root of this repository.

There are four containers

- Mosquitto MQTT broker (bringauto-mosquitto)
- Virtual Vehicle Utility - Car State Protocol client implementation (it connects to BringAuto Daemon and simulates an autonomous driving robot)
- Virtual Fleet - Industrial Portal Protocol implementation (substitutes Fleet Management)
- BringAuto Daemon - Industrial Portal Protocol (BringAuto platform) and Car State Protocol server implementation

To read more about the system architecture look at [BringAuto Google Disk]
to the [Cloud Platform Architecture](https://docs.google.com/document/d/1jgSrBhZm73j_DkxNMtRgBLvnh_K-MUsL7z576hUat-I/edit) document.

## Requirements

- install Docker (version >= 20.10)
- install docker compose (version >= 1.29)

## Usage


Docker compose file has multiple profiles so the developer can disable/enable parts of the system he needs

- all - start all containers including MQTT, virtual vehicle, daemon, and virtual fleet
- without-autonomy - do not start Virtual Vehicle Utility (The Autonomy simulation)
- without-fleet - do not start Virtual Fleet
- without-broker - do not start MQTT broker (you must change the IP address to external broker inside docker-compose)
- without-daemon - do not start BringAuto Daemon
- mosquitto - start only MQTT mosquitto broker
- core - start only MQTT broker and BringAuto Daemon

Now you can run `docker-compose --profile=<profile> up` where `profile` is the name of the profile above.

To run components with different arguments (to load different scenarios of Virtual Fleet) you can use the .env file  
run `docker-compose --env-file=<.env-file-path> --profile="all" up`, default path is `./.env`  
.env file example:
```
COMPANY="bringauto"
PLACE="default"
VEHICLE_NAME="BringAuto 2"
```
## MQTT IP and Port
The MQTT uses a standard plain (not encrypted) connection on port 1883 and an SSL encrypted connection on port 8883.

There are [pregenerated certificate files](configuration/mosquitto/certs) for both, server and client, however, it is not recommended to use those, and they are there for Etna to work out-of-box.

If you generate new certificate files they must have the same name as the original, otherwise, you have to change the paths in file `configuration/mosquitto/mosquitto.conf`.

> Directory `configuration/mosquitto/certs`, include files `cacert.pem` (certificate authority), `server.crt` (signed certificate for the server) and `server.key` (servers private key).

## Topics to listen

Each MQTT topic consist from `company_name` and `car_name`.

BringAuto has the following MQTT topics
- \<company_name>/\<place>/\<vehicle_name>/daemon
- \<company_name>/\<place>/\<vehicle_name>/industrial_portal

where each variable can be changed by the .env file, variable names to be saved there are in parentheses.
- `company_name` is by default set to "bringauto" (COMPANY)
- `place` is by default set to "default" (PLACE)
- `vehicle_name` is by default set to "BringAuto Virtual" (VEHICLE_NAME)


Actual MQTT topics to which developers can connect by default settings are:
- bringauto/default/BringAuto Virtual/daemon
- bringauto/default/BringAuto Virtual/industrial_portal


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


[Industrial Portal]: https://github.com/bringauto/industrial-portal
[Google Artifacts Registry]: https://console.cloud.google.com/artifacts/docker/bringauto-infrastructure/europe-west1/virtual-platform?hl=cs&project=bringauto-infrastructure
[Cloud System Architecture]: https://docs.google.com/document/d/1jgSrBhZm73j_DkxNMtRgBLvnh_K-MUsL7z576hUat-I
[BringAuto Google Disk]: https://drive.google.com/drive/u/0/folders/1ZE9VRs86QtP6GqTJBl6vRJLmkh1lTEc5
[scripts/]: scripts/
