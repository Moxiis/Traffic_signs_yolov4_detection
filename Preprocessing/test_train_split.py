# split train and test images and annotations to separate folders
import os
import shutil

images_directory = r"C:\Users\Moxis\Downloads\datasets\JPEGImages(slovakia)\JPEGImages"
test_directory = r"C:\Users\Moxis\Downloads\datasets\JPEGImages(slovakia)\test"
train_directory = r"C:\Users\Moxis\Downloads\datasets\JPEGImages(slovakia)\train"

for files in os.listdir(images_directory):
	if files.endswith("txt"):
		img = files.split("_")[0]
		if "train" in files:
			shutil.move(os.path.join(images_directory, files), os.path.join(train_directory, files))
			shutil.move(os.path.join(images_directory, img), os.path.join(train_directory, img))
		elif "test" in files:
			shutil.move(os.path.join(images_directory, files), os.path.join(test_directory, files))
			shutil.move(os.path.join(images_directory, img), os.path.join(test_directory, img))

# renaming our annotation files so that they are named the same as the corresponding jpg files			
for file in os.listdir(test_directory):
  if file.endswith(".txt"):
    new_file = file.split(".")[0] + ".txt"
    os.rename(file, new_file)
	
for file in os.listdir(train_directory):
  if file.endswith(".txt"):
    new_file = file.split(".")[0] + ".txt"
    os.rename(file, new_file)	
