from PIL import Image
import numpy as np

def ft_invert(image_arr):
	"""
	Inverts array image color and displays new image
	"""
	try:
		inverted_img = 255 - image_arr
		image = Image.fromarray(inverted_img)
		image.save("inverted_img.jpg")
	except Exception as e:
		print(f'{type(e).__name__} : {str(e)}')


def ft_red(image_arr):
	"""
	Keeps only red channel and displays image

	Parameter: 3d image array
	"""
	try:
		red = image_arr[:, :, 0]
		new_arr = np.zeros_like(image_arr)
		new_arr[:, :, 0] = red

		image = Image.fromarray(new_arr)
		image.save("red_img.jpg")
	except Exception as e:
		print(f'{type(e).__name__} : {str(e)}')


def ft_green(image_arr):
	"""
	Keeps only green channel and displays image

	Parameter: 3d image array
	"""
	try:
		green = image_arr[:, :, 1]
		new_arr = np.zeros_like(image_arr)
		new_arr[:, :, 1] = green

		image = Image.fromarray(new_arr)
		image.save("green_img.jpg")
	except Exception as e:
		print(f'{type(e).__name__} : {str(e)}')


def ft_blue(image_arr):
	"""
	Keeps only blue channel and displays image

	Parameter: 3d image array
	"""
	try:
		blue = image_arr[:, :, 2]
		new_arr = np.zeros_like(image_arr)
		new_arr[:, :, 2] = blue

		image = Image.fromarray(new_arr)
		image.save("blue_img.jpg")
	except Exception as e:
		print(f'{type(e).__name__} : {str(e)}')


def ft_grey(image_arr):
	"""
	Converts array image to grayscale and displays image

	Parameter: 3d image array
	"""
	try:
		red = image_arr[:, :, 0] // 3
		green = image_arr[:, :, 1] // 3
		blue = image_arr[:, :, 2] // 3

		grey = red + green + blue

		image = np.stack([grey, grey, grey], axis=2)
		grey_image = Image.fromarray(image)
		grey_image.save("grey_img.jpg")
	except Exception as e:
		print(f'{type(e).__name__} : {str(e)}')
