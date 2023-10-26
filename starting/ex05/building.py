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
	arg = sys.argv[1:]

	if len(arg) > 1:
		print("AssertionError: You should pass only one argument, use quotes.")
		return
	if len(arg) == 0:
		string = input("What is the text to count?\n")
	else:
		string = ' '.join(arg)
	get_values(string)

if "name == __main__":
	main()
