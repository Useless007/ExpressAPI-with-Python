# Creating database
# It captures images and stores them in datasets
# folder under the folder name of sub_data
import cv2, sys, os
haar_file = '../ExpressAPIWithPython/python/haarcascade_frontalface_default.xml'

# All the faces data will be
# present this folder
datasets = '../ExpressAPIWithPython/python/datasets'
success = False
pictureframe = 60

# These are sub data sets of folder,
# for my faces I've used my name you can
# change the label here
sub_data = sys.argv[1]	

path = os.path.join(datasets, sub_data)
os.makedirs(path, exist_ok=True)
if not os.path.isdir(path):
	os.mkdir(path)

# defining the size of images
(width, height) = (130, 100)	

#'0' is used for my webcam,
# if you've any other camera
# attached use '1' like this
face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0) # ตรงนี้ใช้กล้องIPได้ "rstp://"

count = 1
while count <= pictureframe:
	(_, im) = webcam.read()
	gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 4)
	for (x, y, w, h) in faces:
		cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
		face = gray[y:y + h, x:x + w]
		face_resize = cv2.resize(face, (width, height))
		cv2.imwrite('% s/% s.png' % (path, count), face_resize)
		
	count += 1

	cv2.imshow('OpenCV', im)
	key = cv2.waitKey(10)

	if count == pictureframe:
		success = True
		print("The user " + sub_data + " was add to the python datasets.")

	if key == 27:
		break
