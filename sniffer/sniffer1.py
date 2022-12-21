import socket,struct,textwrap

def main():
    conn = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.ntohs(0x0800))
    #conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    conn.bind(('192.168.1.37',0))
    #conn.settimeout(5)
    #conn.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
 #receives all packets
    #conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    conn.settimeout(5)
    i=0
    while True:
        try:
            raw_data,addr=conn.recvfrom(2048)
            dest_mac,src_mac,eth_proto,data = eternet_frame(raw_data)
            print('Eternet Frame:')
            print("Destination:",dest_mac,",Source:",src_mac,",Protocal:",eth_proto)
        except:
            print("time out")
            pass

#Unpack Ethernet frame
def eternet_frame(data):
    dest_mac,src_mac,proto = struct.unpack('!6s6s2s',data[:14])
    return get_mac_addr(dest_mac),get_mac_addr(src_mac),socket.htons(proto),data[14:]

#Return properly formatted MAC address (ie AA:BB:CC:DD:EE:FF)
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format,bytes_addr)
    mac_addr = ':'.join(bytes_str).upper()
    return mac_addr

main()