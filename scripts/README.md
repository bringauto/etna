
# BringAuto Etna helper scripts

Directory contains scripts which help newcomers
understand how the BringAuto software and hardware platform works.

## Requirements

- Python (version >= 3.9)
- Protobuf (version == 3.20)
- BringAuto Etna docker compose environment prepared and running


## Prepare

- install requirements by `pip3 install -r ./requirements.txt`


## Scripts

### third_party_monitoring

- it helps to observe messages sent by BringAuto Daemon
- it may need recompiled protobuf files with following commands:
  - `git submodule update --init --recursive`
  - `protoc -I"$(pwd)/../autonomy-host-protocol/" --python_out=. "$(pwd)/../autonomy-host-protocol/CarStateProtocol.proto"`
  - `protoc -I"$(pwd)/../autonomy-host-protocol/" --python_out=. "$(pwd)/../autonomy-host-protocol/IndustrialPortalProtocol.proto"`
- run the script by `python3 third_party_monitoring.py`

#### Arguments

- `-i` or `--ip-address` -- ip address of the MQTT broker, default is 172.17.0.1
- `-p` or `--port` -- port of the MQTT broker, default is 8883
- `--ca-certs` -- certificate authority, default is ./certs/ca-chain.pem
- `--certfile` -- client certificate, default is ./certs/client.pem
- `--keyfile` -- key to client certificate, default is ./certs/client.key

### fleet-init

- initializes the fleet management database with stops and routes
- is a submodule so it needs to be initialized by:
  - `git submodule update --init --recursive`
- run the script by `python3 fleet-init/main.py -c init_config.ini -m maps -d`

### create_docker_compose_for_testing

- creates a new `docker-compose.yml` with docker images replaced by desired images built from local repositories
- the config file `docker_compose_for_testing.json` needs to be adjusted
  - `etna_path`: needs to point to the root directory of the etna repository
  - `name`: needs to match a service name from the original compose file
  - `replace`: to build a docker image from your local repository, change the tag to `true`
  - `path`: path to the root of the coresponding project (dockerfiles are taken from this directory)
  - `force_rebuild`: forces the docker image of that component to be rebuilt
- run the script by `python3 create_docker_compose_for_testing.py`

#### Config

```json
{
    "etna_path": "..",
    "components": [
        {
            "name": "name-of-component",
            "replace": false,
            "path": "../../path/to/project",
            "force_rebuild": false
        }
    ]
}
```

#### Arguments

- `-c` or `--config` -- path to config file, default is ./docker_compose_config.json
- `-o` or `--output` -- path to output directory for docker-compose.yml, default is ./
