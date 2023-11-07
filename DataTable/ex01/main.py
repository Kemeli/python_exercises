from load_csv import load
from aff_life import get_graph

def main():
	loaded = load("life_expectancy_years.csv")
	print(loaded)
	get_graph(loaded)


if __name__ == "__main__":
	main()
