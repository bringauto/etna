#!/bin/bash

# Create the databases
psql -c 'CREATE DATABASE protocol_api;'
psql -c 'CREATE DATABASE management_api;'

# Connect to the protocol_api database and create the table
psql -d protocol_api -c '
CREATE TABLE api_keys (id INTEGER PRIMARY KEY, name TEXT, key TEXT);
INSERT INTO api_keys(id, name, key) VALUES (2, '\''test_api_key'\'', '\''ProtocolStaticAccessKey'\'');
'

# Connect to the management_api database and create the table
psql -d management_api -c '
CREATE TABLE api_keys (id INTEGER PRIMARY KEY, name TEXT, key TEXT, creation_timestamp BIGINT);
INSERT INTO api_keys(id, name, key, creation_timestamp) VALUES (2, '\''test_api_key'\'', '\''ManagementStaticAccessKey'\'', 0);
'