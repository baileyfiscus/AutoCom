#Code to send data over particular socket

import socket

UDP_IP = "155.246.202.131"
UDP_PORT = 5005
MESSAGE = "Let there be red light!"
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE
sock = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
