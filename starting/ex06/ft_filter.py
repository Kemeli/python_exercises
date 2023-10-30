def ft_filter(func, items):
	"""
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
	"""
	iterator = [item for item in items if func(item)]
	return iterator


# def main():
# 	print(list(ft_filter(all, "hello world!")))
# 	print(ft_filter.__doc__)

# if "name = ft_filter":
# 	main()
