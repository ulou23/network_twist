from aiohttp import web
from marshmallow import fields, Schema
from webargs.aiohttpparser import use_args

from elasticsearch_dsl import connections

import aiohttp_cors

from __backend_aiohttp import search

async def handle(request:web.Request)-> web.Response:
    return web.Response(body='<h2> Love </h2>', content_type='text/html')



# def setup_config(app):
#     app['config']=

def setup_routes(app):
    app.router.add_routes(search.routes)

def setup_cors(app):
    cors=aiohttp_cors.setup(
        app,
        defaults={"*":aiohttp_cors.ResourceOptions()}  ,
    )
    for r in list(app.router.routes()):
        cors.add(r)
    app['cors']=cors

async def setup_DB(app):
    app['db']=co

def init_app():
    app=web.Application()

    #setup_config(app)
    setup_routes(app)
    setup_cors(app)

    app.on_startup.append(setup_DB)

    return app