import os
import numpy as np
from pathlib import Path
from rembg import remove
from PIL import Image
from keras._tf_keras.keras.preprocessing.image import load_img, img_to_array

def check_valid_file_format(file_name, allowed_image_exts):
    file_ext = os.path.splitext(file_name)[1].lower()
    if file_ext in allowed_image_exts:
        return True
    else:
        return False

def check_valid_file_size(file_path, min_image_size_kb, max_image_size_kb):
    min_size_bytes = min_image_size_kb * 1024
    max_size_bytes = max_image_size_kb * 1024
    file_size = os.path.getsize(file_path)
    if (file_size >= min_size_bytes) and (file_size <= max_size_bytes):
        return True
    else:
        return False

def remove_image_background(file_path):
    input_image = Image.open(file_path)
    output_image = remove(input_image)
    return output_image

def is_existing_dir(dir_path):
    return os.path.isdir(dir_path)

def is_existing_path(path):
    return os.path.exists(path)

def preprocess_image(image_path, image_size):
    # Load the image with the target size
    img = load_img(image_path, target_size=image_size)
    # Convert the image to a numpy array
    img_array = img_to_array(img)
    # Rescale pixel values (same as training)
    img_array = img_array / 255.0
    # Expand dimensions to match the input shape of the model (1, 150, 150, 3)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array
            
def process_file(file_path, 
                 output_path):
    
    if not is_existing_path(output_path):
        remove_image_background(file_path).save(output_path)
        print(f"Background removed for image {file_path} saved to {output_path}")
        return True
    else:
        print(f"Output file already exists: {output_path}. Skipping process.")
        return False

def process_files(file_names, 
                  processed_class_dir_path, 
                  root, 
                  allowed_image_exts, 
                  min_image_size_kb, 
                  max_image_size_kb):
    
    for file_name in file_names:
        if file_name.lower() == '.ds_store':
            continue
        file_path = os.path.join(root, file_name)
        
        if check_valid_file_format(file_name, allowed_image_exts) and check_valid_file_size(file_path, min_image_size_kb, max_image_size_kb):
            print(f"Processing file: {file_path}")
            output_path = os.path.join(processed_class_dir_path, "no_bg_" + file_name.split('.')[0] + '.png')
            process_file(file_path, output_path)

    return True