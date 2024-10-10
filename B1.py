import shutil
import os
# Define paths
input_image_path = '1.jpg'
esrgan_input_folder = "Real-ESRGAN/inputs"

# Move the input image to the ESRGAN input folder
shutil.move(input_image_path, esrgan_input_folder)

# Now the input image is in the ESRGAN input folder, you can run the ESRGAN model
# Add your code to run the ESRGAN model here
import subprocess

# Change directory to the ESRGAN folder
esrgan_folder = 'Real-ESRGAN'
os.chdir(esrgan_folder)

# Run the main.py file
subprocess.run(['python', 'main.py'])

import os
from PIL import Image
os.chdir("C:/Users/takhiuddin/FINAL_PROJECT")
# Define paths
input_folder = "Real-ESRGAN/results"  # Path to the folder containing the enhanced images

output_folder = 'resized_img'  # Path to the folder where resized images will be saved

# Iterate over each file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.png') or filename.endswith('.jpg'):
        # Open the image
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)

        # Resize the image to 640x640
        resized_image = image.resize((640, 640))

        # Save the resized image to the output folder
        output_path = os.path.join(output_folder, filename)
        resized_image.save(output_path)

print('All images resized and saved to', output_folder)

import shutil
import os

# Source folder containing the images
source_folder = "resized_img"

# Destination folder where the images will be moved
destination_folder = "YOLOV8_BRAIN-\YOLOV8_BRAIN\YOLO_UZ\F_inp"

# Iterate over the files in the source folder
for file_name in os.listdir(source_folder):
    if file_name.endswith('.jpg') or file_name.endswith('.png'):
        # Create the full path for the source file
        source_file = os.path.join(source_folder, file_name)
        # Create the full path for the destination file
        destination_file = os.path.join(destination_folder, file_name)
        # Move the file from the source to the destination folder
        shutil.move(source_file, destination_file)

print("Images moved successfully to", destination_folder)





