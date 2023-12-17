import cv2
import os
import random

dvr_filename = input("DVR filename : ")
output_folder_name = 'frame samples'

sample_percent = 5

if not os.path.exists(output_folder_name):
    os.mkdir(output_folder_name)
    
if not os.path.exists("breakup"):
    os.mkdir("breakup")
    
if not os.path.exists("clean"):
    os.mkdir("clean")
    

dvr = cv2.VideoCapture(dvr_filename)

if not dvr.isOpened():
    print("Video file could not be opened")
    exit()
    
    
frame_count = int(dvr.get(cv2.CAP_PROP_FRAME_COUNT))

frames_removed = int(frame_count * (sample_percent / 100))

sample_frame_numbers = random.sample(range(frame_count),frames_removed)

frame_number = 0

while True:
    ret, frame = dvr.read()
    
    
    if not ret:
        break
    
    if frame_number in sample_frame_numbers:
        frame_filename = os.path.join(output_folder_name, f'frame_{frame_number:04d}.jpg')
        cv2.imwrite(frame_filename,frame)
        
    
    frame_number += 1
    
    
dvr.release()

print(f'{frames_removed} frames grabbed and saved to {output_folder_name}')

        