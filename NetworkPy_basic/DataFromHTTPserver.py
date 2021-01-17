import urllib.request

import argparse

REMOTE_HOST="https://spidersweb.pl/plus"
class HTTPclient:

    def __init__(self,host):
        self.host=host

    def fetch(self):
        res=urllib.request.urlopen(self.host)

        data=res.read()
        text=data.decode('utf-8')
        return text

if __name__=="__main__":

    parser=argparse.ArgumentParser("HTTP_CLIENT")
    parser.add_argument('--host', action="store", dest="host",default=REMOTE_HOST)
    given_args=parser.parse_args()
    host=given_args.host
    client=HTTPclient(host)

    print(client.fetch())
