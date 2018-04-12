#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import numpy as np
import cv2

#function to display the gray image
def showGray(msg):
    name = msg.data
    img = cv2.imread( name+'.png' ,0)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)#if cv2.WINDOW_NORMAL it is resizable, else default cv2.WINDOW_AUTOSIZE
    cv2.imshow('image',img)
    keypressed = cv2.waitKey(0)
    if keypressed == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif keypressed == ord('s'): # wait for 's' key to save and exit
        name = name + '_gray'
        cv2.imwrite(name+'.png',img)
        print('Saved image as grayscale with name ' + name + '.png')
        cv2.destroyAllWindows()
    del( img )

#message Subscriber
def subscriber():
    # Starts a new node
    rospy.init_node('image_grayscaled')
    image_subscriber = rospy.Subscriber('/phrases', String, showGray)
    #Force stop
    rospy.spin()

#main function
if __name__ == '__main__':
    subscriber()
