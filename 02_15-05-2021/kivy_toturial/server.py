import socket
import time
import pickle



HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    ClientSocket, Adress = s.accept()
    print(f"Connection from {Adress} has ben established!")

    d = {1: "Hey", 2: "There"}
    msg = pickle.dumps(d)

    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") +msg
    ClientSocket.send(msg)
