from PIL import Image

def zoom_image(image, height, width):
	"""
	receives an array representing an image, creates the zoomed image and returns
	the zoomed image array

	Parameters:
	image: (array) the image in array format
	new_height: (int) the new height to the image
	new width: (int) the new width to the image

	Calculates the new starting an ending points based on the center of the image;
	Zooms the array  and prints it's new shape;
	Transforms the array to a zoomed image, saves it and returns the new image
	in array format
	"""

	try:
		assert height > 0 and width > 0, 'new sizes must be bigger than zero'
		x_start = (image.shape[1] - width) // 2
		x_end = x_start + width
		y_start = (image.shape[0] - height) // 2
		y_end = y_start + height
	except Exception as e:
		print(f'{type(e).__name__}: {str(e)}')

	zoomed_img = image[y_start:y_end, x_start:x_end]
	zoomed_h = zoomed_img.shape[0]
	zoomed_w = zoomed_img.shape[1]

	print(f"New shape after slicing: ({zoomed_h}, {zoomed_w}, or {zoomed_img.shape}")

	zoomed_img_pil = Image.fromarray(zoomed_img)
	zoomed_img_pil.save("zoomed_img.jpeg")
	return zoomed_img
