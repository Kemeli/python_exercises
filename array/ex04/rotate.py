from PIL import Image
import numpy as np

def rotate(image):
	"""
	rotates an array image, displays the image and returns the rotated array

	Parameter:
	The array image to be rotated

	Creates a 3d array of zeros, with the same size as the original;
	Iterates through every pixel in the original array and copies them to the
	new array in different positions, in order to get the rotation effect;
	Creates and saves the rotated image;
	Returns the rotated array.
	"""
	try:
		height, width, channels = image.shape
		assert height == width, "array image must be square"
		rotated_arr = np.zeros((width, height, channels), dtype=np.uint8)
	except Exception as e:
		print(f'{type(e).__name__} : {str(e)}')
		return

	for i in range(height):
		for j in range(width):
			rotated_arr[width - 1 - j, i] = image[i, j]

	print(f'New shape after Transpose: {rotated_arr.shape}')
	rotated_img = Image.fromarray(rotated_arr)
	rotated_img.save("rotated_img.jpeg")
	return rotated_arr
