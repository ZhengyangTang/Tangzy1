
from google.cloud import vision_v1

client = vision_v1.ImageAnnotatorClient()
for count in range(10):
	with open('C:/0%d.jpg'%count, 'rb') as image_file:
		content = image_file.read()
	image = vision_v1.types.Image(content = content)
	response = client.web_detection(image = image)
	detection = response.web_detection
	file = open('C:/image_analysis.txt','a+',encoding = 'utf-8')
	file.write('labels for image%d:'%count+'\n')
	for i in detection.web_entities:
		file.write(i.description+'\n')
	file.close()
