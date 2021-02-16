import os
import json

import panel as pn

from templates.template import template
from static.description import description
from static.css import css

pn.config.raw_css = [css,]

def get_static_file(path):
    site_root = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(site_root, path)

def get_static_json(path):
    return json.load(open(get_static_file(path)))

apps = get_static_json('static/apps.json')

tmpl = pn.Template(template)
tmpl.add_variable('description', description)
tmpl.add_variable('apps', apps['apps'])
tmpl.add_variable('badge', apps['badge'])

tmpl.servable()
