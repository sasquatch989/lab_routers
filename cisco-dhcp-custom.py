#!/usr/bin/env python

"""
Example custom dynamic inventory script for Ansible, in Python.
"""

import os
import sys
import argparse

try:
    import json
except ImportError:
    import simplejson as json

class CiscoDHCPInventory(object):

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()

        # Called with `--list`.
        if self.args.list:
            self.inventory = self.get_inventory()
        # Called with `--host [hostname]`.
        elif self.args.host:
            # Not implemented, since we return _meta info `--list`.
            self.inventory = self.empty_inventory()
        # If no groups or vars are present, return an empty inventory.
        else:
            self.inventory = self.empty_inventory()

        print(json.dumps(self.inventory));

    # Example inventory for testing.
    def get_inventory(self):
        host_list = ['1.1.1.1', '2.2.2.2']
        inventory = {
            'lab-routers': {
                'hosts': host_list,
                'vars': {}
            },
            '_meta': {}
        }
        print(inventory)
        return inventory
    # Empty inventory for testing.
    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()

# Get the inventory.
CiscoDHCPInventory()