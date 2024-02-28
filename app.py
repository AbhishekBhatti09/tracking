import json
from Loaders.ImageLoader import ImageLoader
import requests
import logging
from threading import Thread
from constants import img_903,img_904,img_905,img_906,read_json_file


# Create and configure logger
logging.basicConfig(filename="/home/wot-abhishek/JoiningDocument/AI_ML_Training/Abhishek-Bhatti-AI-ML-Training-2024/opencv-intro/trailer_plotting/app.log",
                    format='%(asctime)s %(message)s')
 
# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)

 
try:
    rois_903, rois_904,rois_905,rois_906 = read_json_file()
    logger.info("ROI Json data read success")
except Exception as e:
    logger.exception("Error in reading json")

m1 = ImageLoader(img_903,logger,rois_903,'903.json')




# m2 = ImageLoader(img_904,logger,rois_904,'904.json')
# main1 = Driver()
# main1 = Driver(img_904,rois_904,'904.json')

# main2 = Driver(img_905,rois_905)
# main2 = Driver(img_906,rois_906)