import socket
import os
import sys
import struct


def sock_client_image(path):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("192.168.23.129", 40))
        except socket.error as msg:
            print(msg)
            print(sys.exit(1))
        file_path = path
        file = struct.pack(b'128sq', bytes(os.path.basename(file_path), encoding='utf-8'), 
                           os.stat(file_path).st_size)  
        s.send(file)
        fp = open(file_path, 'rb')
        while True:
            data = fp.read(1024)  
            if not data:
                print(f'{file_path}send over')
                break
            s.send(data)
        s.close()
        break


if __name__ == '__main__':
    path = input('input the path:')
    sock_client_image(path)

