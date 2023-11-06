from load_image import ft_load
from zoom import zoom_image

def main():
	loaded = ft_load("animal.jpeg")
	print(loaded)
	zoomed = zoom_image(loaded, 400, 400)
	print(zoomed)

if __name__ == "__main__":
	main()
