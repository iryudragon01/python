import socket,struct,textwrap,binascii,time,threading#you will need the win32 libraries for this snippet of code to work, Links below
import win32gui
from time import sleep
from scapy.all import *

from pynput.keyboard import Key,Controller
keyboard = Controller()
firstloop=0
found = False
#activate window
hd=win32gui.FindWindow(None,'sniper')
win32gui.SetForegroundWindow(hd)
keyboard.press(keyboard._KeyCode(115))
keyboard.release(keyboard._KeyCode(115))

def wink():
    win32gui.SetForegroundWindow(hd)
    keyboard.press(keyboard._KeyCode(80))
    keyboard.release(keyboard._KeyCode(80))
    
def sendkey(key):
    win32gui.SetForegroundWindow(hd)
    keyboard.press(keyboard.press(key))
    keyboard.release(keyboard.release(key))

    
#sniff(filter="ip", prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}"))
def actionNow():
    global firstloop,found
    while True:
        wink()
        scapy(packet_callback, filter="ip")
        sleep(1)
        if(firstloop>20):
            break
        print(firstloop)
    print("found")    
    found=True
    return


def packet_callback(packet):
    global firstloop,found
    # Check if the packet has the IP layer
    if packet.haslayer(IP):
        # Check if the destination IP address is "43.134.158.172"
        if packet[IP].dst == "43.134.158.172" :
            # Check if the packet has the Raw layer (contains data)
            if packet.haslayer(Raw):
                # Print the data contained in the packet
                data_raw=packet[Raw].load                
                hex_data = binascii.hexlify(data_raw).decode()
                action=data_raw[5:6]
                string=str(data_raw).find('x1a')
                #print(string,"   string")
                if action == b'\x15':
                    #print('wink')
                    pass
        # Check if the destination IP address is "43.134.158.172"
        if packet[IP].src== "43.134.158.172":
            # Check if the packet has the Raw layer (contains data)
            if packet.haslayer(Raw):
                # Print the data contained in the packet
                data_raw=packet[Raw].load                
                hex_data = binascii.hexlify(data_raw).decode()
                if len(data_raw)==1424 :
                    firstloop=0
                else:
                    firstloop=firstloop+1
                
                if(found):
                    f=open('fight.txt','a')
                    print(data_raw)
                    f.write(hex_data)
                    f.write('\n')
                    f.close()

f=open('fight3.txt','a')
threading.Thread(target=actionNow).start()

sniff(prn=packet_callback, filter="ip") 