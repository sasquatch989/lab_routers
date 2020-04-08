#!/usr/bin/env python

"""
Example custom dynamic inventory script for Ansible, in Python.
"""


import argparse
import json
from subprocess import check_output
import re


class CiscoDHCPInventory(object):
    print('In the class now')
    def __init__(self):
        self.inventory = {}
        self.read_cli_args()

        # Called with `--list`.
        print('Called with --list')
        if self.args.list:
            self.inventory = self.get_inventory()
        # Called with `--host [hostname]`.
        print('Called with --host')
        elif self.args.host:
            # Not implemented, since we return _meta info `--list`.
            self.inventory = self.empty_inventory()
        # If no groups or vars are present, return an empty inventory.
        else:
            self.inventory = self.empty_inventory()

        print(json.dumps(self.inventory));

    # Getting inventory
    def get_inventory(self):
        print('Getting inventory')
        out = check_output(['ssh', 'admin@172.20.20.1', "sh ip dhcp bind a | inc 01.*08"])
        print(out)
        host_list = [i for i in out.decode().split() if re.match('\d+\.\d+\.\d+\.\d+',i)]
        print(host_list)
        return {
            'lab-routers': {
                'hosts': host_list
            },
            '_meta': {
                'hostvars': {}
            }
        }

    # Empty inventory for testing.
    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action='store_true')
        parser.add_argument('--host', action='store')
        self.args = parser.parse_args()


# Get the inventory.
CiscoDHCPInventory()