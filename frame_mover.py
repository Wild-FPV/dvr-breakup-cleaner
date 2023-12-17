import os
import shutil

current_dir = os.getcwd()

folder_name = 'frame_samples'
breakup_folder_name = 'breakup'
clean_folder_name = 'clean'

#input frames to be moved to breakup folder.
#Recommended that you go through frame sample folder and write down frames with breakup

number_of_frames_moved = int(input("Please input the number of breakup frames you would like to move : "))

frames_to_move = []

number_frames_received = 0

while number_frames_received < number_of_frames_moved:
    current_frame = str(input("Please input the next sample frame number to be moved : ").zfill(4))
    
    frames_to_move.append(f'frame_{current_frame}.jpg')
    
    number_frames_received += 1
    
print(frames_to_move)

for name in frames_to_move:
    print(name)
    shutil.move(os.path.join(current_dir,folder_name,name),os.path.join(current_dir,breakup_folder_name,name))
