import sys
from sos import sos

def main():
	args = sys.argv[1:]
	if len(args) != 1:
		print("Pass (only) one argument to the program")
		return
	print(sos(args[0]))


if "name == __main__":
	main()
