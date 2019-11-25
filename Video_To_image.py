import os
import cv2
import shutil
import math
import re
# Let us print the  present working directory (PWD)
PWD = os.getcwd()

# *****************************************************************************************************************
#                Let us create the files using r, d and f where  r=root, d=directories, f = files
# *************************************************************************************************************
for r, d, f in os.walk(PWD):
    for file in f:
        if ".mp4" in file:
#  **************************************************************************************************************
#                Creating the image folder without mp4 extension and with camera name
# ***************************************************************************************************************
            image_folder = "CAM_F" + "_" + re.sub('.mp4', "", file)
            # create folders from obtained files name
            os.makedirs(image_folder)
            # Creating source and destination in order to move file to destination
            image_source = PWD
            file_source = image_source + "/" + file
            resulted_image = image_source+ "/" + image_folder
            # Moving file from PWD( present working directory) the place our image must be stored
            shutil.move(file_source, resulted_image)

# *******************************************************************************************************************
            # Adding videos to the created folders
# *******************************************************************************************************************
            videoFile = image_folder + '/' + file

            camera_F = cv2.VideoCapture(videoFile)
            frameRate = camera_F.get(5)  # frame rate
            x = 1
# *********************************************************************************************************************
#            Creating a function with while loop
# *********************************************************************************************************************
            while (camera_F.isOpened()):
                frameId = camera_F.get(1)  # to get one image per second
                ret, frame = camera_F.read()
                if (ret != True):
                    break
                if (frameId % math.floor(frameRate) == 0):
                    filename = './' + image_folder + '/' + image_folder + '' + str(int(x)) + ".png";
                    x += 1
                    cv2.imwrite(filename, frame)  # saving the images
            camera_F.release()
        print(" Converting the video folder" + " " + image_folder + " " + "is Done!")

        # Creating variables of video to be deleted
        delete_Video = resulted_image + "/" + file
        # deleting video into image files
        delete_Video = os.remove(delete_Video)
