import cv2
import os

def convert_images_to_grayscale(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            filepath = os.path.join(input_folder, filename)
            img = cv2.imread(filepath)
            
            if img is None:
                print(f"Could not open or find the image: {filepath}")
                continue
            
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            output_filepath = os.path.join(output_folder, filename)
            cv2.imwrite(output_filepath, gray_img)
        else:
            print(f"Skipping file: {filename} (not an image)")

convert_images_to_grayscale('D:/My Documents/GIT Projects/IEEE-Hack-the-meta/ASL_F/asl_alphabet_test/Z', 'D:/My Documents/GIT Projects/IEEE-Hack-the-meta/ASL_F/asl_alphabet_test/Z')
print("Z Done")