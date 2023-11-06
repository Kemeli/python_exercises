from PIL import Image
import numpy as np

def ft_load(path: str):
	"""
	transforms an image to an array

	parameters:
	path: (str) the path to the image

	transforms the image to array format, prints it's shape and returns the array
	"""
	try:
		img = Image.open(path)
		assert img.format == 'JPG' or img.format == 'JPEG', 'Invalid image format'
	except Exception as e:
		print(f'Error loading image: {str(e)}')
	else:
		np_data = np.asarray(img)
		shape = np_data.shape
		print("the shape of the image is", shape)
		return np_data
