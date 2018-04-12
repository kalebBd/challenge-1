import socket
import bge
import sys

def motionreader():
    global x,y,teta,msg
    x = obj.getLinearVelocity(True).x / 240 # linear
    teta = obj.getAngularVelocity(True).z / 10 # rotation
    msg = str(x) + ' ' + str(teta)
    print(msg)

def init():
    #Global variables
    global x,y,teta,s,obj,msg
    x = 5.5
    y=5.5
    teta=0
    msg = '1 0'
    obj = bge.logic.getCurrentController().owner

    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = socket.gethostname()

    port = 12345

    # connection to hostname on the port.
    s.connect((host, port))

    # Receive no more than 1024 bytes
    smsg = s.recv(1024).decode('ascii')
    print(str(smsg))


if __name__ == "__main__":
    init()
    motionreader()
    s.send(msg.encode('ascii'))
