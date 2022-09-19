#!/usr/bin/env python3

import argparse
import paho.mqtt.client as mqtt
import IndustrialPortalProtocol_pb2 as protocol
import CarStateProtocol_pb2 as car_state
import ssl
import signal

from google.protobuf.message import DecodeError


def signal_handler(sig, frame) -> None:
    exit(0)


def argument_parser_init() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Sniffing tool')
    parser.add_argument('-i', '--ip-address', type=str, default='172.17.0.1', help='ip address of the MQTT broker')
    parser.add_argument('-p', '--port', type=int, default=8883, help='port of the MQTT broker')
    parser.add_argument('--ca-certs', type=str, default='./certs/ca-chain.pem', help='Certificate authority')
    parser.add_argument('--certfile', type=str, default='./certs/client.pem', help='Client certificate')
    parser.add_argument('--keyfile', type=str, default='./certs/client.key', help='Key to client certificate')
    return parser.parse_args()


def print_status_message_state(state) -> None:
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


def print_status_message_position(position) -> None:
    print("\tposition:")
    print("\t\tlatitude:  %s" % position.latitude)
    print("\t\tlongitude: %s" % position.longitude)
    print("\t\taltitude:  %s" % position.altitude)


def print_status_message_stop(stop) -> None:
    print("\tstop: %s" % str(stop.to))


def print_status_message_server(server) -> None:
    if server.type == protocol.Status.ServerError.OK:
        print("server: OK")
    if server.type == protocol.Status.ServerError.SERVER_ERROR:
        print("server: SERVER_ERROR")


def print_status_message(status_message) -> None:
    print_status_message_server(status_message.server)
    print("Status:")
    print_status_message_state(status_message.carStatus.state)
    print_status_message_stop(status_message.carStatus.stop)
    print_status_message_position(status_message.carStatus.telemetry.position)


def print_statusResponse_message(status_response) -> None:
    print(f"StatusResponse: {status_response.type}\n")


def print_message_deamon(message) -> None:
    message_daemon = protocol.MessageDaemon()
    message_daemon.ParseFromString(message.payload)
    if(message_daemon.HasField("commandResponse")):
        print("commandResponse")
    elif(message_daemon.HasField("connect")):
        print("connect")
    elif(message_daemon.HasField("status")):
        print_status_message(message_daemon.status)


def print_message_industrial_portal(message) -> None:
    message_industrial_portal = protocol.MessageIndustrialPortal()
    message_industrial_portal.ParseFromString(message.payload)
    if(message_industrial_portal.HasField("connectReponse")):
        print("connectReponse")
    elif(message_industrial_portal.HasField("command")):
        print("command")
    elif(message_industrial_portal.HasField("statusResponse")):
        print_statusResponse_message(message_industrial_portal.statusResponse)


def on_message(client, userdata, message) -> None:
    print(f'topic: {message.topic}')
    if (message.topic.split('/')[-1] == 'daemon'):
        print_message_deamon(message)
    elif (message.topic.split('/')[-1] == 'industrial_portal'):
        print_message_industrial_portal(message)
    else:
        print(f'ERROR:\n\ttopic: {message.topic}\n')


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)

    args = argument_parser_init()
    client = mqtt.Client(client_id='Monitoring Test',
                         clean_session=None,
                         userdata=None,
                         protocol=mqtt.MQTTv5,
                         transport='tcp')
    client.on_message = on_message
    client.tls_set(ca_certs=args.ca_certs,
                   certfile=args.certfile,
                   keyfile=args.keyfile,
                   tls_version=ssl.PROTOCOL_TLSv1_2)
    client.connect(args.ip_address, port=args.port, keepalive=60)
    client.subscribe("#", qos=2)
    client.loop_forever(timeout=60)
