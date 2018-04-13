#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import sys
#sys.path.remove('/opt/ros/jade/lib/python2.7/dist-packages')
import cv2

def callback(data):
    br= CvBridge()
    rospy.loginfo('receiving image')
    #cv2.imshow("camera",cv2.cvtColor(br.imgmsg_to_cv2(data), cv2.COLOR_BGR2RGB))
    cv2.imshow("processed", br.imgmsg_to_cv2(data))
    cv2.waitKey(1)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/camera/image_raw', Image, callback)
    #rospy.Subscriber('imager', Image, callback)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        print('\n________________________\n\t Started subscriber \n_______________________________')
        listener()
    except rospy.ROSInterruptException:
        pass
#rosrun image_view image_view image:=/camera/image_raw
