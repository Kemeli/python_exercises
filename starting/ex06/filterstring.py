from ft_filter import ft_filter

def no_punctuation(string):
	punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
	for char in string:
		if char in punctuation:
			return False
	return True

def filter_string(S, N):
	validate_size = lambda word : len(word) > N
	substr = list(ft_filter(validate_size, S.split()))
	print(list(ft_filter(no_punctuation, substr)))
