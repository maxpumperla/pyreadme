# pyreadme - Python interface for the readme.io HTTP API

NOTE: This library is pre-release and still in testing phase.

## Installation

```bash
git clone https://github.com/maxpumperla/pyreadme
cd pyreadme
python setup.py develop
```

## Getting started

First time you log into a new project, do:

```python
from pyreadme import login

login(project='your_readme.io_project', email='your@email', password='youR_P4ssWord')

```

pyreadme will store credentials for each project you have, so next time around you can simply do:

```python
login(project='your_readme.io_project')
```

and will be good to go. To get document details for a `slug` and a version of your docs, you do

```python
details = get_document_details(slug='your-slug', version='v1.0')
```

## Under development

- [x] Wrap complete HTTP API for version "v1"
- [ ] Add CLI
- [ ] Make it easy to manage readme.io projects from GitHub
- [ ] Add sufficient test suite