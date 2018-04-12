#!/usr/bin/env python
import rospy
from turtlesim.srv import SetPen
from turtlesim.srv import TeleportAbsolute
from turtlesim.srv import TeleportRelative
from std_srvs.srv import Empty as EmptyServiceCall

#Explanation of fractale
def message():
    print('\n************************************')
    print('\tFractale design by Kaleb.')
    print('************************************')
    print('Story and presuption: \n\t1. Ribbens interconnected \n\t2. A bamboo wheel tyre \n\t3. Fractured vision fly.')
    print('************************************')
    print('************************************')

#Hexagonal fractale with red color
def fractale1(angle):
    #TODO here
    color = angle + 1
    red = 200.0
    blue = (100+color)//255
    green = (50*color)//255
    turtle1_set_pen(red,blue,green,color//5,0)
    if angle > 0:
        turtle1_teleport_relative(3,0)
        turtle1_teleport_relative(0,1)
        fractale1(angle - 1)

#Triangular fractale with blue color
def fractale2(angle):
    #TODO here
    color = angle + 1
    red = (200.0/color)//255
    blue = (100+color)//255
    green = 250
    turtle1_set_pen(red,blue,green,color//5,0)
    if angle > 0:
        turtle1_teleport_relative(3,0)
        turtle1_teleport_relative(0,2)
        fractale2(angle - 1)

#combination of Hexagonal and Triangular fractals with depth argument
def fractale3(depth):
    #TODO here
    if depth > 0:
        fractale1(16)
        fractale2(6)
        fractale3(depth - 1)

#Intitalizer function
def init():
    global turtle1_set_pen,turtle1_teleport_absolute,turtle1_teleport_relative,clear_background
    rospy.wait_for_service('turtle1/set_pen')
    rospy.wait_for_service('clear')
    turtle1_set_pen = rospy.ServiceProxy('turtle1/set_pen', SetPen)
    turtle1_teleport_absolute = rospy.ServiceProxy('turtle1/teleport_absolute', TeleportAbsolute)
    turtle1_teleport_relative = rospy.ServiceProxy('turtle1/teleport_relative', TeleportRelative)
    clear_background = rospy.ServiceProxy('clear', EmptyServiceCall)
    turtle1_set_pen(255.0,0,0,0,0)
    turtle1_teleport_absolute(3,3,0)
    clear_background()

#main function
if __name__ == '__main__':
    try:
        message()
        init()
        fractale3(10)
    except rospy.ROSInterruptException: pass
