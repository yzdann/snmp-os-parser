import json

from snmp_data_samples import snmp_samples_list
from parser import os_parser

if __name__ == "__main__":
    with open('versions.json', 'r') as file_:
        versions_json = json.load(file_)

    for snmp_data in snmp_samples_list:
        print(os_parser(versions_json, snmp_data))
