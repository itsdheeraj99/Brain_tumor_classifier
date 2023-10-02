# Brain Tumor Classification
### Disclaimer
This project is intended for research and educational purposes only. It should not be used as a substitute for professional medical advice or diagnosis.

## Overview

The Brain Tumor Classification project is a deep learning-based system designed to classify brain MRI images into different tumor types: 'glioma,' 'meningioma,' 'pituitary,' and 'no tumor.' This machine learning model has been trained on a diverse dataset containing over 6,000 brain MRI images, making it a robust tool for assisting in the diagnosis of brain tumors from medical imaging.

## Key Features:
- The project leverages the power of deep learning and utilizes the RESNET50 architecture to accurately classify brain MRI scans into distinct tumor categories.
- It can differentiate between four primary brain tumor types: glioma, meningioma, pituitary, and cases where no tumor is present. This capability aids in making informed decisions.
- The project is designed with an intuitive implementation that allows users to upload MRI images for classification effortlessly. 

## Usage
- Download the project.
- Download the saved model(BT_class) and dataset from [here](https://drive.google.com/drive/folders/1b83pEnYPyMckZOU4REXA62BMub8ImCz6?usp=sharing)
- Install the required dependencies pip install -r requirements.txt
- In the file, `test.py` update the image_path to your image's path.
- If running the file in terminal, run `python3 test.py`.
- If running in jupyter notebook, just run the entire code from `test.py` in a cell. 

## Results
The model achieved 99% accuracy on the testing data. 
The predictions can be seen in the `.ipynb` extention file. 
