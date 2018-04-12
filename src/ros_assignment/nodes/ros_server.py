#!/usr/bin/env python
import rospy
from turtlesim.srv import SetPen
from turtlesim.srv import TeleportAbsolute
from turtlesim.srv import TeleportRelative
from std_srvs.srv import Empty as EmptyServiceCall
import socket
import shlex

def init():
    #Global variables
    global serversocket,turtle1_set_pen,turtle1_teleport_absolute,turtle1_teleport_relative,clear_background
    # create a socket object
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = socket.gethostname()

    port = 12345

    # bind to the port
    serversocket.bind((host, port))

    # queue up to 5 requests
    serversocket.listen(5)

    # connection to hostname on the port.
    #serversocket.connect((host, port))

    #ros turtle controller initalization
    rospy.wait_for_service('turtle1/set_pen')
    rospy.wait_for_service('clear')
    turtle1_set_pen = rospy.ServiceProxy('turtle1/set_pen', SetPen)
    turtle1_teleport_absolute = rospy.ServiceProxy('turtle1/teleport_absolute', TeleportAbsolute)
    turtle1_teleport_relative = rospy.ServiceProxy('turtle1/teleport_relative', TeleportRelative)
    clear_background = rospy.ServiceProxy('clear', EmptyServiceCall)
    turtle1_set_pen(255.0,0,0,0,0)
    turtle1_teleport_absolute(5.5,5.5,0)
    clear_background()


if __name__ == "__main__":
    try:
        init()
        while not rospy.is_shutdown():
            # establish a connection
            clientsocket,addr = serversocket.accept()
            print('Tunning for message')
            # Receive no more than 1024 bytes
            msg = serversocket.recv(1024).decode('ascii')
            if msg:
                print('recieved message')
                #receive a message from blender
                pose_input = str(msg)
                #parse and partionion message
                vector_str = shlex.split(pose_input)
                x = vector_str[0]
                y = vector_str[1]
                teta = vector_str[2]
                #move turtle using absolute motion
                turtle1_teleport_absolute(float(x),float(y),float(teta))
                print ('vector position is at {}'.format(vector_str))
            print('Exited if condition')
        clientsocket.close()

    except rospy.ROSInterruptException: pass