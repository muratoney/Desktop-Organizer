# Code for desktop organizer script :)
# Code by: muratoney

import os
import shutil

# gather file_paths
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
organizer_path = os.path.join(desktop_path, "_")
image_folder = os.path.join(organizer_path, 'Images')
other_folder = os.path.join(organizer_path, 'Other')
video_folder = os.path.join(organizer_path, 'Videos')
folder_folder = os.path.join(organizer_path, 'Folders')

os.makedirs(organizer_path, exist_ok=True)
os.makedirs(image_folder, exist_ok=True)
os.makedirs(other_folder, exist_ok=True)
os.makedirs(video_folder, exist_ok=True)


# go through files in desktop
print(os.listdir(desktop_path))
for file_name in os.listdir(desktop_path):
    # skip if file exists in orgaanized folder
    file_path = os.path.join(desktop_path, file_name)

    if file_name in ['Images', 'Other']:
        continue
    
    # check if file is image
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')) or "Photos" in file_name:
        shutil.move(file_path, image_folder)
    
    # check if file is document
    if file_name.lower().endswith(('.txt', '.doc', '.docx', '.pdf', '.ppt', '.pptx', '.xls', '.xlsx' , 'html')):
        shutil.move(file_path, other_folder)

    #check if file is video
    if file_name.lower().endswith(('.mp4', '.mkv', '.avi', '.mov')):
        shutil.move(file_path, video_folder)
    


