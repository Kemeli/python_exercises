def ft_statistics(*args: any, **kwargs: any) -> None:
	if len(args) == 0:
		for i in kwargs:
			print ("ERROR")
		return
	try:
		mean = sum(args) / len(args)
		lst = [i for i in args]
		lst.sort()
		median = lst[len(lst) // 2]
		quartile = []
		quartile.append(lst[len(lst) // 4])
		quartile.append(lst[len(lst) // 4 * 3])
		variance = sum((mean - x) ** 2 for x in lst) / len(lst)
		std_deviation = variance ** 0.5
	except Exception as e:
		print(f'{type(e).__name__}: {e}')
		return

	dict = {"mean": mean, "median": median, "quartile": quartile,
		"std": std_deviation, "var": variance}

	for key in kwargs.values():
		if key in dict.keys():
			print(f'{key}: {dict[key]}')
