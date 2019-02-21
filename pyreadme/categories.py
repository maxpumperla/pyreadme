from pyreadme.config import get_host, get_auth
import requests
import json

def get_category(category_slug, version='v1.0'):
    """Get the category of this category slug.
    """
    url = get_host() + "/api/v1/categories/" + category_slug
    headers = {'x-readme-version': version}
    response = requests.request("GET", url, headers=headers, auth=get_auth())
    return json.loads(response.content)


def get_docs_by_category(category_slug, version='v1.0'):
    """Get all documents with the same category as the provided category slug.
    """
    url = get_host() + "/api/v1/categories/" + category_slug + "/docs"
    headers = {'x-readme-version': version}
    response = requests.request("GET", url, headers=headers, auth=get_auth())
    return json.loads(response.content)


def get_doc_slugs_by_category(category_slug, version='v1.0'):
    """Get a list of document slugs with this category slug.
    """
    docs = get_docs_by_category(category_slug, version)
    return [d.get('slug') for d in docs]