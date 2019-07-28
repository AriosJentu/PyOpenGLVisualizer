# from PIL import Image
import cv2
import numpy as np

def compare(img1, img2):

	"""
	i1 = Image.open(img1)
	i2 = Image.open(img2)

	if (i1.mode != i2.mode):
		print("Different kinds of images.")

	if (i1.size != i2.size):
		print("Different sizes.")
 
	pairs = zip(i1.getdata(), i2.getdata())

	if len(i1.getbands()) == 1:
		# for gray-scale jpegs
		dif = sum(abs(p1-p2) for p1,p2 in pairs)
	else:
		dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
	 
	ncomponents = i1.size[0] * i1.size[1]
	print(dif, ncomponents, dif/255, dif*100/(255*ncomponents))
	percentage = (dif/255) * (100 / ncomponents)
	#print("Difference (percentage):", percentage, ncomponents, dif)
	"""

	aimg1 = cv2.imread(img1, 0)
	aimg2 = cv2.imread(img2, 0)

	#--- take the absolute difference of the images ---
	res = cv2.absdiff(aimg1, aimg2)
	percentage = (np.count_nonzero(res) * 100)/ res.size
	
	return percentage