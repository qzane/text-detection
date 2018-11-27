# text detection
very simple text detection using opencv and python <br>
也可以用于中文！ <br>
심지어 한국 <br>

# usage
``` bash
python TextDetect.py input.png
```

# requirements
* Python > 3.0 (Tested with: 3.4.3)
* Opencv > 3.0 (Tested with: 3.0.0)

# what to do when the result is not good
Try to change the ele_size for text_detect, smaller value results in a more sensitive detector in corresponding direction

# results

![original image](/test_detection.png) ![tests](/test_detection-rect.png)

# see also
* http://stackoverflow.com/a/23565051
* http://docs.opencv.org/master/da/d56/group__text__detect.html#gsc.tab=0

# license
BSD 3-Clause licensed. See the bundled LICENSE file for more details.
