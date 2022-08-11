#!/usr/bin/env python
import os
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    if 'Proprietary' == '{{ cookiecutter.license }}':
        remove_file('LICENSE')

    if '{{ cookiecutter.use_docker | lower}}' != 'y':
        remove_file('docker-compose.yml')
        remove_file('Dockerfile')
        remove_file('scripts/docker.py')

subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', '[feat] Initial commit'])

os.symlink(
    os.path.join(PROJECT_DIRECTORY, 'git_hooks/pre-commit'),
    os.path.join(PROJECT_DIRECTORY, '.git/hooks/pre-commit')
)
os.symlink(
    os.path.join(PROJECT_DIRECTORY, 'git_hooks/commit-msg'),
    os.path.join(PROJECT_DIRECTORY, '.git/hooks/commit-msg')
)
