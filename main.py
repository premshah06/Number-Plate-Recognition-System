import streamlit as st
import base64
import cv2
import imutils
import numpy as np
import pytesseract
from matplotlib import pyplot as plt
import pandas as pd

file_path = 'violations.xls'
df = pd.read_excel(file_path)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

st.set_page_config(layout="wide", page_title="Number Plate Detection And Recognition")

# main page
st.write("# Number Plate Detection And Recognition")
st.write("## Motivation behind the project :bulb:")
st.write("Ahmedabad accounts for the maximum percentage of traffic violations in Gujarat, reveals a survey. Violations such as not wearing helmets, seat-belts, overspeeding, driving on the wrong side of the road and talking over mobile phone during driving is maximum in Ahmedabad (61 per cent), followed by Surat (45 per cent), Rajkot (39 per cent) and Vadodara (28 per cent), suggests a survey conducted by the Associated Chambers of Commerce and Industries of India (Assocham). Over 65 per cent of two-wheeler riders and 55 per cent of car drivers have been found to be using mobile phones, texting and listening to music while driving on Ahmedabad roads,” the survey said.")
st.write("**Source:** [Traffic violations in ahmedabad by indian express](https://indianexpress.com/article/cities/ahmedabad/maximum-traffic-violations-road-accidents-take-place-in-ahmedabad-survey/)")
st.write("### **The motivation behind this project is make traffic system more secure by detect and recognize license plates of vehicles that violates traffic rules.**")
st.write("")

col1, col2 = st.columns(2)
with col1:
    st.write("**Without using NPDR**")
    file_ = open("meme.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="busted">',
        unsafe_allow_html=True,
    )

with col2:
    st.write("**When using NPDR**")
    file_ = open("meme2.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="busted">',
        unsafe_allow_html=True,
    )


# sidebar
st.sidebar.write("### NPDR")
st.sidebar.image('./car1.jpeg')
st.sidebar.write("Upload an image to detect and recognize number plates. :gear:")
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if my_upload is not None:
    st.sidebar.write("Your Image:")
    st.sidebar.image(my_upload)
    file_bytes = np.asarray(bytearray(my_upload.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    img = cv2.resize(opencv_image, (600,400) )
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    gray = cv2.bilateralFilter(gray, 13, 15, 15) 
    edged = cv2.Canny(gray, 30, 200)
    contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]
    screenCnt = None
    cv2.drawContours(img,contours,-1,(0,255,0),3)

    for c in contours:
        
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)
    
        if len(approx) == 4:
            screenCnt = approx
            break

    if screenCnt is None:
        detected = 0
        print ("No contour detected")
    else:
        detected = 1

    if detected == 0:
        st.sidebar.write("There is something wrong with this image, pls try again with other image")

    if detected == 1:
        cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)
        mask = np.zeros(gray.shape,np.uint8)
        new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
        new_image = cv2.bitwise_and(img,img,mask=mask)
        (x, y) = np.where(mask == 255)
        (topx, topy) = (np.min(x), np.min(y))
        (bottomx, bottomy) = (np.max(x), np.max(y))
        Cropped = gray[topx:bottomx+1, topy:bottomy+1]
        text = pytesseract.image_to_string(Cropped, config='--psm 11')
        img = cv2.resize(img,(500,300))
        Cropped = cv2.resize(Cropped,(400,200))
        st.sidebar.write("Number Plate:")
        st.sidebar.image(Cropped)
        st.sidebar.write(f"Number Plate in Textutal Format: {text}")

        number_plate = text
        count = 0
        if number_plate in df['number_plate'].values:
            df.loc[df['number_plate'] == number_plate, 'count'] += 1
            count = df.loc[df['number_plate'] == number_plate, 'count'].values[0]
        else:
            new_row = {'number_plate': number_plate, 'count': 1}
            df = df.append(new_row, ignore_index=True)
            count = df.loc[df['number_plate'] == number_plate, 'count'].values[0]
        df.to_excel(file_path, index=False)
        st.sidebar.write(f"No. of times detected: {count}")
else:
    pass
