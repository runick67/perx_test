import aiohttp_jinja2
import jinja2
from aiohttp import web

import views


app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))
app.add_routes([web.get('/', views.index), web.post('/', views.post_task)])
web.run_app(app, host='localhost')
