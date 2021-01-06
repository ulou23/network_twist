from twisted.internet import reactor
from twisted.web.server import Site,NOT_DONE_YET
from twisted.web.resource import Resource

from asyncFun import AsyncJSON

class bigint(Resource):
    def render_GET(self,request):
        length=int(request.args['length'][0])
        asyn=AsyncJSON(range(length)).beginProducing(request)
        asyn.addCallback(lambda ignored:request.finish())
        return NOT_DONE_YET
resource=bigint()
fac=Site(resource)
reactor.listenTCP(8880,fac)
reactor.run()

