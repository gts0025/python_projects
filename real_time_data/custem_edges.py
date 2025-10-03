
#simple edge detection project,

import cv2,numpy as np
def edges(image):
    gray = (
        image[:,:,0]+
        image[:,:,1]+
        image[:,:,2]
    )/3
    edges = np.sqrt(
        (gray[2:,1:-1]-gray[:-2,1:-1])**2+
        (gray[1:-1,2:]-gray[1:-1,:-2])**2
    )
    gray[:,:] = 0
    gray[1:-1,1:-1] = (edges>50)*200
    return gray

cap  = cv2.VideoCapture(0)

while True:
    working,image = cap.read()
    image = image[:,::-1]
    #image = edges(image)
    cv2.imshow("some_image",cv2.Canny(image,50,50))
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
