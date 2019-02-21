from pyreadme.config import get_host, get_auth
import requests
import json
import frontmatter


def get_document_details(slug, version='v1.0'):
    """Get a document details by document slug.
    """
    url = get_host() + "/api/v1/docs/" + slug
    headers = {'x-readme-version': version}
    response = requests.request("GET", url, headers=headers, auth=get_auth())
    return json.loads(response.content)


def update_document(md_file, slug, version='v1.0', extra_payload={}):
    '''Update a given document slug with the content of a provided markdown
    file `md_file`. If extra payload arguments are specified, they will be
    added to the request.

    Example usage: 
        update_document(md_file='/path/to/file.md', 
                        slug='xxx', version='v1.0', 
                        extra_payload={'parentDoc': '5c6c2f84a74d560013734d07'})

    '''
    url = get_host() + "/api/v1/docs/" + slug
    headers = {
        'x-readme-version': version,
        'content-type': "application/json",
    }
    with open(md_file, 'r') as f:
        try:
            post = frontmatter.load(f)
        except:
            raise Exception('Cannot read markdown file. Did you provide a valid file?')
   
    post_dict = post.to_dict()    
    payload = post_dict.copy()
    payload['body'] = payload.pop('content')
    payload.update(extra_payload)    

    response = requests.request("PUT", url, data=json.dumps(payload), headers=headers, auth=get_auth())
    return json.loads(response.content)


def delete_document(slug, version='v1.0'):
    """Delete a document by document slug.
    """
    url = get_host() + "/api/v1/docs/" + slug
    headers = {'x-readme-version': version}
    response = requests.request("DELETE", url, headers=headers, auth=get_auth())
    return json.loads(response.content)


def create_document(md_file, slug, version='v1.0', extra_payload={}):
    '''Create a document slug with the content of a provided markdown
    file `md_file`. If extra payload arguments are specified, they will be
    added to the request.

    TODO: how to create a doc in a given category?

    Example usage: 
        create_document(md_file='/path/to/file.md', 
                        slug='xxx', version='v1.0', 
                        extra_payload={'parentDoc': '5c6c2f84a74d560013734d07'})

    '''
    url = get_host() + "/api/v1/docs/" + slug
    headers = {
        'x-readme-version': version,
        'content-type': "application/json",
    }
    with open(md_file, 'r') as f:
        try:
            post = frontmatter.load(f)
        except:
            raise Exception('Cannot read markdown file. Did you provide a valid file?')
   
    post_dict = post.to_dict()    
    payload = post_dict.copy()
    payload['body'] = payload.pop('content')
    payload.update(extra_payload)    

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers, auth=get_auth())
    return json.loads(response.content)
