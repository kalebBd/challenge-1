#!/usr/bin/env python
import rospy
import cv2
import cv_bridge
from std_msgs.msg import Header
from sensor_msgs.msg import Image
from realsense_camera.msg import IMUInfo

rospy.init_node('image_publisher', anonymous=True)
pub = rospy.Publisher("camera/image", Header, queue_size=10)
rate = rospy.Rate(5)

camera = cv2.VideoCapture(0)
while not rospy.is_shutdown():
    msg = Image()
    msg = camera.read() #rospy.CvImage(Header, "bgr8", img)
    pub.publish(msg)
    cv2.waitKey(0)
rospy.spin()
rate.sleep()
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <sstream> // for converting the command line parameter to integer


#  // Check if video source has been passed as a parameter
#  if(argv[1] == NULL) return 1;

#  ros::init(argc, argv, "image_publisher");
#  ros::NodeHandle nh;
#  image_transport::ImageTransport it(nh);
#  image_transport::Publisher pub = it.advertise("camera/image", 1);

#  // Convert the passed as command line parameter index for the video device to an integer
#  std::istringstream video_sourceCmd(argv[1]);
#  int video_source;
#  // Check if it is indeed a number
 # if(!(video_sourceCmd >> video_source)) return 1;

#  --cv::VideoCapture cap(video_source);
#  // Check if video device can be opened with the given index
#  if(!cap.isOpened()) return 1;
#  cv::Mat frame;
#  sensor_msgs::ImagePtr msg;

#  ros::Rate loop_rate(5);
#  while (nh.ok()) {
#    cap >> frame;
#    // Check if grabbed frame is actually full with some content
#    if(!frame.empty()) {
#      --msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", frame).toImageMsg();
#      pub.publish(msg);
#      cv::waitKey(1);
#    }

#    ros::spinOnce();
#    loop_rate.sleep();
#  }
#}
