import json 
import cv2
import re
import numpy as np
from queue import Queue
from threading import Thread
import time

class trailer_plotter:

    def __init__(self):
        # self.q = Queue()
        self.read_trailer_info('903.json')
        self.img = np.zeros((5120, 2560, 3), dtype='uint8')
   
    def read_trailer_info(self,json_file_name):
     
        with open('/home/wot-abhishek/JoiningDocument/AI_ML_Training/Abhishek-Bhatti-AI-ML-Training-2024/opencv-intro/trailer_plotting/trailer_entries/'+json_file_name, 'r') as out_file:
                c=out_file.read()
                x=json.loads(c)
        # length = len(x['messages'])
        # print(length)
        # self.trailer_data = []
        # trailer_data_at_particular = []
        # for i in (x['messages']):
        #     for j in (i['objects']):
        #         if j[:3] =='TOP':
        #             data = re.split('\|',j)
        #             trailer_data_at_particular.append([i['ts'],data[1],data[3],data[4],data[5],data[6]])
        #     self.trailer_data.append(trailer_data_at_particular) 
        #     trailer_data_at_particular = []
        self.process_and_display_all_frames(x, 5120, 2560)




   

    def process_frame(self,frame_data, image_width, image_height):

        frame_id = frame_data['id']

        ts = frame_data['ts']

        sensor = frame_data['sensor']

        objects = frame_data['objects']


        image = np.zeros((image_height, image_width, 3), dtype=np.uint8)

       
        

        for obj in objects:
            # print(len(obj))

            parts = obj.split('|')

            if parts[0] == "TOP":

                trailer_id = parts[1]

                x1 = int(parts[3]) * image_width // 10000

                y1 = int(parts[4]) * image_height // 10000

                x2 = int(parts[5]) * image_width // 10000

                y2 = int(parts[6]) * image_height // 10000

                # Draw bounding box and Trailer ID

                cv2.rectangle(image, (x1, y1), (x2, y2), (0,255,255), 2) # Yellow for trailer

                cv2.putText(image, f"ID: {trailer_id}", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,255), 2)

        # Display frame time

        cv2.putText(image, f"Frame Time: {ts}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,255), 2)

        # Return the processed image

        return image



    def process_and_display_all_frames(self,data, image_width, image_height):

        for frame_data in data['messages']:

            processed_image = self.process_frame(frame_data, image_width, image_height)

            

            # Display the processed image
            cv2.namedWindow('Frame',cv2.WINDOW_NORMAL)
            cv2.imshow("Frame", processed_image)

            

            if cv2.waitKey(33) & 0xFF == ord('q'):  # Press 'q' to quit early

                break

        cv2.destroyAllWindows()





tp = trailer_plotter()



