# Plant Disease Detection Website

## Overview
This project is a web application designed to detect plant diseases using deep learning models. Users can upload images of plants, and the application will identify potential diseases and provide relevant information. The application is built using Flask for the backend, TensorFlow for the machine learning models, and OpenCV for image processing.

## Features
- Detects diseases for a variety of plants.
- Provides detailed information about detected diseases.
- User-friendly interface for uploading plant images.
- List of prominent agronomists and their contributions.

## Technologies Used
- **Flask**: A micro web framework for Python.
- **TensorFlow**: An open-source library for machine learning.
- **OpenCV**: A library for image processing.
- **NumPy**: A library for numerical operations.
- **JSON**: A format for structuring data.

## Setup Instructions

### Prerequisites
- Python 3.x
- Flask
- TensorFlow
- OpenCV
- NumPy

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/mjiid/plant-disease
    cd plant-disease
    ```

2. Create a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application
1. Navigate to the project directory:
    ```sh
    cd plant-disease
    ```

2. Run the Flask application:
    ```sh
    python main.py
    ```

3. Open your web browser and go to `http://127.0.0.1:5000`.

## Usage
1. Upload an image of a plant through the web interface.
2. The application will process the image and display the detected disease along with detailed information.


