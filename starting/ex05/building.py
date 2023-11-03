import sys

def punctuation(string):
	punctuation_list = []
	punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
	for char in string:
		if char in punctuation:
			punctuation_list.append(char)
	return punctuation_list


def get_values(string):
	print("The text contains", len(string), "characters:")
	print(sum(1 for c in string if c.isupper()), "upper letters")
	print(sum(1 for c in string if c.islower()), "lower letters")

	punctuation_list = punctuation(string)
	print(len(punctuation_list), "punctuation marks")

	print(sum(1 for c in string if c.isspace()), "spaces")
	print(sum(1 for c in string if c.isdigit()), "digits")


def main():
	arg = sys.argv
	string = arg[1:]
	try:
		if len(arg) > 2:
			raise AssertionError ("You must pass only one argument, use quotes.")
		try:
			while (len(string) == 0):
				string = input("What is the text to count?\n")
			get_values(string)
		except KeyboardInterrupt:
			print ('')
	except Exception as e:
		print(f'{type(e).__name__}', e)


if "name == __main__":
	main()
