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


    #ros turtle controller initalization
    rospy.wait_for_service('turtle1/set_pen')
    rospy.wait_for_service('clear')
    turtle1_set_pen = rospy.ServiceProxy('turtle1/set_pen', SetPen)
    turtle1_teleport_absolute = rospy.ServiceProxy('turtle1/teleport_absolute', TeleportAbsolute)
    turtle1_teleport_relative = rospy.ServiceProxy('turtle1/teleport_relative', TeleportRelative)
    clear_background = rospy.ServiceProxy('clear', EmptyServiceCall)
    turtle1_set_pen(200,100,50,2,0)
    turtle1_teleport_absolute(5.5,5.5,0)
    clear_background()


if __name__ == "__main__":
    try:
        init()
        while not rospy.is_shutdown():
            # establish a connection
            clientsocket,addr = serversocket.accept()
            clientsocket.send('Connected'.encode('ascii'))
            print('Tunning for message')
            # Receive no more than 1024 bytes
            msg = clientsocket.recv(1024).decode('ascii')
            print('recieved message')
            #receive a message from blender
            pose_input = str(msg)
            #parse and partionion message
            vector_str = shlex.split(pose_input)
            x = vector_str[0]
            teta = vector_str[1]
            #move turtle using relative motion
            turtle1_teleport_relative(float(x),float(teta))
            print ('vector position is at {}'.format(vector_str))
        clientsocket.close()

    except rospy.ROSInterruptException:
        clientsocket.close()
        pass
