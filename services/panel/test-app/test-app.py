import panel as pn
import holoviews as hv

from template import template

tmpl = pn.Template(template)

tmpl.add_variable('app_title', '<h1>Custom Template App</h1>')

tmpl.add_panel('A', hv.Curve([1, 2, 3]))
tmpl.add_panel('B', hv.Curve([1, 2, 3]))

tmpl.servable();
