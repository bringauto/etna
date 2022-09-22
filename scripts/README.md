
# BringAuto Etna helper scripts

Directory contains scripts which helps newcomers
to understand how the BringAuto software and hardware platform works.

## Requirements

- Python (version >= 3.9)
- Protobuf (version >= 3.6)
- BringAuto Etna docker compose environment prepared and running


## Prepare

- install requirements by `pip3 install -r ./requirements.txt`


## Scripts

### third_party_monitoring

- it helps to observe messages send by BringAuto Daemon
- run the script by `python3 third_party_monitoring.py`

## Arguments

### third_party_monitoring

- `-i` or `--ip-address` -- ip address of the MQTT broker, default is 172.17.0.1
- `-p` or `--port` -- port of the MQTT broker, default is 8883
- `--ca-certs` -- certificate authority, default is ./certs/ca-chain.pem
- `--certfile` -- client certificate, default is ./certs/client.pem
- `--keyfile` -- key to client certificate, default is ./certs/client.key
