import socket
import sys
import argparse

host='localhost'
data_payload=2048
backlog=5     #max no clients in queued connections

def echo_server(port):
    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #reuse address port
    tcp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    #bind socket to port
    server_address=(host,port)
    print("Start echo server on %s port %s" % server_address)
    tcp_socket.bind(server_address)
    
    #listen clients
    tcp_socket.listen(backlog)
    while True:
        print("waiting receive")
        client,address=tcp_socket.accept()
        data=client.recv(data_payload)
        if data:
            print("Received Data %s" %data)
            client.send(data)
            print(" sent %s bytes back to %s" % (data,address))

            #end connection
            client.close()

if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Socket Server")
    parser.add_argument('--port',action="store",dest="port",type=int, required=True)
    given_arg=parser.parse_args()
    port=given_arg.port
    echo_server(port)


