#!/usr/bin/env python
import rospy
import roslib
roslib.load_manifest('ros_assignment')
import math
import tf
import geometry_msgs.msg
import turtlesim.srv

def message():
    print('\n*******************************')
    print('Turtle chaser with PID motion.')
    print('*******************************')
    print('Defining PID motion: \n\t 1. Chaser turtle decreases speed when approching turtle1. \n\t 2. Turtle2 does not take sharp corners like turtle1. \n\t 3. Speed of turtle2 is high when turtle1 is at a distance.')
    print('\n---------------------------------------------------')
    print('You can control the turtle1 by either keyboard keys.\n Or by running gui app assuming your directory is in rosworkspace, \n Run this command in new terminal \n\t"python src/ros_assignment/nodes/GUI_controller.py"')
    print('---------------------------------------------------')
    print('\n*******************************')
    print('*******************************')

if __name__ == '__main__':
    message()
    rospy.init_node('turtle_beta')

    listener = tf.TransformListener()

    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(2, 4, 0, 'turtle2')
    turtle_vel = rospy.Publisher('turtle2/cmd_vel', geometry_msgs.msg.Twist,queue_size=1)

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/turtle2', '/turtle1', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException):
            continue

        angular = 4 * math.atan2(trans[1], trans[0])
        linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
        cmd = geometry_msgs.msg.Twist()
        cmd.linear.x = linear
        cmd.angular.z = angular
        turtle_vel.publish(cmd)

        rate.sleep()
