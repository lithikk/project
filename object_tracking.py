import cv2
import time
import math
p1=530
p2=300

xarray=[]
yarray=[]
video = cv2.VideoCapture("C:/Users/santh/Downloads/PRO-C107-Teacher-Boilerplate-main/PRO-C107-Teacher-Boilerplate-main/bb3.mp4")
#loaded the algorithm
tracker=cv2.TrackerCSRT_create()

# Read the first frame of the video
returned,img=video.read()
bbox=cv2.selectROI("tracking",img,False)
tracker.init(img,bbox)

def drawbox(img,bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img,"tracking",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)


def goal_track(img,bbox):
     x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
     
     c1=x+int(w/2)
     c2=y+int(h/2)
     cv2.circle(img,(c1,c2),2,(0,0,255),5)
     cv2.circle(img,(int(p1),int(p2)),2,(0,0,255),5)

     dist = math.sqrt(((c1-p1)**2) + (c2-p2)**2)
     if dist<=20:
        cv2.putText(img,"goal",(300,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

     xarray.append(c1)
     yarray.append(c2)
     for i in range(len(xarray)-1):
         cv2.circle(img,(xarray[i],yarray[i]),2,(0,0,255),5)
         





while True:
    check,img = video.read()   
    success,bbox=tracker.update(img)
    if success:
        drawbox(img,bbox)
    else:
        
        cv2.putText(img,"Lost",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    goal_track(img,bbox)
    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break


video.release()
cv2.destroyALLwindows()




