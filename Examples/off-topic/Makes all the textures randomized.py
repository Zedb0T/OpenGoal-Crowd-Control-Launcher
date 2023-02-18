import os
import random
import shutil

root_folder = r"C:\Users\NinjaPC\Documents\Github\Jak-1-wood-crate-tracker\data\decompiler_out\jak1\textures"
# Define a list of strings to skip if present in the image filename
strings_to_skip = ["watermark", "copy","font","ascii"]

# Loop through all the directories in the root folder
for dirpath, dirnames, filenames in os.walk(root_folder):
    # Create a list of image filenames in the directory
    image_files = [f for f in filenames if f.lower().endswith(".png") or f.lower().endswith(".jpg")]
    # If there are at least two images in the directory, shuffle them and swap their contents
    if len(image_files) >= 2:
        random.shuffle(image_files)
        for i in range(len(image_files) - 1):
            # Swap the contents of the current and next image file
            print("Swapping file " + str(i) + " of " + str(len(image_files) - 1))
            img1_path = os.path.join(dirpath, image_files[i])
            img2_path = os.path.join(dirpath, image_files[i+1])
            img1_filename = os.path.splitext(image_files[i])[0]
            img2_filename = os.path.splitext(image_files[i+1])[0]
            temp_file = "__temp_swap_file__"
            skip_image = False
            # Check if any strings to skip are present in either filename
            for string in strings_to_skip:
                if string in img1_filename or string in img2_filename:
                    print("Skipping images with string: " + string)
                    skip_image = True
                    break
            if skip_image:
                continue
            if "clouds" in img1_filename or "sky" in img1_filename:
                shutil.copy2(img2_path, img1_path)
            elif "clouds" in img2_filename or "sky" in img2_filename:
                shutil.copy2(img1_path, img2_path)
            else:
                shutil.copy2(img1_path, temp_file)
                shutil.copy2(img2_path, img1_path)
                shutil.copy2(temp_file, img2_path)
                os.remove(temp_file)
