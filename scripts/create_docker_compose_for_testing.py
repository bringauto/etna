#!/usr/bin/env python3

import yaml
import json
import os.path
import subprocess

def main():
    with open('docker_compose_for_testing.json', 'r') as file:
        config = json.load(file)

    etna_path = os.path.abspath(config['etna_path'])
    with open(os.path.join(etna_path, 'docker-compose.yml'), 'r') as file:
        docker_compose = yaml.load(file, Loader=yaml.FullLoader)

    for component in config['components']:
        if component['replace']:
            if os.path.isfile(os.path.join(component['path'], 'Dockerfile')):
                print(f"Building docker image for {component['name']}")
                command = f"docker build -t {component['name']}:testing -f {component['path']}/Dockerfile {component['path']}"
                rc = subprocess.call(command.split(" "), text=True)
                if rc != 0:
                   print(f"Failed to build docker image for {component['name']}")
                   return
                docker_compose['services'][component['name']]['image'] = f"{component['name']}:testing"
            else:
                print(f"Path provided for {component['name']} does not lead to a Dockerfile")
                return
        volumes = docker_compose['services'][component['name']]['volumes']
        docker_compose['services'][component['name']]['volumes'] = []
        for volume in volumes:
            paths = volume.split(':')
            docker_compose['services'][component['name']]['volumes'].append(
                os.path.join(etna_path, paths[0]) + ":" + paths[1]
            )

    with open('docker-compose.yml', 'w') as file:
        file.write(yaml.dump(docker_compose))

if __name__ == '__main__':
    main()