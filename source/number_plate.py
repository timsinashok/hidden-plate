
# Import necessary libraries
import numpy as np
import cv2
from IPython.display import Image
from matplotlib import pyplot as plt
from ultralytics import YOLO

import os


## Downloading the data using roboflow
#from roboflow import Roboflow
#rf = Roboflow(api_key="JemAXJ2X7SOptsVPKxrG")
#project = rf.workspace("kanwal-masroor-gv4jr").project("yolov7-license-plate-detection")
#dataset = project.version(3).download("yolov8")


from ultralytics import YOLO

print("Here")

# Load a pretrained YOLO model (recommended for training)
model = YOLO('yolov8n.pt')

# Train the model using the 'coco128.yaml' dataset for 3 epochs
results = model.train(data='/scratch/at5282/plate/yolov7-license-plate-detection-3/data.yaml', epochs=50)

# Evaluate the model's performance on the validation set
results = model.val()

# Export the model to ONNX format
success = model.export(format='onnx')
