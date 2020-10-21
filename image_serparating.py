from skimage import measure
import matplotlib.pyplot as plt
import numpy as np
import cv2
import PIL
from PIL import Image
import os
import shutil
import glob

if not os.path.exists("separated_Cenek_images"):
    os.makedirs("separated_Cenek_images")
count = 0
#filelist = glob.glob(os.path.join('new_different_frames/'))
for filename in sorted(os.listdir('new_different_frames')):
    print(filename)
    if not filename.startswith('.'):
        if count < 29:
            if not os.path.exists('separated_Cenek_images/plastic_bottles'):
                os.makedirs('separated_Cenek_images/plastic_bottles')
            
            shutil.copyfile('new_different_frames/' + str(filename), 'separated_Cenek_images/plastic_bottles/' + str(filename))
        elif count < 55:
            if not os.path.exists('separated_Cenek_images/metal_cans'):
                os.makedirs('separated_Cenek_images/metal_cans')
            
            shutil.copyfile('new_different_frames/' + str(filename), 'separated_Cenek_images/metal_cans/' + str(filename))
        elif count < 81:
            if not os.path.exists('separated_Cenek_images/cardboard'):
                os.makedirs('separated_Cenek_images/cardboard')
            shutil.copyfile('new_different_frames/' + str(filename), 'separated_Cenek_images/cardboard/' + str(filename))
        elif count < 108:
            if not os.path.exists('separated_Cenek_images/plastic_bags'):
                os.makedirs('separated_Cenek_images/plastic_bags')
            shutil.copyfile('new_different_frames/' + str(filename), 'separated_Cenek_images/plastic_bags/' + str(filename))
        elif count < 134:
            if not os.path.exists('separated_Cenek_images/shells'):
                os.makedirs('separated_Cenek_images/shells')
            shutil.copyfile('new_different_frames/' + str(filename), 'separated_Cenek_images/shells/' + str(filename))
        elif count < 168:
            if not os.path.exists('separated_Cenek_images/paper'):
                os.makedirs('separated_Cenek_images/paper')
            shutil.copyfile('new_different_frames/' + str(filename), 'separated_Cenek_images/paper/' + str(filename))
        elif count < 195:
            if not os.path.exists('separated_Cenek_images/cardboard_and_paper'):
                os.makedirs('separated_Cenek_images/cardboard_and_paper')
            shutil.copyfile('new_different_frames/' + str(filename), 'separated_Cenek_images/cardboard_and_paper/' + str(filename))
        else:
            if not os.path.exists('separated_Cenek_images/assorted'):
                os.makedirs('separated_Cenek_images/assorted')
            shutil.copyfile('new_different_frames/' + str(filename), 'separated_Cenek_images/assorted/' + str(filename))
    count+=1
            