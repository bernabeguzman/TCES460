import numpy
import cv2
import urllib
import urllib2

print("Downloading Images and Necessary Files")
christiano = 'http://cdn.images.express.co.uk/img/dynamic/67/590x/cristiano-ronaldo-553153.jpg'
rawurl = 'http://raw.githubusercontent.com/Itseez/opencv/master/data/haarcascades/haarcascade_frontalface_alt.xml'

urllib.urlretrieve(christiano,
 '/usr/lib/edison_config_tools/public/DSC_0713_linkedin.jpg') 

urllib.urlretrieve(rawurl, 
'/usr/lib/edison_config_tools/public/haarcascade_frontalface_alt.xml')

#file = urllib2.urlopen(stephurl)
#data = file.read()
#with open("/usr/lib/edison_configure_tools/public/in.jpg", "wb") as code:
#	code.wirte(data)

#file = urllib2.urlopen(rawurl)
#data = file.read()
#with open("/usr/lib/edison_configure_tools/public/haarcascade_frontalface_alt.xml", "wb") as code:
#	code.wirte(data)

img = cv2.imread('/usr/lib/edison_config_tools/public/DSC_0713_linkedin.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier('/usr/lib/edison_config_tools/public/haarcascade_frontalface_alt.xml')
faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, 
minNeighbors=5, minSize = (30, 30), flags = cv2.cv.CV_HAAR_SCALE_IMAGE)

for(x, y, w, h) in faces:
	cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
	cv2.imwrite('in_facefound.png', img)

