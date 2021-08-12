import cv2
import imutils
import numpy as np
import argparse

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def detect(frame):
   bounding_box_coordinates, weights = HOGCV.detectMultiScale(frame, winStride = (4,4), padding = (8,8), scale = 1.03)

   person = 1
   for x,y,w,h in bounding_box_coordinates:
       cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0)2)
       cv2.putText(frame, person, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),1)
       person +=1

       cv2.putText(frame, 'Status:Detecting Persons', (40,40), cv2.FONT_HERSHEY_DUPLEX, 0.8,(255,0,0),2)
       cv2.putText(frame, 'Total Perons: {person -1}', (40,70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0),2)
       cv2.imshow('output',frame)

       return frame


   def humanDetector(args):
       image_path = args["image"]
       video_path = args['video']
       if str(args["camera"]) == 'true'
           camera = True
       else:
           camera = False

       writer = None
       if args['output'] is not None & image_path is None:
           writer = cv2.VideoWriter(args['output'], cv2.VideoWriter_fourcc(*'MJPG'), 10,(600,600))

       if camera:
           print('[INFO] Opening Web Cam')
           detectByCamera(output_path,writer)
       elif video_path is not None:
           print('[INFO] Opening Video from path.')
       elif image_path is not None:
           print('[INFO] Opening image from path')
           detectByPathImage(image_path, args['output'])


def detectByCamera(writer):
   video = cv2.VideoCapture(0)
   print('Detecting People')

   while True:
       check, frame = video.read()

       frame = detect(frame)
       if writer is not None:
           writer.write(frame)


       key = cv2.waitKey(1)
       if key == ord('q'):
           break

   video.release()
   cv2.destroyAllWindows()

def detectByPathImage(path,output_path):
   image = cv2.imread(path)
   image = imutils.resize(image, width = min(800, image.shape[1]))

   result_image = detect(image)

   if output_path is not None:
       cv2.imwrite(output_path, result_image)

   cv2.waitKey(0)
   cv2.destroyAllWindows()

def argsParser():
   arg_parse = argparse.ArgumentParser()
   arg_parse.add_argument("-v")
   arg_parse.add_argument("-i")
   arg_parse.add_argument("-c")
   arg_parse.add_argument("-o")


   args = vars(arg_parse.parse_args())

   return args


if __name__ "__main__":
       HOGCV = cv2.HOGDescriptor()
       HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


       args = argsParser()
       humanDetector(args)



