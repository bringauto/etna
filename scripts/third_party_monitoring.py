import paho.mqtt.client as mqtt
import IndustrialPortalProtocol_pb2 as protocol
import CarStateProtocol_pb2 as car_state
import ssl


def print_status_message_state(state):
    state_string = ""
    if(state == car_state.CarStatus.DRIVE):
        state_string = "DRIVE"
    if(state == car_state.CarStatus.ERROR):
        state_string = "ERROR"
    if(state == car_state.CarStatus.IDLE):
        state_string = "IDLE"
    if(state == car_state.CarStatus.IN_STOP):
        state_string = "IN_STOP"
    if(state == car_state.CarStatus.OBSTACLE):
        state_string = "OBSTACLE"
    print("\tstate: %s" % state_string)


def print_status_message_position(position):
    print("\tposition:")
    print("\t\tlatitude:  %s" % position.latitude)
    print("\t\tlongitude: %s" % position.longitude)
    print("\t\taltitude:  %s" % position.altitude)


def print_status_message_stop(stop):
    print("\tstop: %s" % str(stop.to))


def print_status_message_server(server):
    if server.type == protocol.Status.ServerError.OK:
        print("server: OK")
        print("stops:  []")
    if server.type == protocol.Status.ServerError.SERVER_ERROR:
        print("server: SERVER_ERROR")


def print_status_message(message):
    status_message = message.status
    print_status_message_server(status_message.server)
    print("Status:")
    print_status_message_state(status_message.carStatus.state)
    print_status_message_stop(status_message.carStatus.stop)
    print_status_message_position(status_message.carStatus.telemetry.position)
    print("")


def on_message(client, userdata, message):
    message_daemon = protocol.MessageDaemon()
    message_daemon.ParseFromString(message.payload)
    if message_daemon.HasField("commandResponse"):
        print("commandResponse")
    if message_daemon.HasField("connect"):
        print("connect")
    if message_daemon.HasField("status"):
        print_status_message(message_daemon)


client = mqtt.Client(client_id='Monitoring Test',
                     clean_session=None,
                     userdata=None,
                     protocol=mqtt.MQTTv5,
                     transport='tcp')

client.on_message = on_message

client.tls_set(ca_certs="../configuration/mosquitto/certs/cacert.pem",
               certfile="../configuration/mosquitto/certs/client/client.crt",
               keyfile="../configuration/mosquitto/certs/client/client.key",
               tls_version=ssl.PROTOCOL_TLSv1_2)
client.tls_insecure_set(True)

client.connect("172.17.0.1", port=8883, keepalive=60)

client.subscribe("bringauto/default/BringAuto Virtual/daemon", qos=2)

client.loop_forever(timeout=60)
