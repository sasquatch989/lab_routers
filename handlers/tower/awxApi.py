import json
import subprocess
import os
import logging
# # Make dynamic for project seperation

def get_token():
    if not os.getenv('TOWER_TOKEN'):
        login = subprocess.run(['awx', 'login'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    try:
        if json.loads(login.stdout)['token']:
            os.environ['TOWER_TOKEN'] = json.loads(login.stdout['token'])
    except json.decoder.JSONDecodeError:
        print(login.stdout.decode())
        exit()


def api_call():
    project_id = json.loads(
        subprocess.run(
            ['awx', 'projects', 'list', '--name', 'lab-routers'],
            stdout=subprocess.PIPE
        ).stdout
    )['results'][0]['id']

    return subprocess.run(['awx', 'projects', 'update', project_id])


if __name__ == '__main__':
    get_token()
    api_call()
