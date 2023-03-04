import shutil
import os
from winsound import PlaySound
import winsound

script_dir = os.path.dirname(os.path.abspath(__file__))
# navigate to the parent directory
parent_dir = os.path.join(script_dir, "..")

def copy_items(items_list, dest_path):
    for item in items_list:
        item_name = os.path.basename(item)
        if os.path.isdir(item):
            if item_name in ['goal_src', 'custom_levels', 'decompiler', 'game', 'launcher']:
                # Create the parent directory if it doesn't exist
                data_path = os.path.join(dest_path, 'data')
                if not os.path.exists(data_path):
                    os.makedirs(data_path)
                # Remove the existing directory if it exists
                dest_item = os.path.join(data_path, item_name)
                if os.path.exists(dest_item):
                    shutil.rmtree(dest_item)
                # Copy the directory to the 'data' folder
                shutil.copytree(item, dest_item, copy_function=shutil.copy2)
            else:
                # Remove the existing directory if it exists
                dest_item = os.path.join(dest_path, item_name)
                if os.path.exists(dest_item):
                    shutil.rmtree(dest_item)
                # Copy the directory and its contents to the destination path
                shutil.copytree(item, dest_item, copy_function=shutil.copy2)
        else:
            # Create the parent directories for the file, if they don't exist
            parent_dir = os.path.join(dest_path, os.path.dirname(item))
            if not os.path.exists(parent_dir):
                os.makedirs(parent_dir)
            # Remove the existing file if it exists
            dest_file = os.path.join(dest_path, item_name)
            if os.path.exists(dest_file):
                os.remove(dest_file)
            # Copy the file to the destination path
            shutil.copy2(item, dest_file)

items_list = [
    os.path.join(parent_dir, 'opengoal-crowd-control','data','goal_src'),
    os.path.join(parent_dir,'opengoal-crowd-control','gk.exe'),
    os.path.join(parent_dir,'opengoal-crowd-control','goalc.exe'),
    os.path.join(parent_dir,'opengoal-crowd-control','extractor.exe'),
    os.path.join(parent_dir,'opengoal-crowd-control','data','custom_levels'),
    os.path.join(parent_dir,'opengoal-crowd-control','data','decompiler'),
    os.path.join(parent_dir,'opengoal-crowd-control','data','game'),
    os.path.join(parent_dir,'opengoal-crowd-control','data','launcher')]
dest_path = os.path.join(parent_dir,'Release','openGOAL')
copy_items(items_list, dest_path)
# Play the audio file when the copy is complete
audio_file = os.path.join(parent_dir,"unpackaged resources", 'ok.wav')

PlaySound(audio_file, winsound.SND_FILENAME)