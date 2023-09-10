import os
from sklearn.model_selection import train_test_split

data_path = 'D:/My Documents/GIT Projects/IEEE-Hack-the-meta/ASL/asl_alphabet'
train_path = 'D:/My Documents/GIT Projects/IEEE-Hack-the-meta/ASL/asl_alphabet_train'
test_path = 'D:/My Documents/GIT Projects/IEEE-Hack-the-meta/ASL/asl_alphabet_test'

data_dict = {}

for class_dir in os.listdir(data_path):
    class_dir_path = os.path.join(data_path, class_dir)
    if os.path.isdir(class_dir_path):
        files = [f for f in os.listdir(class_dir_path) if os.path.isfile(os.path.join(class_dir_path, f))]
        data_dict[class_dir] = files

for class_name, files in data_dict.items():
    train_files, test_files = train_test_split(files, test_size=0.5)
    
    os.makedirs(os.path.join(train_path, class_name), exist_ok=True)
    os.makedirs(os.path.join(test_path, class_name), exist_ok=True)
    
    for file in train_files:
        os.rename(os.path.join(data_path, class_name, file), os.path.join(train_path, class_name, file))

    for file in test_files:
        os.rename(os.path.join(data_path, class_name, file), os.path.join(test_path, class_name, file))
