
# coding: utf-8

# In[15]:


import cv2
import numpy as np
tempx = tempy = -1
drawing = False
tempx1 = tempy1 = -1
drawing1 = False
def draw(event,x,y,flags,params) : 
    global tempx, tempy, drawing
    global tempx1, tempy1,drawing1
    if event == cv2.EVENT_LBUTTONDOWN : 
        drawing = True
        tempx = x 
        tempy = y
    elif event == cv2.EVENT_MOUSEMOVE and drawing == True:
        cv2.rectangle(img,(tempx,tempy),(x,y),(200,200,100),-1)
    elif event == cv2.EVENT_LBUTTONUP : 
        drawing = False
    if event == cv2.EVENT_RBUTTONDOWN : 
        drawing1 = True
        tempx1 = x 
        tempy1 = y
    elif event == cv2.EVENT_MOUSEMOVE and drawing1 == True:
        cv2.rectangle(img,(tempx1,tempy1),(x,y),(0,100,230),-1)
    elif event == cv2.EVENT_RBUTTONUP : 
        drawing1 = False
        
cv2.namedWindow(winname = 'Draw')
cv2.setMouseCallback('Draw',draw)
img = np.zeros((512,512,3))
while True : 
    cv2.imshow('Draw',img)
    if cv2.waitKey(3) & 0xFF == 27 : 
        break
cv2.destroyAllWindows()

