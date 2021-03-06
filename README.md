# Makerspace Tool Tool [![Build Status](https://travis-ci.org/flynnguy/maxt_project.svg?branch=master)](https://travis-ci.org/flynnguy/maxt_project) [![codecov](https://codecov.io/gh/flynnguy/maxt_project/branch/master/graph/badge.svg)](https://codecov.io/gh/flynnguy/maxt_project)

## Local Development
1. Create a Python Virtual Environment
```bash
$ python3 -m venv ./maxt_venv
```

or

```bash
$ virtualenv -p python3 ./maxt_venv
```

1. Activate environment and install required packages
(Note: You'll need to activate everytime you load a new shell and want to do development)
```bash
$ source ./maxt_venv/bin/activate
$ pip install -r requirements.txt
```

1. Setup local database and admin user
```bash
$ cd maxt
$ python manage.py migrate
$ python manage.py createsuperuser
```

1. Run a local copy of the server
```bash
$ python manage.py runserver
```

## Deploying
When deploying to a production machine, please see `example_local_settings.py` for variables you will want to change.
