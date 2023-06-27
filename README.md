
# Email Webcam Detection

This software basically detect whenever a person or an object comes in front of the camera and send an email to the user with the image of person or the object attached to the email.

- the efficiency of capturing the object in frame depends on quality of camera and lightning effects.

- It is made using the **Python** and **cv2** module which helps in using the webcame and capturing the object or a person in the frame.

- To use this software you have to first create an app in the google account and copy paste its password in the variables.py file.

- While running the software you have to hit and try your webcam slot in **cv.VideoCapture()** method with 0 to 4.

- Link to create the app in the google account [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

- To exit the software you have to press **q** key

- Make sure not to press the exit key instantly after capturing object because it takes around 4 to 5 seconds to send mail after capturing.




## Run Locally


Install cv2 module 

```bash
  pip install opencv-python
```

Run main.py

```bash
  python main.py
```


## Screenshots

![Screenshot1](https://github.com/AkramExp/email-webcam-detection/blob/main/screenshots/ss1.png)

