import sys
from filterstring import filter_string

def main():
	args = sys.argv[1:]
	if len(args) != 2:
		print ("AssertionError: two arguments are required")
		return
	try:
		S = str(args[0])
		N = int(args[1])
	except ValueError:
		print ("AssertionError: first argument should be a string and",
			"second argument should be an integer")
		return

	filter_string(S, N)


if "name == __main__":
	main()
