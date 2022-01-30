{% set is_open_source = cookiecutter.license != 'Proprietary' -%}
# {{ cookiecutter.project_name }}

{% if is_open_source %}
[![PyPI](https://img.shields.io/pypi/v/{{cookiecutter.project_slug}}.svg)](https://pypi.python.org/pypi/{{cookiecutter.project_slug}})
[![Documentation Status](https://readthedocs.org/projects/{{cookiecutter.project_slug | replace("_", "-")}}/badge/?version=latest)](https://readthedocs.org/projects/{{cookiecutter.project_slug | replace("_", "-")}}/badge/?version=latest)
{%- endif %}


{{ cookiecutter.project_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.license }} license
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

## Features

* TODO
