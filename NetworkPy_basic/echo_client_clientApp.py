import socket
import  sys
import argparse

host='localhost'

def echo_client(port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_add=(host,port)
    print("connection to %s port %s" % server_add)
    sock.connect(server_add)

    try:
        mess="tekst will be echoed NADI"
        print("sending message %s" % mess)
        sock.sendall(mess.encode('utf-8'))
        amount_rec=0
        amount_exp=len(mess)
        while amount_rec<amount_exp:
            data=sock.recv(16)
            amount_rec+=len(data)
            print("received: %s " % data)
    except socket.error as e:
        print(f"Socket {e}")
    finally:
        print("closing commection")
        sock.close()

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description="Socket server ex gratio")
    parser.add_argument('--port',action='store',dest='port',type=int,required=True)
    given_args=parser.parse_args()
    port=given_args.port
    echo_client(port)