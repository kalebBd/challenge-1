#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import numpy as np
import cv2
from time import gmtime, strftime

#function for capturing Image
def captureImage():
    # initialize the camera
    camera_port = 0 # 0 -> index of camera
    camera = cv2.VideoCapture(camera_port)
    s, img = camera.read()
    image = 'pic_' + strftime("%Y_%m_%d_%H_%M_%S", gmtime()) + '.jpg'
    name = '../images/'
    for title in image:
        if title == '.':
            break
        name = name + title
    if s:    # frame captured without any errors
        cv2.namedWindow("cam-test",cv2.WINDOW_AUTOSIZE)
        cv2.imshow("cam-test",img)
        keypressed = cv2.waitKey(0)
        if keypressed == 27:         # wait for ESC key to exit
            cv2.destroyAllWindows()
        elif keypressed == ord('s'): # wait for 's' key to save and exit
            name = name + '_cam'
            cv2.imwrite(name+'.png',img)
            print('Saved image as ' + name + '.png')
            #cv2.destroyAllWindows()
        camera.release()
    else:
        print('Error saving image')
    del(camera)
    return name

#message Publisher
def publisher(img_msg):
    # Starts a new node
    rospy.init_node('image_capture')
    image_publisher = rospy.Publisher('/phrases', String, queue_size=10)
    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
        #Publish the image
        image_publisher.publish(img_msg)
        rate.sleep()
    #Force stop
    rospy.spin()

#main function
if __name__ == '__main__':
    print('\nClick "s" key on keyboard, to convert image to grayscale.')
    publisher(captureImage())
