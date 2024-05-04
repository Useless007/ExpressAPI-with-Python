# It helps in identifying the faces
import cv2, numpy, os, datetime, time, csv
# from PIL import Image
import pandas as panda 
from datetime import datetime
from time import localtime, strftime


# Define the CSV file name
csv_filename = "../ExpressAPIWithPython/python/data_with_timestamp.csv"

# Define the data to be written to the CSV file



dataFrame = panda.DataFrame(columns = ["Initial", "Final"])
size = 4
haar_file = '../ExpressAPIWithPython/python/haarcascade_frontalface_default.xml'
datasets = '../ExpressAPIWithPython/python/datasets'
stamp = False
running = True

# Part 1: Create fisherRecognizer
print('Recognizing Face Please Be in sufficient Lights...')

# Create a list of images and a list of corresponding names
(images, labels, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(datasets):
	for subdir in dirs:
		names[id] = subdir
		subjectpath = os.path.join(datasets, subdir)
		for filename in os.listdir(subjectpath):
			path = subjectpath + '/' + filename
			label = id
			images.append(cv2.imread(path, 0))
			labels.append(int(label))
		id += 1
(width, height) = (130, 100)

# Create a Numpy array from the two lists above
(images, labels) = [numpy.array(lis) for lis in [images, labels]]

# OpenCV trains a model from the images
# NOTE FOR OpenCV2: remove '.face'
model = cv2.face.LBPHFaceRecognizer_create()

model.train(images, labels)

# Part 2: Use fisherRecognizer on camera stream
face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0) # ตรงนี้ใช้กล้องIPได้ "rstp://"
while running == True:
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    check, frame = webcam.read()  
    result, image = webcam.read()
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        # Try to recognize the face
        prediction = model.predict(face_resize)
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
        
        cv2.putText(im, '% s - %.0f' % 
            (names[prediction[0]], prediction[1]), (x-10, y-10), 
        cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))           
             
        frame_width = int(webcam.get(3))
        frame_height = int(webcam.get(4))



        
  
        if prediction[1]<500:
            
           
            cv2.putText(im, '% s - %.0f' % 
            (names[prediction[0]], prediction[1]), (x-10, y-10), 
            cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
            

            
            if prediction[1]>60:
                              
                new_data = [[(names[prediction[0]]), None]]
                file2 = cv2.imwrite('../ExpressAPIWithPython/python/CAM01.jpg', image) 
                
                
                         
            # Add timestamps to the new data
                while stamp == False:
                    for row in new_data:
                        row[1] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Adding current timestamp
                    with open(csv_filename, mode="a", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(new_data)

                        for i in range(1):
                            
                            #line
                            
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
                            cv2.putText(im, '% s - %.0f' % 
                                (names[prediction[0]], prediction[1]), (x-10, y-10), 
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))  
                            i += 1
                            stamp = True
                            if prediction[1]>80:   
                                times = time.time()
                break
            
         
      

        else:
            cv2.putText(im, 'not recognized', 
            (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))

         
        
  
    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(5)
    # running = False
    
    if stamp == True:
        break
    
    if (key == 27):
        running = False
        webcam.release()
        cv2.destroyAllWindows()
    
webcam.release()
cv2.destroyAllWindows() 
exit()
    
    # if key == 27:
    #     break
    