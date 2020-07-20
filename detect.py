import cv2
import sys
import os.path

def detect(abs_filename, cascade_file = "../lbpcascade_animeface.xml"):#, mode="display"):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread(abs_filename, cv2.IMREAD_COLOR)
    height, width, channels = image.shape
    #image = image[0: int(h/2), 0: w]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    
    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor = 1.01,
                                     minNeighbors = 5,
                                     minSize = (250, 250)
                                     #,maxSize = (int(0.4*w), int(0.4*h))
                                     #too inclusive ... i.e. it appears to be OR-ing the condition, not AND-ing.
                                     )
    '''
    Don't overwrite images accidentally! non unique abs_filename for multi crops...
    '''
    tag = 0
    filename = os.path.basename(abs_filename)
    for (x, y, w, h) in faces:
        if h > height * 0.5:
            continue

        #cv2.rectangle(image, (int(x*0.85), int(y*0.1)), (x + int(w*1.5), y + h), (255, 0, 0), 50)
        cropped = image[int(y*0.1): y + h, int(x*0.85): x + int(w*1.5)]
        #cv2.imshow("AnimeFaceDetect", image)
        #cv2.waitKey(0)
        cv2.imwrite(str(filename[0:-4] + '_' + str(tag) + filename[-4:]), cropped)
        tag += 1

    print(tag)

if len(sys.argv) != 2:
    sys.stderr.write("usage: detect.py <abs_filename>\n")
    sys.exit(-1)
detect(sys.argv[1])
