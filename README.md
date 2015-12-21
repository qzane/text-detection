# text-detection
text detection using opencv and python

# usage
``` python
img = cv2.imread('img-in.png')
rect = text_detect(img)
for i in rect:
    cv2.rectangle(img,i[:2],i[2:],(0,255,0))
cv2.imwrite('img-out.png')
```

# requirements
* Python > 3.0 (Tested with: 3.4.3)
* Opencv > 3.0 (Tested with: 3.0.0)

# see also
* http://stackoverflow.com/a/23565051
* http://docs.opencv.org/master/da/d56/group__text__detect.html#gsc.tab=0
