from queue import Queue
from threading import Thread
import cv2
import time

from numpy import append
from Drawers.trailer_plotter import trailer_plotter



class ImageLoader:

    
    def __init__(self,img_path,logger,rois,json_file_name):
        self.img_path = img_path
        self.rois = rois
        self.json_file_name = json_file_name
        # self.q = Queue()
    
        print("in image loader init")  
        logger.info("Image loaded")
        self.frame_dict = {}
        self.main_q = Queue()
        self.obj = trailer_plotter(img_path,logger,rois,json_file_name)
        self.load_image_thread = Thread(target=self.obj.run)
        self.load_image_thread.daemon = True
        self.load_image_thread.start()
        time.sleep(0.2)

        logger.info("AT display finally")
        # if (not self.obj.q.empty()):
        while True:
            print("Dequeu")
            self.frame = self.obj.q.get_nowait()
            # self.dict[json_file_name].append(self.frame)
            cv2.namedWindow(json_file_name,cv2.WINDOW_NORMAL)
            cv2.imshow(json_file_name, self.frame[0])

            if cv2.waitKey(1)==ord('q'):    
                break
            time.sleep(0.2)
                
        cv2.destroyAllWindows()
        
        print("Hellllllllooooooo")
            
           

    
            


