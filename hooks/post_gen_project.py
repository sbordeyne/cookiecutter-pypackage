#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    if 'Proprietary' == '{{ cookiecutter.licence }}':
        remove_file('LICENSE')

    if '{{ cookiecutter.use_docker | lower}}' != 'y':
        remove_file('docker-compose.yml')
        remove_file('Dockerfile')
        remove_file('scripts/build_docker.py')
        remove_file('scripts/push_docker.py')
