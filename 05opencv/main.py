import cv2
import os
import time
import numpy


cap = cv2.VideoCapture(0)
pTime = 0

while True:
      success, img = cap.read()
      imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
      cTime = time.time()
      fps = 1 // (cTime - pTime)

      pTime = cTime
      #cv2.face.createEigenFaceRecognizer()
      gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      #img=cv2.flip(img,1)
      cv2.putText(img, f'FPS:{int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

      cv2.imshow("Test", img)
      print(fps)
      if(cv2.waitKey(1) & 0xFF == ord('q')):
            cap.release()
            cv2.destroyAllWindows()

            break
