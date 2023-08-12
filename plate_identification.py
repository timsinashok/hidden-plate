import cv2

imagefile = "images/Cars101.png"
image = cv2.imread(imagefile)

window_name = 'Image Show'

cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()