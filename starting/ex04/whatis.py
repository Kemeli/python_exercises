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
	try:
		if size > 1:
			raise AssertionError("more than one argument is provided")
		try:
			num = int(var[0])
		except:
			raise AssertionError("argument is not an integer")
	except Exception as e:
		print(f"{type(e).__name__}: {e}")
	else:
		if int(num) % 2 == 0:
			print ("I'm Even.")
		else:
			print ("I'm Odd.")
