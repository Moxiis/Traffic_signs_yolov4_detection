import os
import re
import cv2

dir_path = os.path.dirname(os.path.realpath(__file__))
categories = []
file_name = input("What is the name of your annotation file")

# appending to txt all important signs category and passing all unimportant
def category_to_txt(category):
	with open("category.txt", "a") as file:
		important = 0
		while important != "y" and important != "n":
			important = input("czy jest on ważny(y/n)\n")
		if important == "n":
			return
		sign = input("jaki to znak?\n")
		file.write(f"{category}:{sign}\n")

# showing sign image from appropriate category
def show_img(file, bbox):
	directory = f"C:\\Users\\Moxis\\Downloads\\datasets\\JPEGImages(slovakia)\\JPEGImages\\{file}"
	img = cv2.imread(directory)
	bbox = bbox.split(',')
	sub_image = img[int(bbox[1]):int(bbox[1]) + int(bbox[3]), int(bbox[0]):int(bbox[0]) + int(bbox[2])]
	cv2.imshow('image', sub_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

#checking if item is in list
def in_list(list, string):
	string = string.split('"')[8]
	string = re.sub('[^0-9]', '', string)
	for item in list:
		if item == string:
			return False
	return True

# returning filename of coresponding category
def filename(id, text):
	for line in text:
		number = line.split(",")[0]
		number = re.sub('[^0-9]', '', number)
		if "height" in line and number == id:
			return line.split('"')[9]

# itterating over files in folder and splitting correct ones
for files in os.listdir(dir_path):
	if files.lower() == file_name.lower():
		with open(files, "r") as f:
			text = f.read()
			test = text.split("{")

# acquiring unique category and image_id of this category
for line in test:
	if "category_id" in line and in_list(categories, line):
		category = line.split('"')[8].replace(":","").replace(",","")
		image_id = line.split('"')[12].replace(":","").replace(",","")
		bbox = line.split('[')[1].split("]")[0]
		show_img(filename(image_id, test), bbox)
		category_to_txt(category)
		categories.append(category)
