import sys

"""
gets arguments from the command line
checks if it is one valid number
prints information about the number
*tries to not create any function
"""

var = sys.argv[1:] #gets argv from second argument on
size = len(var)

if size != 0:
	if size > 1:
		print("AssertionError: more than one argument is provided")
	else:
		try:
			num = int(var[0])
			if int(num) % 2 == 0:
				print ("I'm Even.")
			if int(num) % 2 != 0:
				print ("I'm Odd.")
		except ValueError:
			print("AssertionError: argument is not an integer")
