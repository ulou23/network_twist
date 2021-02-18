from elasticsearch_dsl import Document,Keyword,Text,Integer

class TestDB(Document):

    id=Keyword()
    name=Text()
    desc=Text()
    number=Integer()

    class Index:
        name="testdb"