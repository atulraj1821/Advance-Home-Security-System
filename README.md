# Microsoft engage 2022https
Link to my documentation : https://docs.google.com/document/d/1Tsx2JXMnV_Uu1zxZz5_OaWxGW7b-vShPe79-YUgTcZI/edit?usp=sharing

Overview of the project:
My idea here is to develop an advanced home security system that uses face recognition. 
Below is a step-by-step approach that I've formulated:
The flow of the whole project is divided into two parts:

Part-one: Face detection flow

Requirement: Face detection system installed at house door.

-The person wanting to enter the house will have to access the system.

-The camera present in the system will detect the person’s face.

-After detecting the face the system will go through a three step procedure.

    Step-one: The system will first match the detected face with the face dataset present in the known faces database.

        -If match is found: The system will allow the person to enter.

        -If match is not found: The system will move on to the next step.

    Step-two: The system will then match the detected face with the face dataset present in the criminal faces database.

        -If match is found: The system will deny entry to the person.

        -If match is not found: The system will move onto the third step.

    Step-three: If the program reaches this step that means the image is matched with neither of the datasets, the image will be treated as an unknown image.

    If the image gets tagged as unknown then the face will be cropped from the webcam image and it will be sent to the unknown database and a mail will be sent to the admin.

Part-two: Admin flow

    -After the completion of the face detection algorithm, the admin can manage the results through the admin panel provided.

    -Once the admin accesses the homepage of the application, he is provided with four options in form of buttons:

        -Admin panel: for accessing the admin panel and make changes in the database.

        -Known images: to view the known images present

        -Criminal images: to view the criminal images present

        -Unknown images: to view the unknown images present

    -The admin also gets the option to view and edit the databases(known, criminal, unknown) from the admin panel.

Credentials:

Django admin login:

Username : Admin

Password : 28012001

Dummy mail login to receive mail:

Email id : getemail000@gmail.com
Password : admin123@

Version of programming language used: 

(as used by me)
OpenCV: 4.5.5

Python: 3.9.5

Django: 4.0.4

HTML5

CSS3

How To Run and things to Install:

Prerequisites: 

-Python installed(version: 3.x.x) 

-IDE capable of executing python projects(VS Code preferable).

Things to install:

For Face Recognition: 

-OpenCV 

-Numpy

-Cmake

-Dlib

-Face Recognition Module

-Playsound Module

For Admin Panel:
-Django
-Django Rest Framework

How to Run:
Face Recognition System:

Steps: 
Command:
Cloning the Github Repository
git clone “url”
Accessing the cloned project through an IDE

Opening terminal inside “Dir_Name” and installing the required modules listed below:

OpenCV and Numpy

-pip install opencv-python

Upgrading pip(if needed) 

-pip install --upgrade pip

Cmake

-pip install cmake

Dlib

-pip install https://github.com/jloh02/dlib/releases/download/v19.22/dlib-19.22.99-cp310-cp310-win_amd64.whl

Face Recognition Module

-pip install face_recognition

Playsound Module(version: 1.2.2)

-pip install playsound==1.2.2


After the successful installation of the modules listed above:

Restarting the IDE(to apply the changes done)

Executing the Face Recognition File:

Opening the terminal inside the same directory

Running the command: python -u “camera.py”

Closing the Webcam window after successful execution of the program:

Pressing “c” on the keyboard


Admin Panel:

Shifting from “Dir_Name” directory to “peopledata” directory

In a fresh terminal window

Running the command: cd peopledata

Steps: 

After getting into “peopledata” directory,

installing the required modules listed below using the terminal:

Django

-pip install django

Django Rest Framework

-pip install djangorestframework


After the successful installation of the modules listed above:

Restarting the IDE(to apply the changes done)

Running the Admin Panel on local server:

In the terminal opened inside the same directory

Running the command: python manage.py runserver

After the successful execution of the above step the Admin panel will start running on port: 8000

Navigating to the Home page:

Clicking on the link given in terminal window

After accessing the home page the user can navigate to any of the pages they want to visit.



Requirement : 
-Port(local server) 8000 should not be preoccupied 

-One person at a time (so that the camera does not capture everyone appearing in the camera frame and also to improve accuracy of the algorithm)

Future scope:

-We can integrate this with IOT(Internet of Things) and create smart doors that can allow and deny entry automatically, thus improving the security .

-We can also link this system to android and ios devices in order to create an environment so that the user could get multi device support i.e the user could get notifications and access the facilities across multiple platforms.

-If a person with a criminal record or any unwanted person attempts entry an alert may also be sent to the local police station thereby helping the police to enhance security. 

-On a broader scale and adding more features this project may be implemented to integrate with NRC (National Register of Citizens ) to check infiltration and prevent cross border terrorism.

# Microsoft-Engage-2022-github
