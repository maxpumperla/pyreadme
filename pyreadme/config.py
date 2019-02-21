import os
import json
from requests.auth import HTTPBasicAuth

def mkdir(x):
    if not os.path.isdir(x):
        os.mkdir(x)

HOST = 'https://dash.readme.io'
USER_PATH = os.path.expanduser('~')
PYREADME_DIR = os.path.join(USER_PATH, '.pyreadme')
mkdir(PYREADME_DIR)

PROJECT_NAME = None
PROJECT_DIR = None

def is_project_config_defined():
    return os.path.isfile(config_file())


def check(f):
    def wrapper(*args, **kwargs):
        if PROJECT_NAME is None:
            raise Exception(
                'No project found! Set project using pyreadme.set_project()')
        mkdir(PROJECT_DIR)
        return f(*args, **kwargs)
    return wrapper


def set_project(project):
    global PROJECT_NAME
    global PROJECT_DIR
    PROJECT_NAME = project
    if project is None:
        PROJECT_DIR = None
    else:
        PROJECT_DIR = os.path.join(PYREADME_DIR, project)
        mkdir(PROJECT_DIR)


@check
def get_project():
    return PROJECT_NAME


def get_host():
    return HOST


def get_base_dir():
    path = os.environ.get('PYREADME_CLASS_PATH')
    if path is None:
        return PYREADME_DIR
    return path


@check
def config_file():
    return os.path.join(PROJECT_DIR, 'config.json')


@check
def store_project_config(config):
    with open(config_file(), 'w') as f:
        f.write(json.dumps(config))


@check
def get_project_config():
    with open(config_file(), 'r') as f:
        config = json.load(f)
    return config


@check
def get_auth():
    config = get_project_config()
    api_key = config.get('api_key')
    auth = HTTPBasicAuth(api_key, '')
    return auth
