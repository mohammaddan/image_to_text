import numpy as np
import cv2
import matplotlib.pyplot as plt
# from termcolor import colored

img = cv2.imread('/home/md/Pictures/myself2.jpg',0)
contrast=150
alpha = 1.2 # Contrast control (1.0-3.0)
beta = 20 # Brightness control (0-100)
myname='mohammad_daneshamooz_'
img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
# Convert to graycsale

# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
# img_blur = cv2.GaussianBlur(img, (3,3), 0) 
# sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
# sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
# img = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
# img = cv2.Canny(image=img, threshold1=5, threshold2=100)

rStep=len(img)//29
cStep=len(img[0])//58

# ri=0
for ri in range(0,len(img),rStep):
    # ri+=1
    # ci=0
    # if ri%14!=0:
        # continue
    for ci in range(0,len(img[ri]),cStep): 
        # ci+=1
        # if ci%7!=0:
            # continue
        # if img[ri-1][ci-1]>contrast and ri<len(img)-1 and img[ri][ci-1]>contrast:
        #     print('*',end='')
        # elif img[ri-1][ci-1]>contrast and ri<len(img)-1 and img[ri][ci-1]<contrast:
        #     print('\'',end='')
        # elif img[ri-1][ci-1]<contrast and ri<len(img)-1 and img[ri][ci-1]>contrast:
        #     print('.',end='')
        if img[ri][ci]>contrast:
            # print(colored(myname[(ci//7+ri)%len(myname)],'cyan' if c>240 else 'grey'),end='')
            print(myname[(ci//cStep+ri)%len(myname)],end='')
        else:
            print(' ',end='')
    print('')
        
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()