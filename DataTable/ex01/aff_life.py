import matplotlib.pyplot as plt

def get_graph(df):
	try:
		campus_data = df[df['country'] == 'Brazil']
		years = campus_data.columns[1:]
		life_expectancy = campus_data.values[0][1:]
	except Exception as e:
		print(f'{type(e).__name__}: {str(e)}')
		return

	plt.figure(figsize=(10, 6))
	plt.plot(years, life_expectancy)
	plt.title('Brazil Life Expectancy projections')
	plt.xlabel('Year')
	plt.xticks(years[::40])
	plt.ylabel('Life Expectancy')
	plt.tight_layout()
	plt.savefig("graph.png")
