
import os
import sys
import cv2 as cv
import numpy as np

def Histogram_Computation(Image):

    Image_Height = Image.shape[0]
    Image_Width = Image.shape[1]
    Image_Channels = Image.shape[2]

    Histogram = np.zeros(768, np.int32)

    for x in range (0, Image_Height):
        for y in range (0, Image_Width):
            for c in range(0, Image_Channels):
                Histogram[c*256 + Image[x,y,c]] += 1.0
    Histogram = np.true_divide(Histogram, float(Image_Height * Image_Width))


    
    return Histogram

def main():
    print("run")
    for filename in os.listdir('HW2_AuroraImages/test'):
        Input_Image = cv.imread('HW2_AuroraImages/test/' + str(filename))
        print(str(filename))
        if filename.startswith('.'):
            continue
        Histogram = Histogram_Computation(Input_Image)
        
        original_stdout=sys.stdout
        print(str(Histogram))
        with open('HW2_AuroraImages/aurelia_histograms/histograms8.txt', 'a') as f:
            sys.stdout = f
            print('1', end = ' ')
            for c in Histogram.tolist():
                print(str(c), end=' ')
            print('HW2_AuroraImages/test_images_2_take_2/' + str(filename))
            sys.stdout = original_stdout
    """
    for filename in os.listdir('HW2_AuroraImages/test_images_take_2'):
        Input_Image = cv.imread('HW2_AuroraImages/test_images_take_2/' + str(filename))
        if filename.startswith('.'):
            continue
        Histogram = Histogram_Computation(Input_Image)
        
        original_stdout=sys.stdout
        with open('HW2_AuroraImages/aurelia_histograms/histograms7.txt', 'a') as f:
            sys.stdout = f
            print('-1', end = ' ')
            for c in Histogram.tolist():
                print(str(c), end=' ')
            print('HW2_AuroraImages/test_images_take_2/' + str(filename))
            sys.stdout = original_stdout
    """

    """
    for filename in os.listdir('HW2_AuroraImages/not_known_copy'):
        Input_Image = cv.imread('HW2_AuroraImages/not_known_copy/' + str(filename))
        Histogram = Histogram_Computation(Input_Image)
        
        original_stdout=sys.stdout
        with open('HW2_AuroraImages/aurelia_histograms/histograms5.txt', 'a') as f:
            sys.stdout = f
            print('0', end = ' ')
            for c in Histogram.tolist():
                print(str(c), end=' ')
            print('HW2_AuroraImages/not_known_copy/' + str(filename))
            sys.stdout = original_stdout
    """
    

if __name__ == "__main__":
    main()
