import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
split = "0"

# user input and verification
file_name = input("What is the name of your annotation file")
while(split.lower() == "test" and split.lower() == "train"):
	split = input("Is this a train or test split?")

# calculates bbox for darknet detection(%)
def calculate_bbox(bbox, width, height):
	x = (int(bbox[0]) + int(bbox[2])/2) / int(width)
	y = (int(bbox[1]) + int(bbox[3])/2) / int(height)
	new_width = int(bbox[2]) / int(width)
	new_height = int(bbox[3]) / int(height)
	return x, y, new_width, new_height

# returning all category of our object detection
def category_list(file):
	list = []
	with open(file, "r") as f:
		for line in f.readlines():
			list.append(line.split(":")[0])
		return list

# returning filename of coresponding category
def filename_resolution(id, text):
	for line in text:
		number = line.split(",")[0]
		number = re.sub('[^0-9]', '', number)
		if "height" in line and number == id:
			return line.split('"')[9], re.sub('[^0-9]', '',line.split(',')[1]), re.sub('[^0-9]', '',line.split(',')[2])

# itterating over files in folder and splitting correct ones
for files in os.listdir(dir_path):
	if files == file_name:
		try:
			with open(files, "r") as f:
				text = f.read()
				text = text.split("{")
		except:
			print(f"cannot read {files}")
			exit(1)

categories = category_list("category.txt")

# acquiring unique category and image_id of this category
for line in text:
	if "category_id" in line and line.split('"')[8].replace(":", "").replace(",", "") in categories:
		index = categories.index(line.split('"')[8].replace(":", "").replace(",", ""))
		image_id = line.split('"')[12].replace(":","").replace(",","")
		bbox = line.split('[')[1].split("]")[0].split(",")
		name, height, width =  filename_resolution(image_id, text)
		x, y, new_width, new_height = calculate_bbox(bbox, width, height)
		name = f"{name}_annotation_{split}.txt"
		with open(os.path.join("C:\\Users\\Moxis\\Downloads\\datasets\\JPEGImages(slovakia)\\JPEGImages",name),"a") as f:
			f.write(f"{index} {x} {y} {new_width} {new_height}\n")

