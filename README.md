# Face_Recognition&Attendance-project
**OBJECTIVE:**
To make the attendance marking and management system efficient, time saving and simple. Instead of using conventional systems, this method develops an automated system that records attendees' attendance.
-----------------------
In this, Face-Recognition and Attendance Project, language used is Python with cmake, dlib, OpenCV, NumPy libraries. Face-Recognition deals with detecting faces and distance of the facial characters. OpenCV library in Python, uses machine learning algorithms to search for faces within a picture.
NumPy is used to convert images into array which stores the model which has been trained.
Here, two images(original image and test image) when passed, checks if they are of the same person and returns true if so. But if not, it returns false.
![Screenshot (2)](https://user-images.githubusercontent.com/78093967/170690258-a9e0f7a0-2712-4760-b3f3-6fdbf4c089d0.png)
In attendance project, firstly, images of the attendees are passed then encodings of the images are found out by findEncodings() function. ![Screenshot (3)](https://user-images.githubusercontent.com/78093967/170699136-5699d1af-f417-485d-a2ae-7dd4e3d7cac4.png)


By accessing webcam, images are examined and marked through markAttendnace() and their attendance is marked in a .csv file by opening that file in read and write mode simultaneously. 
![Screenshot (4)](https://user-images.githubusercontent.com/78093967/170699329-a96fc353-89a6-4f1a-8f27-67e4e0f5c32f.png)
Then, the names of attendees and their time are noted in att.csv file through which the data(Name and Time) could be accesssible in form of excel sheets.![Screenshot (6)](https://user-images.githubusercontent.com/78093967/170712505-5ca94522-2f58-4f04-a5e5-9f6aa5b1a8a1.png)

![Screenshot (5)](https://user-images.githubusercontent.com/78093967/170699549-2af94d49-a2e4-47e2-91b9-b9b7754dca2e.png)
