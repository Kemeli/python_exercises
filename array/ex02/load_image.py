# import PIL as pil
from PIL import Image
import numpy as np

def ft_load(path: str):
	img = Image.open(path)
	np_data = np.asarray(img)
	print(np_data.shape)
	return np_data
	# print(img.format)
	# print(img.size)
	# print(img.mode)
