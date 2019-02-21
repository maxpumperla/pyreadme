from pyreadme.config import get_auth, get_host

import requests 
import json


def get_project_details():
    """Get details of your project as Python dictionary.
    """
    url = "{}/api/v1/".format(get_host())
    response = requests.request("GET", url, auth=get_auth())
    return json.loads(response.content)