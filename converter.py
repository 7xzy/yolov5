import xml.etree.ElementTree as ET
import os

categories=["person","bird","cat","cow","dog","horse","sheep","aeroplane","bicycle","boat",\
	"bus","car","motorbike","train","bottle","chair","diningtable","pottedplant","sofa","tvmonitor"]

print("START")

path=r'C:\Users\Utente\Documents\GitHub\datasets\VOC2007\test'

images=os.listdir(path=path+r'\annotations')

for image in images:
	print("READING '{}' FILE".format(image))

	tree = ET.parse(path+r'\annotations\{}'.format(image))
	annotation = tree.getroot()

	size=annotation.find("size")
	w, h = int(size.find("width").text), int(size.find("height").text)

	outputs=[]

	for object in annotation.findall("object"):
		object_name=object.find("name").text
		object_id=categories.index(object_name)

		box=object.find("bndbox")
		box_x=(int(box.find("xmin").text)+int(box.find("xmax").text))/(2*w)
		box_y=(int(box.find("ymin").text)+int(box.find("ymax").text))/(2*h)

		box_w=(int(box.find("xmax").text)-int(box.find("xmin").text))/w
		box_h=(int(box.find("ymax").text)-int(box.find("ymin").text))/h

		if image=='005137.xml':
			print(box_x,box_y,box_w,box_h)

		s="{} {:.6f} {:.6f} {:.6f} {:.6f}".format(object_id,box_x,box_y,box_w,box_h)
		outputs.append(s)

	output="\n".join(outputs)

	with open(path+r'\labels\{}'.format(image.replace(".xml",".txt")),"w") as label:
		label.write(output)

