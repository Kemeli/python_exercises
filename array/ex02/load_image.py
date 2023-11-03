# import PIL as pil
from PIL import Image
import numpy as np

def ft_load(path: str):
	try:
		img = Image.open(path)
		assert img.format == 'JPG' or img.format == 'JPEG', 'Invalid image format'
	except Exception as e:
		print(f'Error loading image: {str(e)}')
	else:
		np_data = np.asarray(img)
		print(np_data.shape)
		return np_data

