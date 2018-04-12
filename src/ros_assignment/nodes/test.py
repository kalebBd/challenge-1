import numpy as np
import cv2

# Load an color image in grayscale
name = 'my'
formate = '.jpg'
def showGray(name,formate):
    img = cv2.imread( name+formate ,0)#1 for colored and 0 for grayscale
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)#if cv2.WINDOW_NORMAL it is resizable, else default cv2.WINDOW_AUTOSIZE
    cv2.imshow('image',img)
    keypressed = cv2.waitKey(0)
    if keypressed == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif keypressed == ord('s'): # wait for 's' key to save and exit
        name = name + '_gray'
        cv2.imwrite(name+'.png',img)
        print 'Saved image as ' + name
        cv2.destroyAllWindows()
#IplImage *input #pointer to image(works for cpp)
#input = cv2.LoadImage('my.jpg',1)#Loads image. 1 for colored and 0 for grayscale
#cv2.namedWindow ('window', 1)#creates a window
#cv2.imshow('window', input)#To display the loaded image
#cv2.waitKey(0)#if number<=0,indefinetly if number > 0 number in milisec
#cv2.destroyWindow( 'window' )#Destroys window
#cv2.releaseImage( &input )#releases memory for image
