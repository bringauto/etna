# Etna Testing Scenarios

This document outlines the procedures for testing the Etna system with both single and multiple vehicles. Follow the steps carefully to ensure accurate testing results.

## 1. Testing with One Vehicle

To test the system with a single vehicle:

1. **Start the entire Etna system**:

   ```bash
   docker compose --profile all up
   ```

   - This command will start one vehicle named `virtual_vehicle`, which will run the following missions:
      - **Mission 1**
      - **Mission 2**
      - **Mission 3**

   *All missions are described in the [Table of Missions](#table-of-missions) below.*

2. **Use the mission module display tool to inspect the vehicle's progress**:

## 2. Testing with Multiple Vehicles

1. **Start the Etna system without specific components**:

   ```bash
   docker compose --profile for-virtual-fleet up
   ```

   - This command will start the system excluding `virtual-vehicle`, `module-gateway`, and `external-server`.

2. **Configure the number of virtual vehicles in virtual fleet**:
   - Edit the configuration file to set the number of virtual vehicles in `config/virtual-fleet-config.json`

3. **Start the virtual fleet**:

   ```bash
   python3 VirtualFleetDocker.py
   ```

   - This command will start up to 7 virtual vehicles, named `virtual_vehicle_x` where `x` is a number from 1 to 7.
  
4. **Use the mission module display tool to inspect the vehicles' progress**:

### Vehicle Mission Assignments

- **virtual_vehicle_1**: Runs Mission 1, Mission 2, and Mission 3
- **virtual_vehicle_2**: Runs Mission 1 and Mission 2
- **virtual_vehicle_3**: Runs Mission 1 and Mission 3
- **virtual_vehicle_4**: Runs Mission 2 and Mission 3
- **virtual_vehicle_5**: Runs Mission 1
- **virtual_vehicle_6**: Runs Mission 3
- **virtual_vehicle_7**: Runs Mission 2

## 3. Testing Data Transmission After the VerneMQ Outage

1. **Start the Etna system without the MQTT broker**:

   ```bash
   docker compose --profile without-mqtt up
   ```

2. **Start the MQTT broker inside the Etna system**:

   ```bash
   docker compose --profile mqtt up
   ```

3. **Start InfluxDB**.
4. **Start the HTTP API sniffer**.
5. **Wait until the vehicle starts moving in the mission module display tool**.
6. **Stop the MQTT broker**:

   ```bash
   docker compose --profile mqtt down
   ```

7. **Wait some time so the virtual vehicle has a chance to pass through some stops**.
   *Ideally, wait until the HTTP API sniffer prints out warnings about "vehicle not found" because it ensures that important components have noticed the vehicle's absence.*
8. **Start the MQTT broker again**:

   ```bash
   docker compose --profile mqtt up
   ```

9. **Check if there are error messages reflecting passed stops during the outage in InfluxDB**.

## 4. Testing Data Transmission After the External Server Outage

1. **Start the Etna system without the external server**:

   ```bash
   docker compose --profile without-external-server up
   ```

2. **Start the external server inside the Etna system**:

   ```bash
   docker compose --profile external-server up
   ```

3. **Start InfluxDB**.
4. **Start the HTTP API sniffer**.
5. **Start the [MQTT sniffer](https://gitlab.bringauto.com/bring-auto/fleet-protocol-toolchain/mqtt-sniffer)**.
6. **Wait until the vehicle starts moving in the mission module display tool**.
7. **Stop the external server**:

   ```bash
   docker compose --profile external-server down
   ```

8. **Wait some time so the virtual vehicle has a chance to pass through some stops**.
9. **Start the external server again**:

   ```bash
   docker compose --profile external-server up
   ```

10. **Check if there are error messages reflecting passed stops during the outage in InfluxDB**.
11. **Use the MQTT reporting tool to check for information about the outage**.

## 5. Testing Data Transmission After the VerneMQ Outage while using Virtual Fleet

1. **Start part of the Etna system specifically for the virtual fleet**:

   ```bash
   docker compose --profile for-virtual-fleet up
   ```

2. **Start the MQTT broker inside the Etna**.

   ```bash
   docker compose --profile mqtt up
   ```

3. **Start the virtual fleet without the MQTT broker**.

   Inside the virtual fleet config file `config/virtual-fleet-config.json`, set the option `"start_mqtt": false` and run it.

   ```bash
   python3 VirtualFleetDocker.py
   ```

4. **Start InfluxDB**.

5. **Start the [HTTP API sniffer](https://gitlab.bringauto.com/bring-auto/fleet-protocol-toolchain/http-api-sniffer)**.
6. . **Wait until the vehicle starts moving in the mission module display tool**.
7. . **Stop the MQTT broker**:

   ```bash
   docker compose --profile mqtt down
   ```

8. **Wait some time so the virtual vehicle has a chance to pass through some stops**.
9. **Start the MQTT broker again**:

   ```bash
   docker compose --profile mqtt up
   ```

10. **Check if there are error messages reflecting passed stops during the outage in InfluxDB**.

## 6. Testing the Virtual Fleet While Messing with the Virtual Fleet Management

1. **Start the Etna system for the virtual fleet without virtual fleet management**:

   ```bash
   docker compose --profile for-virtual-fleet-without-fleet-management up
   ```

2. **Start the virtual fleet**.
3. **Start virtual fleet management**:
   *Ensure that there are scenarios for vehicles operated by the virtual fleet within the Virtual Fleet Manager.*
4. **Check if all vehicles with scenarios started moving**.
5. **Try to stop the virtual fleet management and check if all vehicles stopped moving at the last stop of their mission**.
6. **Start the virtual fleet management for a short period so all vehicles are ordered to start the next mission and check if all vehicles started moving and ended at the starting stop of the mission**.
7. **Try to "mess up" the virtual fleet management by starting and stopping it during the vehicles' missions and check if the vehicles are able to finish their missions**.

## 7. Testing the HTTP API Reporting Tool

1. **Start the whole Etna system**:

   ```bash
   docker compose --profile all up
   ```

2. **Start InfluxDB**.
3. **Start the HTTP API sniffer**.
4. **Use the HTTP API reporting tool**.
5. **Check if the data in the reporting tool are consistent with the data in the Virtual Fleet Manager**:
   Mainly focus on the file `route_char.txt` where all missions that the vehicle completed should be displayed.

## 8. Test Vehicle State

1. **Set a short time interval for virtual vehicle stops**:
   1. In Etna, navigate to the file `configuration/virtual-vehicle-utility/config.json`.
   2. In this file, change the value of `"wait-at-stop-s"` to 2.

2. **Start the whole Etna system**:

   ```bash
   docker compose --profile all up
   ```

3. **Start InfluxDB**.
4. **Start the HTTP API sniffer**.
5. **After a while, check that there is a state change to "IN_STOP" for each passed stop in InfluxDB**.

## Table of Missions

The following table outlines the routes and stops for each mission:

| Mission  | Route                | Stops                                  |
|----------|----------------------|----------------------------------------|
| Mission 1 | Moravské náměstí 2  | Svatopluka Čecha A, Těšínská           |
| Mission 2 | Roundabout long     | Charvatská A, Svatopluka Čecha B, Slovinská, Bulharská |
| Mission 3 | Moravské náměstí 1  | Těšínská, Vodova                       |
