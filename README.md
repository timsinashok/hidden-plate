# Hidden Plate

Hidden Plate is a program designed to obscure the number plates of vehicles in images of cars. It serves as a tool for online car dealerships to maintain privacy and minimize the risks associated with uploading vehicle images containing license plate information to the internet.

## Program Description

The program is trained on the annotated data downloaded from the roboflow. The dataset is present <a href = "https://universe.roboflow.com/kanwal-masroor-gv4jr/yolov7-license-plate-detection">here. </a> The program utilizes YOLOv8 for image processing for detecting number plates in the image and uses computer vision to obscure number plates in vehicle images. This ensures that sensitive information is protected before images are uploaded to online platforms.

## Program Demonstration

### Original Image
<img src="Images/car.jpeg" alt="Original Image" width="400"/>

### Modified Image
<img src="Images/modified_image.jpg" alt="Modified Image" width="400"/>

## Usage

This model can be easily used by cloning the repository and changing the path of the input file in the script <a href="source/hide_test.py">hide_test.py</a>. Alongside that you will have to install the requirements present at <a href="requirements.txt"> requirements.txt</a>. 

## Conclusion

The program effectively conceals the number plate of vehicles in images, ensuring privacy while maintaining the visual integrity of the vehicle. Ongoing development efforts are focused on improving the program's capabilities, especially in scenarios where the number plate is not a complete rectangle.


## References:

- <a href="https://docs.ultralytics.com/usage/python/#val"> YOLO v8 Documentation on Ultralytics </a> 
- <a href="https://universe.roboflow.com/kanwal-masroor-gv4jr/yolov7-license-plate-detection"> Roboflow Annotated Dataset on License Plate</a>
