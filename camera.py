import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import sqlite3
from PIL import Image
import string
import random
import uuid
from playsound import playsound
import smtplib

# Connecting to database

conn = sqlite3.connect("peopledata\db.sqlite3")
cursorObject = conn.cursor()
print("Database connection successful ")

# Create your SMTP(library) session

smtp = smtplib.SMTP('smtp.gmail.com', 587)

# Using TLS to add security

smtp.starttls()

# Authenticating admin email

smtp.login("sendemail2224@gmail.com", "admin123@")
print("Admin email authenticated")

# Defining The Message

message_one = "Criminal Face Detected"
message_two = "Unknown Face Detected"

# Accessing Known images

path = 'peopledata\media\knownimg'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    imgHeight = curImg.shape[0]
    imgWidth = curImg.shape[1]
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)
print("Known Image accessed")

# Accessing Criminal images

Cpath = 'peopledata\media\criminalimg'
Cimages = []
myCList = os.listdir(Cpath)
print(myCList)
for c in myCList:
    CcurImg = cv2.imread(f'{Cpath}/{c}')
    CimgHeight = CcurImg.shape[0]
    CimgWidth = CcurImg.shape[1]
    Cimages.append(CcurImg)
print("Criminal Image accessed")

# Finding face encodings for Known Images

def findEncodings(images):
    encodeList = []

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

# Finding face encodings for Criminal Images

def findCEncodings(Cimages):
    CencodeList = []

    for Cimg in Cimages:
        Cimg = cv2.cvtColor(Cimg, cv2.COLOR_BGR2RGB)
        Cencode = face_recognition.face_encodings(Cimg)[0]
        CencodeList.append(Cencode)
    return CencodeList


encodeListKnown = findEncodings(images)
print('Encoding Complete')

encodeListC = findCEncodings(Cimages)
print('Blacklist Encoding Complete')

print("Starting Webcam...")

# Initializing Web Cam

cap = cv2.VideoCapture(0)

# Setting Frame width and height

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1000)

count = 0
count_two = 0
count_three = 0
count_four = 0
i = 0


while True:
    if cap.isOpened():

        success, img = cap.read()
        if success:

            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            # Finding Face Encodings for Face detected by webcam

            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            # Comparing face detected by web cam with known faces

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(
                    encodeListKnown, encodeFace, tolerance=0.50)
                faceDis = face_recognition.face_distance(
                    encodeListKnown, encodeFace)
                matchIndex = np.argmin(faceDis)
                name = ''

                # Displaying Result if face matched with known face

                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()
                    if count_two < 1:
                        playsound(r'peopledata\Audio\Known.mp3')
                        playsound(r'peopledata\Audio\Entry.mp3')

                    fontScale = (imgWidth * imgHeight) / (1400*1100)
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    font = cv2.FONT_HERSHEY_SIMPLEX

                    # Building rectangle around the face in webcam video

                    cv2.rectangle(
                        img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2),
                                  (0, 255, 0), cv2.FILLED)

                    # Displaying Date and Time on the webcam video

                    cv2.putText(img, str(datetime.now()), (10, 30),
                                font, 1, (0, 255, 0), 2, cv2.LINE_AA)

                    # Displaying name on the webcam video

                    cv2.putText(img, name, (x1 + 6, y2 - 6),
                                font, fontScale, (255, 255, 255), 2)
                    count_two += 1

                # Displaying result if face matched with Criminal Face

                else:
                    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                        Cmatches = face_recognition.compare_faces(
                            encodeListC, encodeFace, tolerance=0.50)
                        CfaceDis = face_recognition.face_distance(
                            encodeListC, encodeFace)

                        CmatchIndex = np.argmin(CfaceDis)
                        if Cmatches[CmatchIndex]:
                            name = "Blacklisted"
                            if count_three < 1:
                                playsound(r'peopledata\Audio\Criminal.mp3')
                                playsound(r'peopledata\Audio\Deny.mp3')

                                # Sending the Email

                                smtp.sendmail(
                                    "sendemail2224@gmail.com", "getemail000@gmail.com", message_one)

                                # Terminating the session

                                smtp.quit()
                                print(
                                    "Email sent successfully! Check your inbox for more details")

                            fontScale = (imgWidth * imgHeight) / (1400*1100)
                            y1, x2, y2, x1 = faceLoc
                            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                            font = cv2.FONT_HERSHEY_SIMPLEX

                            # Building rectangle around the face in webcam video

                            cv2.rectangle(
                                img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                            cv2.rectangle(img, (x1, y2 - 35), (x2, y2),
                                          (0, 255, 0), cv2.FILLED)

                            # Displaying Date and Time on the webcam video

                            cv2.putText(img, str(datetime.now()), (10, 30),
                                        font, 1, (0, 255, 0), 2, cv2.LINE_AA)

                            # Displaying name on the webcam video

                            cv2.putText(img, name, (x1 + 6, y2 - 6),
                                        font, fontScale, (255, 255, 255), 2)
                            count_three += 1

                        # Displaying result if face matched with neither

                        else:
                            name = "Unknown"
                            if count_four < 1:
                                playsound(r'peopledata\Audio\Unkwn.mp3')
                                playsound(r'peopledata\Audio\Option.mp3')

                                # Sending the Email

                                smtp.sendmail(
                                    "sendemail2224@gmail.com", "getemail000@gmail.com", message_two)

                                # Terminating the session

                                smtp.quit()
                                print(
                                    "Email sent successfully! Check your inbox for more details")

                            fontScale = (imgWidth * imgHeight) / (1400*1100)
                            y1, x2, y2, x1 = faceLoc
                            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                            font = cv2.FONT_HERSHEY_SIMPLEX

                            # Building rectangle around the face in webcam video

                            cv2.rectangle(
                                img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                            cv2.rectangle(img, (x1, y2 - 35), (x2, y2),
                                          (0, 255, 0), cv2.FILLED)

                            # Displaying Date and Time on the webcam video

                            cv2.putText(img, str(datetime.now().replace(microsecond=0)), (10, 30),
                                        font, 1, (0, 255, 0), 2, cv2.LINE_AA)

                            # Displaying name on the webcam video

                            cv2.putText(img, name, (x1 + 6, y2 - 6),
                                        font, fontScale, (255, 255, 255), 2)

                            # Cropping face from the webcam video

                            sub_face = img[y1:y2-35, x1:x2-6]
                            if count < 1:
                                FaceFileName = name + ".jpg"
                                cv2.imwrite(FaceFileName, sub_face)
                                im = open(FaceFileName, 'rb').read()

                                # Assigning id values to the unknown images before sending them to database

                                x = str(uuid.uuid4().int)[:5]

                                # Sending the face to unknown images database

                                cursorObject.execute("INSERT INTO unknowns VALUES(?, ?) ", (x,
                                                                                            sqlite3.Binary(im)))

                                print("Added to database")

                                conn.commit()

                                # Fetching the faces from unknown images database and saving them to local directory

                                # Generating random unique ids for unknown images

                                def id_generator(size=20, chars=string.ascii_lowercase + string.digits + string.ascii_uppercase):
                                    return ''.join(random.choice(chars) for _ in range(size))

                                def writeTofile(data, filename):

                                    # Converting binary data to proper format and writing it on Hard Disk

                                    print("function execution start")
                                    with open(filename, 'wb') as file:
                                        file.write(data)
                                    print("Stored blob data into: ",
                                          filename, "\n")

                                print("added data to file")

                                def readBlobData():
                                    sql_fetch_blob_query = """SELECT * from unknowns where id = ?"""
                                    cursorObject.execute(
                                        sql_fetch_blob_query, [x])
                                    record = cursorObject.fetchall()

                                    for row in record:
                                        photo = row[1]

                                    photoPath = r"peopledata\media\unknownimg\\" + id_generator() + ".jpg"
                                    writeTofile(photo, photoPath)

                                readBlobData()
                                cursorObject.close()
                            count += 1
                            count_four += 1

            # Displaying webcam

            cv2.imshow("Webcam",   img)
            if cv2.waitKey(1) & 0xFF == ord('c'):
            # if cv2.getWindowProperty('image',cv2.WND_PROP_VISIBLE) < 1:
                break

print("Program execution completed")