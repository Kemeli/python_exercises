#imports were not allowed to this exercise, so the
#bar is not responsive and it also doens't show the elapsed time

def print_bar(i, total):
	percent = i / total * 100
	length_bar = 50
	filled_bar = int(length_bar * i // total)
	bar = '█' * filled_bar + ' ' * (length_bar - filled_bar)
	print(f'{percent:.0f}%|{bar}| {i}/{total}', end='\r')


def ft_tqdm(lst: range) -> None:
	try:
		assert type(lst) == range, "argument type must be 'range'"
		total = len(lst)
		for i, item in enumerate(lst):
			yield item
			print_bar(i + 1, total)
	except Exception as e:
		print(f'{type(e).__name__} :', e)
	print()
