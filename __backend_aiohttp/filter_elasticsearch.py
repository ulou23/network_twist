from elasticsearch_dsl import Q
from marshmallow import ( Schema, post_load)



class FilterSchema(Schema):

    model_cls=None
    class Meta:
        strict=True

    @post_load(pass_many=False)
    def create_query(self,data,many, **kwargs):
        self.context['data']=data
        query=Q()

        for filter_name,filter_values in data.items():
            filter_method_name=self.fields[filter_name].metadata.get('filter_method')
            try:
                filter_func=getattr(self,filter_method_name)
            except TypeError:
                pass
            else:
                query=filter_func(query,filter_name,filter_values)

        search=self.model_cls.search()
        search.query=query

        return search
