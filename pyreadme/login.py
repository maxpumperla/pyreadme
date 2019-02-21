import requests 
import json

from .config import get_host, set_project, store_project_config
from .config import is_project_config_defined, get_project_config


def login(project, email=None, password=None):
    '''Log into a readme.io project with email and password. If you already
    logged into the same project from this machine, pyreadme will have stored
    your credentials for you and you only need to specify the project.
    '''

    if email is None or password is None:
        set_project(project)
        if not is_project_config_defined():
            raise Exception("No project configuration found. Try logging in with email and password first")
        data = get_project_config()
    else:
        data = {
            'email': email, 
            'password': password, 
            'project': project
        } 

    response = requests.post(url = '{}/api/v1/login'.format(get_host()), data = data)
    
    if response.ok:
        set_project(project)
        content = json.loads(response.content)
        api_key = content.get('apiKey')
        data['api_key'] = api_key
        store_project_config(data)
    else:
        raise Exception("Unable to authenticate. Check email and password for this project.")
