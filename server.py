#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind('', 8888)

print('listening on port 8888')

while True:
    data, addr = s.recvfrom(4096)

    if data:
        for i in range(0, len(data)):
            print(data[i])
        print (data, addr)
        s.sendto(data, addr)