#!/usr/bin/env python
import rospy
import roslib
roslib.load_manifest('pid')
import math
import time
import tf
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn


if __name__ == '__main__':
	rospy.init_node('turtle_beta_working')

	listener = tf.TransformListener()

	rospy.wait_for_service('spawn')
	spawner = rospy.ServiceProxy('spawn', Spawn)
	spawner(2, 2, 0, 'turtle2')
	turtle_vel = rospy.Publisher('turtle2/cmd_vel', Twist,queue_size=1000)

	rate = rospy.Rate(10.0)

	#delcaring variables
	PI = 3.1415926535897
	tp = time.time() - 1
	angErrPrev = PI / 4
	posErrPrev = 4.865
	#declaring PID constants
	kpp = 0.5
	kpa = 4
	kdp = 0.5
	kda = 0.5
	kip = 0.5
	kia = 0.5
	ia = 0
	ip = 0
	iat = 0.1
	ipt = 0.1

	while not rospy.is_shutdown():
        	try:
            		(trans,rot) = listener.lookupTransform('/turtle2', '/turtle1', rospy.Time(0))
       		except (tf.LookupException, tf.ConnectivityException):
            		continue

		#current time
		tc = time.time()

		angErr = math.atan2(trans[1], trans[0])
		posErr = math.sqrt(trans[0] ** 2 + trans[1] ** 2)

		#calculating P
		pp = kpp * posErr
		pa = kpa * angErr
		#calculating D
		dp = (posErr - posErrPrev) / (tc - tp)
		da = (angErr - angErrPrev) / (tc - tp)
		#calculating I
		#calculating ip
		if(abs(pp + dp) < ipt):
			if(posErr * posErrPrev >= 0):
				ip += 0.5 * abs(tc - tp) * abs(posErr - posErrPrev) + abs(tc - tp) * min(abs(posErr),abs(posErrPrev)) * posErr / abs(posErr)
			else:
				h = tp - posErrPrev * (tc - tp) / (posErr - posErrPrev)
				ip = 0.5 * posErrPrev * (h - tp) + 0.5 * posErr * (tc - h)
		else:
			ip = 0 
		#calculating ia
		if(abs(pa + da) < iat):
			if(angErr * angErrPrev >= 0):
				ia += 0.5 * abs(tc - tp) * abs(angErr - angErrPrev) + abs(tc - tp) * min(abs(angErr),abs(angErrPrev)) * angErr / abs(angErr)
			else:
				h = tp - angErrPrev * (tc - tp) / (angErr - angErrPrev)
				ia = 0.5 * angErrPrev * (h - tp) + 0.5 * angErr * (tc - h)
		else:
			ia = 0
			

		cmd = Twist()
		cmd.linear.x = pp + dp + ip
		cmd.angular.z = pa + da + ia
		turtle_vel.publish(cmd)

		#updating values
		posErrPrev = posErr
		angErrprev = angErr
		tp = tc

		rate.sleep()










