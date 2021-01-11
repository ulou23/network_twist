import socket

def test_timeout_default():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #create socket
    print(s.gettimeout())
    s.settimeout(100)
    print("new" , s.gettimeout())

import argparse
import sys

def connect_socket_test():
    parser=argparse.ArgumentParser(description="SocketTests")
    parser.add_argument('--host',action="store",dest="host",required=False)
    parser.add_argument('--port',action="store",dest="port",type=int,required=False)
    parser.add_argument('--file',action="store",dest="file",required=False)

    given_args=parser.parse_args()
    host=given_args.host
    port=given_args.port
    filename=given_args.file

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("connect to host")
    s.connect((host,port))
    msg="GET %s HTTP/1.0\r\n\r\n" % filename
    s.sendall(msg.encode('utf-8'))

    buf=s.recv(2048)
    sys.stdout.write(buf.decode('utf-8'))

if __name__=="__main__":
    test_timeout_default()
    connect_socket_test()