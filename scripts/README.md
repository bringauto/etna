
# BringAuto Etna helper scripts

Directory contains scripts which helps newcomers
to understand how the BringAuto software and hardware platform works.

## Requirements

- Python (version >= 3.9)
- Protobuf (version == 3.17)
- BringAuto Etna docker compose environment prepared and running


## Prepare

- install requirements by `pip3 install -r ./requirements`
- in the scripts directory run

```
protoc -I"$(pwd)/../autonomy-host-protocol/" --python_out=. "$(pwd)/../autonomy-host-protocol/CarStateProtocol.proto"
protoc -I"$(pwd)/../autonomy-host-protocol/" --python_out=. "$(pwd)/../autonomy-host-protocol/IndustrialPortalProtocol.proto"
```

## Scripts

- third_party_monitoring helps to observe messages send by BringAuto Daemon.
  just run the script by `python3 ./third_party_monitoring.py`
