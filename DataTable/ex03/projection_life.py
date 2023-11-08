import matplotlib.pyplot as plt

def projection_life(income_data, life_expectancy_data):
	year = '1900'
	income = income_data[year] #o primerio é coluna aqui
	life_expectancy = life_expectancy_data[year]

	plt.scatter(income, life_expectancy)
	plt.title(year)
	plt.xlabel('Gross domestic product')
	plt.ylabel('Life Expectancy')
	plt.xscale("log")
	plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
	plt.savefig('graph.png')
