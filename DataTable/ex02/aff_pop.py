import matplotlib.pyplot as plt
import numpy as np

def get_population(string):
	n = float(string[:-1])
	m20 = 20000000
	m70 = 70000000
	if str(string).endswith('M')  and n * 1e6 <= m70:
		return n * 1e6

def get_years(str):
	if int(str) < 2051:
		return int(str)


def get_graph(data):
	try:
		my_campus = data[data['country'] == 'Brazil'].iloc[:, 1:]
		years = my_campus.columns.astype(int)
		population = my_campus.values.flatten()
		other_campus = data[data['country'] == 'Argentina'].iloc[:, 1:]
		other_population = other_campus.values.flatten()

	except Exception as e:
		print(f'{type(e).__name__}: {str(e)}')
		return

	population = [get_population(value) for value in population]
	other_population = [get_population(value) for value in other_population]
	years = [get_years(value) for value in years]
	um = [float(valor) for valor in population if valor is not None]
	dois = [float(valor) for valor in other_population if valor is not None]

	try:
		plt.figure(figsize=(6, 5))
		plt.plot(years, population)
		plt.plot(years, other_population)
	except Exception as e:
		print(f'{type(e).__name__}: {str(e)}')
		return

	max_pop = (max(max(um), max(dois)))
	yticks = [i * 2e7 for i in range(int(max_pop / 2e7) + 1)]
	plt.yticks(yticks, ["{:,.0f}M".format(pop / 1e6) for pop in yticks])
	plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))

	plt.tight_layout()
	plt.savefig("graph.png")

