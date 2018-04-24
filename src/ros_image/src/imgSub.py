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
    cv2.namedWindow('grayscaled', cv2.WINDOW_NORMAL)
    cv2.imshow("grayscaled",cv2.cvtColor(cv2.cvtColor(br.imgmsg_to_cv2(data), cv2.COLOR_BGR2RGB),cv2.COLOR_RGB2GRAY))
    #img = cv2.imread( br.imgmsg_to_cv2(data) ,0)
    cv2.namedWindow('ros_img_message', cv2.WINDOW_NORMAL)
    cv2.imshow("ros_img_message", br.imgmsg_to_cv2(data))
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
