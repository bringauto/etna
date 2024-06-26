
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
- run the script by `python3 third_party_monitoring.py`
- it may need recompiled protobuf files with following commands:
- - `git submodule update --init --recursive`
- - `protoc -I"$(pwd)/../autonomy-host-protocol/" --python_out=. "$(pwd)/../autonomy-host-protocol/CarStateProtocol.proto"`
- - `protoc -I"$(pwd)/../autonomy-host-protocol/" --python_out=. "$(pwd)/../autonomy-host-protocol/IndustrialPortalProtocol.proto"`

### fleet-init

- initializes the fleet management database with stops and routes
- run the script by `python3 fleet-init/main.py -c init_config.ini -m maps -d`
- is a submodule so it needs to be initialized by:
- - `git submodule update --init --recursive`

## Arguments

### third_party_monitoring

- `-i` or `--ip-address` -- ip address of the MQTT broker, default is 172.17.0.1
- `-p` or `--port` -- port of the MQTT broker, default is 8883
- `--ca-certs` -- certificate authority, default is ./certs/ca-chain.pem
- `--certfile` -- client certificate, default is ./certs/client.pem
- `--keyfile` -- key to client certificate, default is ./certs/client.key
