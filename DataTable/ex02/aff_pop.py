import matplotlib.pyplot as plt

def population_range(value):
	n = float(value[:-1])
	m70 = 7e7
	if str(value).endswith('M')  and n * 1e6 <= m70:
		return n * 1e6


def get_years(str):
	if int(str) < 2051:
		return int(str)


def get_population(lst):
	new_lst = [population_range(value) for value in lst]
	return new_lst


def to_float(lst):
	new_lst = [float(valor) for valor in lst if valor is not None]
	return new_lst


def plot(years, campus_pop, other_pop, campus, other):
	try:
		plt.figure(figsize=(6, 5))
		plt.plot(years, campus_pop, label=campus)
		plt.plot(years, other_pop, label=other)
	except Exception as e:
		print(f'{type(e).__name__}: {str(e)}')


def	get_axis_ticks(years):
	plt.yticks(ticks=[2e7, 4e7, 6e7], labels=['20M', '40M', '60M'])
	plt.xticks(to_float(years)[::40])
	plt.xlabel("Year")
	plt.ylabel("Population")


def get_graph(data, campus, other):
	try:
		my_campus = data[data['country'] == campus]
		campus_pop = my_campus.values[0][1:]
		other_campus = data[data['country'] == other]
		other_pop = other_campus.values[0][1:]
		years = my_campus.columns[1:]
	except Exception as e:
		print(f'{type(e).__name__}: {str(e)}')
		return

	campus_pop = get_population(campus_pop)
	other_pop = get_population(other_pop)
	years = [get_years(value) for value in years]

	plot(years, campus_pop, other_pop, campus, other)
	get_axis_ticks(years)
	plt.legend()
	plt.savefig("graph.png")
