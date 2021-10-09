import cv2
import sys

# Importing the haarcascade xml file
cascPath =("haarcascade_frontalface_default.xml")

# Get user supplied values
imagePath=input("input path: ")
type(imagePath)

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
 gray,
 scaleFactor=1.1,
 minNeighbors=5,
 minSize=(1, 1)
)

# printing the number of faces found
print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
# Saving the images that are detected
i=1
for (x, y, w, h) in faces:
 cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
 f = image[y:y+h, x:x+w]
 cv2.imwrite("f"+str(i)+".jpg", f)
 i+=1

# Showing the image with the face detected
cv2.imshow("Faces found", image)
cv2.waitKey(0)