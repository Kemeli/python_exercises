def ft_statistics(*args: any, **kwargs: any) -> None:
	try:
		mean = sum(args) / len(args)
		lst = [i for i in args]
		lst.sort()
		length = len(lst)
		median = lst[length // 2]
		quartile = []
		quartile.append(lst[length // 4])
		quartile.append(lst[length // 4 * 3])
		variance = sum((mean - x) ** 2 for x in lst) / length
		std_deviation = variance ** 0.5
	except Exception as e:
		print('ERROR')
		return

	dict = {"mean": mean, "median": median, "quartile": quartile,
		"std": std_deviation, "var": variance}

	for key in kwargs.values():
		if key in dict.keys():
			print(f'{key}: {dict[key]}')
		else:
			print('ERROR')

