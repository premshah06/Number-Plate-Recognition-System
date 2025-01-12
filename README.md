# Number Plate Recognition System 🚗🔍

## Overview
The **Number Plate Recognition System** is a modern solution designed to enhance road safety and enforce traffic laws effectively. Using cutting-edge **Computer Vision** and **Optical Character Recognition (OCR)** techniques, this system detects and recognizes license plates from uploaded images, providing actionable insights for law enforcement and civic authorities.

---

## Features

- **Real-Time Detection**: Processes images and extracts license plate numbers within ~2 seconds.
- **High Accuracy**: Achieves ~90% detection accuracy under various conditions.
- **Interactive Interface**: Built with Streamlit for a seamless user experience.
- **Scalable Data Logging**: Tracks and updates vehicle violation records.
- **Comprehensive Insights**: Enables data-driven decision-making to improve traffic management systems.

---

## Skills and Technologies Used

- **Programming Language**: Python
- **Computer Vision**: OpenCV
- **Optical Character Recognition**: Tesseract OCR
- **Data Manipulation**: Pandas
- **Visualization**: Streamlit, Matplotlib
- **Data Storage**: Excel/Spreadsheet Integration

---

## How It Works

1. **Image Upload**: Users upload images through the Streamlit interface.
2. **Image Processing**: The system uses OpenCV for contour detection, edge detection, and grayscale filtering to identify the license plate.
3. **Text Extraction**: Tesseract OCR converts the detected plate into text.
4. **Data Logging**: Violation records are updated and stored in an Excel file for future reference.
5. **Real-Time Feedback**: Displays the detected license plate text and logs the number of violations.

---

## Directory Structure
```plaintext
premshah06-number-plate-recognition-system/
├── README.md                # Project documentation
├── main.py                  # Main application code
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/premshah06/number-plate-recognition-system.git
   ```

2. Navigate to the project directory:
   ```bash
   cd premshah06-number-plate-recognition-system
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up Tesseract OCR:
   - Download and install Tesseract from [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).
   - Update the `tesseract_cmd` path in `main.py`.

5. Run the application:
   ```bash
   streamlit run main.py
   ```

---

## Usage

1. Launch the application in your browser.
2. Upload an image containing a license plate.
3. View the detected plate number and log updates in real-time.

---

## Metrics

- **Detection Accuracy**: ~90%
- **Processing Time**: ~2 seconds per image
- **Records Logged**: Vehicle violations tracked effectively

---

## Future Enhancements

- **Video Stream Integration**: Extend functionality to support real-time video feeds.
- **Multi-Language OCR**: Expand OCR capabilities for international license plates.
- **Cloud Storage**: Integrate with cloud services for scalable data storage.
- **Advanced Analytics**: Add predictive analytics for traffic trend analysis.

