import json 
import cv2
import re
import numpy as np
from queue import Queue
from threading import Thread
from datetime import datetime
from queue import Queue
# from Drawers.Roi_Drawer import Roi_Drawer

class trailer_plotter:

    def __init__(self,img_path,logger,rois,json_file_name):
        print("trailer_plotter")
        self.rois = rois
        self.image_width = 5120
        self.image_height = 2560
        self.json_file_name = json_file_name
        self.img = cv2.imread(img_path)
        self.q = Queue()
        
        with open('/home/wot-abhishek/JoiningDocument/AI_ML_Training/Abhishek-Bhatti-AI-ML-Training-2024/opencv-intro/trailer_plotting/trailer_entries/'+self.json_file_name, 'r') as out_file:
                c=out_file.read()
                self.x=json.loads(c)
        
        roi_TPP = np.array(self.rois['TPP'], np.int32)
        roi_DPP = np.array(self.rois['DPP'], np.int32)
        roi_Road = np.array(self.rois['ROAD'], np.int32)

        self.img = cv2.polylines(self.img, [roi_TPP],  True, (255,0,0),   thickness=4)
        self.img = cv2.polylines(self.img, [roi_DPP],  True, (0, 255,0),   thickness=4)
        self.img = cv2.polylines(self.img, [roi_Road],  True, (0, 0, 255),   thickness=4) 


        
      
        print("IN trailer plotter")
        
        
    def run(self):
        print("In run")
        while True:
            for frame_data in self.x['messages']:
                frame_id = frame_data['id']
                ts = frame_data['ts']
                objects = frame_data['objects']


                self.img1 = self.img.copy()
                
                # self.img1 = cv2.putText(self.img1, f"{ts}", (30, 150), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,255,255), 2,cv2.LINE_4)
                
                
                for obj in objects:
                    parts = obj.split('|')
                    if parts[0] == "TOP":
                        trailer_id = parts[1]

                        x1 = int(parts[3]) * self.image_width // 10000
                        y1 = int(parts[4]) * self.image_height // 10000
                        x2 = int(parts[5]) * self.image_width // 10000
                        y2 = int(parts[6]) * self.image_height // 10000

                        # Draw bounding box and Trailer ID

                        self.img1 = cv2.rectangle(self.img1, (x1, y1), (x2, y2), (0,255,255), 1) # Yellow for trailer

                        self.img1 = cv2.putText(self.img1, f"ID: {trailer_id}", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,255), 2)

                self.img1 = cv2.putText(self.img1, f"{ts}", (30, 150), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,255,255), 2,cv2.LINE_4)
                # self.img1 = cv2.resize(self.img1,(500,300))
                print("Img complete")
                # cv2.namedWindow(self.json_file_name,cv2.WINDOW_NORMAL)
                # cv2.imshow(self.json_file_name, self.img1)

                # if cv2.waitKey(0)==ord('q'):
                #     break
                try:
                    print("In queue")
                    self.q.put_nowait([self.img1])
                    print("inserted in queue")
                
                except:
                    self.q.get_nowait()
                    self.q.put_nowait([self.img1])  



  




   

    
                







