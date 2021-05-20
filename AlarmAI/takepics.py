import cv2
import os
import time
# Get the current working directory
cwd = os.getcwd()


#creates an object called camera, of type openCV video capture, using the first camera in the list of cameras connected to the computer.
def takepic():
    camera = cv2.VideoCapture(0)
    for i in range(30):
    #tells the program to loop the following indented code 10 times

        return_value, image = camera.read()
    #read values from the camera object, using it's read method. it resonds with 2 values save the 2 data values into two temporary variables called "return_value" and "image"
        print(cwd + '\Data\\opencv' + str(i) + '.png')
        cv2.imwrite(cwd + '\Data\\opencv'+str(i)+'.png', image)
        time.sleep(300)

    del(camera)


cv2.waitKey(0)
cv2.destroyAllWindows()
