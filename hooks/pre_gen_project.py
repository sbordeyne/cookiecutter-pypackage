
import os
import re
import subprocess
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

module_name = '{{ cookiecutter.project_slug}}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The project slug (%s) is not a valid Python module name. Please do not use a - and use _ instead' % module_name)

    #Exit to cancel project
    sys.exit(1)

subprocess.call(['git', 'init'])
subprocess.call(
    [
        'git', 'remote', 'add', 'origin',
        'git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.git'
    ]
)

os.symlink(
    os.path.join(PROJECT_DIRECTORY, 'git_hooks/pre-commit'),
    os.path.join(PROJECT_DIRECTORY, '.git/hooks/pre-commit')
)
os.symlink(
    os.path.join(PROJECT_DIRECTORY, 'git_hooks/commit-msg'),
    os.path.join(PROJECT_DIRECTORY, '.git/hooks/commit-msg')
)


