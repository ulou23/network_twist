from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource
import time

class TimeR(Resource):
    isLeaf=True
    def render_GET(self,request):
        return "<html><body>%s</body></html>"% (time.ctime(),)
resource=TimeR()
fac=Site(resource)
reactor.listenTCP(8880,fac)
reactor.run()

