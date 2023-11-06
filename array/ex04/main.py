from load_image import ft_load
from zoom import zoom_image
from rotate import rotate

def main():
	loaded = ft_load("animal.jpeg")
	zoomed = zoom_image(loaded, 400, 400)
	rotated = rotate(zoomed)
	print(rotated)

if __name__ == "__main__":
	main()
