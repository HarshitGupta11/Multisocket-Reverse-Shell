import numpy as np
import cv2
import sys
import time

t=sys.argv
t=int(t[-1])

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.avi',fourcc, 25.0, (1280,720))

st=time.time()
#print(st)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True and time.time()-st<t:
        #frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        #cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()