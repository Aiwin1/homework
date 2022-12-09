import struct
import os
import socket
import sys


def socket_service_image():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("0.0.0.0", 40))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print("Wait For Connection")
    while True:
        sock, address = s.accept()
        deal_image(sock, address)


def deal_image(sock, address):
    print(f"Accept connection from {address}")
    while True:
        file_size = struct.calcsize('128sq')  
        print('file_size is', file_size)
        buf = sock.recv(file_size)
        print('buf is', buf)
        if buf:
            filename, filesize = struct.unpack('128sq', buf)
            print('filename:', filename.decode(), 'filesize:', filesize)
            fn = filename.decode().strip('\00')
            new_filename = os.path.join('/tmp/' + fn)
            recvd_size = 0
            fp = open(new_filename, 'wb')
            while not recvd_size == filesize:
                if filesize - recvd_size > 1024: 
                    data = sock.recv(1024) 
                    recvd_size = recvd_size + len(data)  
                else:
                    data = sock.recv(1024)  
                    recvd_size = filesize
                fp.write(data)
            fp.close()
        sock.close()
        break


if __name__ == '__main__':
    socket_service_image()

