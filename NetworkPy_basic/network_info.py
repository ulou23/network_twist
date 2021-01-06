import socket

def print_machine_info():
    host=socket.gethostname()
    ipaddress=socket.gethostbyname(host)
    print(host)
    print("ip address %s " %ipaddress)

def remote_get_machine_info():
    remote_host="www.syllabus.com"
    try:
        print("ip address %s: %s" %(remote_host,socket.gethostbyname(remote_host)))
    except socket.error as err_msg:
        print (remote_host,err_msg)

from binascii import hexlify
def conv_ip4():
    host=socket.gethostbyname(socket.gethostname())
    ip_host=socket.inet_aton(host)
    unpacked_ip=socket.inet_ntoa(ip_host)

    print( "ip %s => packed %s => unpacked %s " %(host,hexlify(ip_host),unpacked_ip) )


if __name__ == '__main__':
    print_machine_info()
    remote_get_machine_info()
    conv_ip4()