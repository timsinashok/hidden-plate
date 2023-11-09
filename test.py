import cv2

# Load the image
image = cv2.imread('Images/Cars250.png')

# Apply car detection to find car bounding boxes
car_cascade = cv2.CascadeClassifier('car_cascade.xml')
cars = car_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)

# Iterate through detected cars
for (x, y, w, h) in cars:
    # Define a region of interest (ROI) around the car
    roi = image[y:y+h, x:x+w]

    # Apply license plate localization within the ROI
    # You can use edge detection, contour analysis, etc.

    # Extract coordinates of the license plate
    plate_x = x  # X-coordinate of the license plate
    plate_y = y  # Y-coordinate of the license plate
    plate_width = w  # Width of the license plate
    plate_height = h  # Height of the license plate

    # Draw a bounding box around the license plate
    cv2.rectangle(image, (plate_x, plate_y), (plate_x + plate_width, plate_y + plate_height), (0, 255, 0), 2)

# Display or save the image with the license plate bounding box
cv2.imshow('License Plate Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()