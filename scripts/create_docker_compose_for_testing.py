#!/usr/bin/env python3

import json
import os.path
import subprocess
import argparse
from ruamel.yaml import YAML


def argument_parser_init() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='docker-compose.yml creation tool')
    parser.add_argument('-c', '--config', type=str, default='./docker_compose_config.json', help='configuration file')
    parser.add_argument('-o', '--output', type=str, default='./', help='output directory for docker-compose.yml')
    return parser.parse_args()


def build_docker_image(component):
    if os.path.isfile(os.path.join(component['path'], 'Dockerfile')):
        print(f"Building docker image for {component['name']}")
        command = (f"docker build {'--no-cache ' if component['force_rebuild'] else ''}"
                   f"-t {component['name']}:testing -f {component['path']}/Dockerfile {component['path']}")
        rc = subprocess.call(command.split(" "), text=True)
        if rc != 0:
            print(f"Failed to build docker image for {component['name']}")
            return False
        return True
    else:
        print(f"Path provided for {component['name']} does not lead to a Dockerfile")
        return False


def replace_volumes(docker_compose, component, etna_path):
    volumes = docker_compose['services'][component['name']]['volumes']
    docker_compose['services'][component['name']]['volumes'] = []
    for volume in volumes:
        paths = volume.split(':')
        docker_compose['services'][component['name']]['volumes'].append(
            os.path.join(etna_path, paths[0]) + ":" + paths[1]
        )


def main():
    args = argument_parser_init()
    with open(args.config) as file:
        config = json.load(file)
    etna_path = os.path.abspath(config['etna_path'])
    yaml = YAML()
    yaml.preserve_quotes = True
    with open(os.path.join(etna_path, 'docker-compose.yml')) as file:
        docker_compose = yaml.load(file)

    for component in config['components']:
        if component['replace']:
            if not build_docker_image(component):
                return
            docker_compose['services'][component['name']]['image'] = f"{component['name']}:testing"
        replace_volumes(docker_compose, component, etna_path)
        docker_compose['services'][component['name']]['profiles'].append(f"{component['name']}-testing")

    with open(os.path.join(args.output, 'docker-compose.yml'), 'w') as file:
        yaml.indent(mapping=2, sequence=4, offset=2)
        yaml.dump(docker_compose, file)


if __name__ == '__main__':
    main()