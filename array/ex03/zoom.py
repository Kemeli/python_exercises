from PIL import Image

def zoom_image(image, new_height, new_width):
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
	x_start = (image.shape[1] - new_width) // 2
	x_end = x_start + new_width
	y_start = (image.shape[0] - new_height) // 2
	y_end = y_start + new_height

	zoomed_img = image[y_start:y_end, x_start:x_end]
	zoomed_h = zoomed_img.shape[0]
	zoomed_w = zoomed_img.shape[1]

	print(f"New shape after slicing: ({zoomed_h}, {zoomed_w}, or {zoomed_img.shape}")

	zoomed_img_pil = Image.fromarray(zoomed_img)
	zoomed_img_pil.save("zoomed_img.jpeg")
	return zoomed_img
