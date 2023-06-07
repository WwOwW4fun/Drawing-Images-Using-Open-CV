
# coding: utf-8

# In[17]:


import cv2
import numpy as np
def draw(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(pic,(x,y),40,(200,200,0),-1)
    elif(event == cv2.EVENT_RBUTTONDOWN):
        cv2.circle(pic,(x,y),40,(0,200,200),-1)
cv2.namedWindow(winname = 'Draw')

cv2.setMouseCallback('Draw',draw)
pic = np.ones((500,500,3),dtype = np.int8)
while True:
    
    cv2.imshow('Draw',pic)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

