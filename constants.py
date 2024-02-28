import json
import requests

img_903 = '/home/wot-abhishek/JoiningDocument/AI_ML_Training/Abhishek-Bhatti-AI-ML-Training-2024/opencv-intro/trailer_plotting/camera_images/MRKDC_0984_0903.jpg'
img_904 = '/home/wot-abhishek/JoiningDocument/AI_ML_Training/Abhishek-Bhatti-AI-ML-Training-2024/opencv-intro/trailer_plotting/camera_images/MRKDC_0984_0904.jpg'
img_905 = '/home/wot-abhishek/JoiningDocument/AI_ML_Training/Abhishek-Bhatti-AI-ML-Training-2024/opencv-intro/trailer_plotting/camera_images/MRKDC_0984_0905.jpg'
img_906 = '/home/wot-abhishek/JoiningDocument/AI_ML_Training/Abhishek-Bhatti-AI-ML-Training-2024/opencv-intro/trailer_plotting/camera_images/MRKDC_0984_0906.jpg'

def read_json_file():

        url = "https://lms-wot.s3.ap-south-1.amazonaws.com/trailer_yard.camera_rois-65dc30dedcdf0.json"
        response = requests.get(url)
        data = json.loads(response.text)
        roi_903 = {}
        roi_904 = {}
        roi_905 = {}
        roi_906 = {}

        for i in range(len(data)):
            if data[i]["cam_name"] == "MRKDC_0984_0903" :
                roi_903[data[i]["roi"]] =  data[i]["points"]
            if data[i]["cam_name"] == "MRKDC_0984_0904" :
                roi_904[data[i]["roi"]] =  data[i]["points"]
            if data[i]["cam_name"] == "MRKDC_0984_0905" :
                roi_905[data[i]["roi"]] =  data[i]["points"]
            if data[i]["cam_name"] == "MRKDC_0984_0906" :
               roi_906[data[i]["roi"]] =  data[i]["points"]
            

        return roi_903, roi_904,roi_905,roi_906



    
                

