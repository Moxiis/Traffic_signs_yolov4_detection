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