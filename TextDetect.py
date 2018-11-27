import os,sys
import numpy as np
import cv2

# author: qzane@live.com
# reference: http://stackoverflow.com/a/23565051
# further reading: http://docs.opencv.org/master/da/d56/group__text__detect.html#gsc.tab=0
def text_detect(img,ele_size=(8,2)): #
    if len(img.shape)==3:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_sobel = cv2.Sobel(img,cv2.CV_8U,1,0)#same as default,None,3,1,0,cv2.BORDER_DEFAULT)
    img_threshold = cv2.threshold(img_sobel,0,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY)
    element = cv2.getStructuringElement(cv2.MORPH_RECT,ele_size)
    img_threshold = cv2.morphologyEx(img_threshold[1],cv2.MORPH_CLOSE,element)
    contours = cv2.findContours(img_threshold,0,1)
    Rect = [cv2.boundingRect(i) for i in contours[1] if i.shape[0]>100]
    RectP = [(int(i[0]-i[2]*0.08),int(i[1]-i[3]*0.08),int(i[0]+i[2]*1.1),int(i[1]+i[3]*1.1)) for i in Rect]
    return RectP


def main(inputFile):
    outputFile = inputFile.split('.')[0]+'-rect.'+'.'.join(inputFile.split('.')[1:])
    print(outputFile)
    img = cv2.imread(inputFile)
    rect = text_detect(img)
    for i in rect:
        cv2.rectangle(img,i[:2],i[2:],(0,0,255))
    cv2.imwrite(outputFile, img)

if __name__ == '__main__':
    main(sys.argv[1])
