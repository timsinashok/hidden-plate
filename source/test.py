from ultralytics import YOLO
import cv2
import imutils

# Load the YOLO model
model = YOLO("/scratch/at5282/plate/runs/detect/train5/weights/best.pt")

# Load the original image
original_image = cv2.imread("/scratch/at5282/plate/abc.jpeg")

# Load the replacement image
replacement_image = cv2.imread("/scratch/at5282/plate/ab.png")

# Predict on a single image
results = model.predict(source="/scratch/at5282/plate/abc.jpeg")

# Define a function for resizing images while preserving aspect ratio
def resize_image(image, width=None, height=None):
    if width is None and height is None:
        return image

    aspect_ratio = image.shape[1] / image.shape[0]

    if width is None:
        width = int(height * aspect_ratio)
    elif height is None:
        height = int(width / aspect_ratio)

    resized_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
    return resized_image

# Loop over the results
for result in results:
    # Access the bounding box coordinates in xyxy format
    for box in result.boxes.xyxy:
        # Convert the tensor to a list of coordinates
        box = box.tolist()
        x1, y1, x2, y2 = int(box[0]), int(box[1]), int(box[2]), int(box[3])
        
        # Calculate the width and height of the region of interest
        roi_width = x2 - x1
        roi_height = y2 - y1
        
        # Resize the replacement image to match the size of the region of interest
        resized_replacement = resize_image(replacement_image, roi_width, roi_height)

        # Replace the region within the bounding box in the original image with the resized replacement image
        original_image[y1:y2, x1:x2] = resized_replacement

# Save the modified image
output_path = "modified_image.jpg"
cv2.imwrite(output_path, original_image)
print(f"Modified image saved to {output_path}")
