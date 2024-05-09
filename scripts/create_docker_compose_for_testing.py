#!/usr/bin/env python3

import yaml
import json
import os.path
import subprocess

def main():
    with open('../docker-compose.yml', 'r') as file:
        docker_compose = yaml.load(file, Loader=yaml.FullLoader)
    with open('docker_compose_for_testing.json', 'r') as file:
        config = json.load(file)

    for component in config['components']:
        if component['replace']:
            if os.path.isfile(component['path']) and component['path'].endswith('/Dockerfile'):
                print(f"Building docker image for {component['name']}")
                command = f"docker build -t {component['name']}:testing -f {component['path']} {component['path'].replace('/Dockerfile', '')}"
                rc = subprocess.call(command.split(" "), text=True)
                if rc != 0:
                    print(f"Failed to build docker image for {component['name']}")
                    return
                docker_compose['services'][component['name']]['image'] = f"{component['name']}:testing"
            else:
                print(f"Path provided for {component['name']} does not lead to a Dockerfile")
                return
            
    with open('docker-compose.yml', 'w') as file:
        file.write(yaml.dump(docker_compose))

if __name__ == '__main__':
    main()