import socket
import bpy
import sys

def motionreader():
    global x,y,teta,msg
    x = obj.location.x
    y = obj.location.y
    teta = obj.location.z #rotation
    msg = str(x) + ' ' + str(y) + ' ' + str(teta)
    print(msg)

def init():
    #Global variables
    global x,y,teta,s,obj,msg
    x = 5.5
    y=5.5
    teta=0
    msg = '1 1 0'
    obj = bpy.data.objects["Cube"]

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
