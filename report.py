import socket
import uuid
import requests 
#from api_nuc import msg
import json
import subprocess, sys



h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)
#print("Host Name is:" + h_name)


mac_address = uuid.getnode()
mac_address_hex = ''.join(['{:02x}'.format((mac_address >> elements) & 0xff) for elements in range(0,8*6,8)][::-1])
#print("mac addr "+mac_address_hex)

publicIP = requests.get('http://ipinfo.io/json').json()['ip']
#print("ip publico "+publicIP)


localIP = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]

#print("ip privado "+localIP)


var =  {'mac':mac_address_hex , 'pubIP': publicIP , 'localIP': localIP}

print(json.dumps(var)) 
exit(1)
