
# BringAuto virtual development platform

It's intended to simplify development for [Industrial Portal] and The Autonomy developers.

The system can be used by docker-compose sotred at the git root of the repository.

There are four containers

- Mosquitto MQTT broker (bringauto-mosquitto)
- Virtual Vehicle Utility - Car State Protocol client implementation (it connects to BringAuto Daemon)
- Virtual Industrial Portal - Industrial Portal Protocol implementation (Industrial Portal)
- BringAuto Daemon - Industrial Portal Protocol (BringAuto platform) and Car State Protocol server implemetation

To read more about the system architecture look at [BringAuto Google Disk]
to the [Cloud System Architecture] document.

## Requirements

- install Docker (version >= 20.10)
- install docker compose (version >= 1.29)

## Usage

Docker compose file has multiple profiles so the developer can disable/enable only parts he needs

- all - start all containers includeing MQTT, virtual vehicle and virtual industrial portal
- without-autonomy - do not start Virtual Vehicle Utility (The Autonomy)
- without-industrial-portal - do not start virtual Industrial Portal
- without-broker - do not start MQTT broker (you must change IP address to external broker inside docker-compose)

Now you can run `docker-compose --profile=<profile> up` where `profile` is name of the profile above.

## MQTT IP and Port

The MQTT uses standard plain (not encrypted) connection on port 1883.

IP: 10.5.0.2
Port: 1883

## Topics to listen

Each MQTT topic consist from `company_name` and `car_name`.

BringAuto has following MQTT topics

- \<company_name>/default/\<car_name>/daemon
- \<company_name>/default/\<car_name>/industrial_portal

where 
- `company_name` is set to "bringauto" (can be changed in docker-compose)
- `car_name` = "BringAuto Virtual" (can be change in docker-compose)

Actual MQTT topics to which developer can connect are

- bringauto/default/BringAuto Virtual/daemon
- bringauto/default/BringAuto Virtual/industrial_portal


## Logs

Logs for each component can be found at `docker_volumes` directory.

In case of problem please attach the `docker_volumes` directory to the Bug report.

## Example scripts

There are example scripts by which you can sniff communication, and see base 
[scripts/]


[Industrial Portal]: https://github.com/bringauto/industrial-portal
[Google Artifacts Registry]: https://console.cloud.google.com/artifacts/docker/bringauto-infrastructure/europe-west1/virtual-platform?hl=cs&project=bringauto-infrastructure
[Cloud System Architecture]: https://docs.google.com/document/d/1jgSrBhZm73j_DkxNMtRgBLvnh_K-MUsL7z576hUat-I
[BringAuto Google Disk]: https://drive.google.com/drive/u/0/folders/1ZE9VRs86QtP6GqTJBl6vRJLmkh1lTEc5
[scripts/]: scripts/
