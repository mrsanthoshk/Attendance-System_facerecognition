import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://sandyface-804db-default-rtdb.firebaseio.com/",  # My URl link to the database to get connect
    'storageBucket': "sandyface-804db.appspot.com"  # For the storage path in the database # to store the images 
})

# Importing students images
folderPath = 'Images'
pathList = os.listdir(folderPath)
imgList = []
studentIds = []
for path in pathList:
    # get the whole file names
    imgList.append(cv2.imread(os.path.join(folderPath, path)))

    # get only the name of the file without the extension
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

# print(len(imgList))
# print(studentIds)
 

 
# Get encodings format from all images
def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        # convert BGR to RGB: OpenCV -> BGR, Computer Vision -> RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
# print(encodeListKnownWithIds)

file = open("EncodeFile.p",'wb') # Need those data in the encode formate to for the work process
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File saved")