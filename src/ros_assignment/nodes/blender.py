#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import bpy

#Global variables
vel_msg = Twist()
speed = 8
obj = bpy.data.objects["Cube"]

#Publisher
def publisher(distance,vel_msg):
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    #Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_distance = 0
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

# mobility function
def mobilize():
    #get the current position and angle of object(Inital)
    x0 = obj.location.x  #get value of blender object's x position
    z0 = obj.location.z  #get value of blender object's z position
    #delay few seconds
    time.sleep(0.1)
    #get the position and rotation of object now (Final)
    x1 = obj.location.x  #get value of blender object's new x position
    z1 = obj.location.z  #get value of blender object's new z position
    #subtract Intial position from Final position
    x = x1 - x0 #get change in position of x-axis
    z = z1 - z0 #get change in position of z-axis
    #calcuate distance and angle change with direction
    distance =  x
    z = z*2*3.14/360    #change radian to degree
    #allocate the vel_msg value properly(Update vel_msg)
    vel_msg.linear.x = x
    vel_msg.angular.z = z
    #publish the result to topic
    publisher(distance,vel_msg)

# Main function
if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            mobilize()
    except rospy.ROSInterruptException: pass
