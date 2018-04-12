#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import sys
import time
import thread
#sys.path.append("../../")
from appJar import gui
from random import *

#function that makes a random motion when random is pressed
def random():
    if not ending:  # Only do this if the Stop button has not been clicked
        # Starts a new node
        rospy.init_node('robot_cleaner', anonymous=True)
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        randomx = Twist()
        speed = randint(1,9)
        distance = randint(1,7)

        randomx.linear.x = speed
        randomx.angular.z = (speed+2)*2*PI/36

        #Since we are moving just in x-axis
        randomx.linear.y = 0
        randomx.linear.z = 0
        randomx.angular.x = 0
        randomx.angular.y = 0

        #Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        #Loop to move the turtle in an specified distance
        while(current_distance < distance):
            #Publish the velocity
            velocity_publisher.publish(randomx)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_distance= speed*(t1-t0)
        #After the loop, stops the robot
        randomx.linear.x = 0
        randomx.angular.z = 0
        #Force the robot to stop
        velocity_publisher.publish(randomx)
        #random()
        time.sleep(0)
        app.after(1,random)

#function that makes all motion by publishing according to the arguments
def move(forward,right):
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    speed = 10
    distance = 5

    if forward > 1:#move forward
        distance = 3
        speed = 5
        vel_msg.linear.x = speed
    elif forward == 0:#move backwards
        distance = 2
        speed = 3
        vel_msg.linear.x =  -speed
    else:#default do not move
        vel_msg.linear.x =  0
    if right > 1:#rotate clockwise
        #Converting from angles to radians
        speed = speed*2*PI/36
        distance = distance*2*PI/36
        vel_msg.angular.z = speed
    elif right == 0:#rotate anti-clockwise
        #Converting from angles to radians
        speed = speed*2*PI/36
        distance = distance*2*PI/36
        vel_msg.angular.z = -speed
    else:#default do not rotate
        vel_msg.angular.z =  0

    if forward == -8 and right == -8:#move with rotation in clockwise
        vel_msg.linear.x = speed - 5
        vel_msg.angular.z = (speed+2)*2*PI/36
    elif forward == -5 and right == -5:#move with rotation in anti-clockwise
        vel_msg.linear.x = speed - 5
        vel_msg.angular.z = -(speed+2)*2*PI/36
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    #Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_distance = 0
    #Loop to move the turtle in an specified distance
    while(current_distance < distance):
        #Publish the velocity
        velocity_publisher.publish(vel_msg)
        #Takes actual time to velocity calculus
        t1=rospy.Time.now().to_sec()
        #Calculates distancePoseStamped
        current_distance= speed*(t1-t0)
    #After the loop, stops the robot
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    #Force the robot to stop
    velocity_publisher.publish(vel_msg)

#click listener to stop random turtle motion
def stop():
    global ending
    ending = True

#function identifying which button is pressed
def press(button):
    if button == "Cancel/Exit":
        print('Good Bye!!!\n See you again')
        app.stop()
    elif button == "Forward":
        print('forward')
        move(2,-1)
    elif button == "Backward":
        print('backward')
        move(0,-1)
    elif button == "Left":
        print('left')
        move(-1,2)
    elif button == "Right":
        print('right')
        move(-1,0)
    elif button == "Stop":
        print('stop')
        stop()
    elif button == "Random":
        print('random')
        print(randint(1,9))
        global ending
        ending = False
        random()
#function that makes a motion when left1 is pressed
def left(button):
    print('Left-Arc')
    move(-8,-8)
#function that makes a motion when right1 is pressed
def right(button):
    print('Right-Arc')
    move(-5,-5)

#instructions for users
def instructions():
    print('\n********************************')
    print('This is a GUI driver for turtlesim')
    print('**********************************')
    print('NOTE: Random button will automatically move the turtle in an undefinend path.')
    print('\tTo stop the motion you must press "Stop" button')
    print('\tOr close the application by pressing "Cancle/Exit" button')
    print('\n**********************************')
    print('**********************************')
    print('Enjoy the controlls and for more instructions read the "README" text.')

#Intitalizer function
def init():
    #global var
    global app, ending, PI
    app = gui()
    ending = False
    PI = 3.1415926535897
    # add & configure widgets - widgets get a name, to help referencing them later
    app.addLabel("title", "Turtle driver")
    app.setLabelBg("title", "red")
    app.setBg("orange")
    # link the buttons to the function called press
    app.addButtons(["Random", "Stop"], press)
    app.addButtons(["Forward"], press)
    app.addButtons(["Left", "Right"], press)
    app.addButtons(["Backward"], press)
    app.addButtons([ "Cancel/Exit"], press)
    #optionally more operative buttons for control
    app.addButtons(["Left1", "Right1"], [left, right])

#main function
if __name__ == '__main__':
    # start the GUI
    try:
        init()
        instructions()
        app.go()
    except rospy.ROSInterruptException: pass
