#!/usr/bin/env python3

import json
import subprocess
import os
import logging

#   TODO Make dynamic for project separation, will want to add better variable checks, exceptions,
#     pass variables to class


class AWX:
    def get_token(self):
        if not os.getenv('TOWER_TOKEN'):
            login = subprocess.run(['awx', 'login'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            return
        try:
            if json.loads(login.stdout)['token']:
                print('Getting a new token')
                os.environ['TOWER_TOKEN'] = json.loads(login.stdout)['token']
                return # os.environ['TOWER_TOKEN']
        except json.decoder.JSONDecodeError:
            print(login.stdout.decode())
            exit()

    def api_call(self):
        print('Calling API')
        project_id = json.loads(
            subprocess.run(
                ['awx', 'projects', 'list', '--name', 'lab-routers'],
                stdout=subprocess.PIPE
            ).stdout
        )['results'][0]['id']

        return subprocess.run(['awx', 'projects', 'update', str(project_id)])


if __name__ == '__main__':
    awx = AWX()
    awx.get_token()
    awx.api_call()
