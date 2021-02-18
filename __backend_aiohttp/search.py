import operator

from aiohttp import web
from marshmallow import fields
from webargs.aiohttpparser import use_args
from elasticsearch_dsl import Q

from functools import reduce

from __backend_aiohttp.filter_elasticsearch import FilterSchema
from __backend_aiohttp.models import TestDB


routes=web.RouteTableDef()

class NameFilterSchema(FilterSchema):

    model_CLS=TestDB

    name=fields.List(
        fields.Str(),
        description='Search x by name' ,
        filter_method='filter_name' ,
        required=False
    )
    number=fields.List(
        fields.Int(),
        description='Search x by number',
        filter_method='filter_nr',
        required=False
    )

    def filter_name(self,query,name,values):
        filter_query=reduce(
            operator.or_,
            (
                Q('match', name={ 'query':value})
                for value in values
            )
        )
        return query & filter_query

    def filter_number(self,query,name,values):
        return query & Q('terms',number=values)


@routes.get('/search, name="search')
@use_args(NameFilterSchema,location='query')
async def handle(request,filters):
    search=filters.execute()
    response={
        'data': [testdb.to_dict()for testdb in search.hits],
        'meta':{
            'search':filters.to_dict()
        }
    }
    return web.json_response(response)
