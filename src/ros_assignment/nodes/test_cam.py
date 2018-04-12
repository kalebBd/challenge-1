import numpy as np
import cv2
from time import gmtime, strftime
#function to display the gray image
def showGray(name,formate):
    img = cv2.imread( name+formate ,0)
    #cv2.namedWindow('image', cv2.WINDOW_NORMAL)#if cv2.WINDOW_NORMAL it is resizable, else default cv2.WINDOW_AUTOSIZE
    #cv2.imshow('image',img)
    keypressed = cv2.waitKey(0)
    if keypressed == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif keypressed == ord('s'): # wait for 's' key to save and exit
        name = name + '_gray'
        cv2.imwrite(name+'.png',img)
        print 'Saved image as grayscale with name ' + name + '.png'
        cv2.destroyAllWindows()
    del( img )
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
            print 'Saved image as ' + name + '.png'
            #cv2.destroyAllWindows()
        camera.release()
    else:
        print 'Error saving image'
    del(camera)
    return name

#main function
if __name__ == '__main__':
    showGray(captureImage(),'.png')
