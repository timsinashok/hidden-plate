from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import cv2
import io
import numpy as np

app = FastAPI()

@app.post("/process_image/")
async def process_image(file: UploadFile):
    try:
        if not file.content_type.startswith("image/"):
            return {"error": "Invalid file format. Please provide an image."}

        contents = await file.read()

        # Read the image using OpenCV
        img = cv2.imdecode(np.fromstring(contents, np.uint8), cv2.IMREAD_COLOR)

        # Perform image processing here (e.g., apply filters, resize, etc.)
        # For example, you can convert the image to grayscale
        processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Encode the processed image to bytes
        _, img_encoded = cv2.imencode(".jpg", processed_img)
        img_bytes = img_encoded.tobytes()

        # Convert image bytes to a file-like object
        img_io = io.BytesIO(img_bytes)

        return FileResponse(io.BytesIO(img_bytes), media_type="image/jpeg")
    except Exception as e:
        return {"error": str(e)}
    

def hide_plate(image_file):
    img = cv2.imread(image_file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bfilter = cv2.bilateralFilter(gray, 11, 17, 17) #Noise reduction
    edged = cv2.Canny(bfilter, 40, 200) #Edge detection

    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    location = None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = approx
            break

    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [location], 0,255, -1)
    new_image = cv2.bitwise_and(img, img, mask=mask)




