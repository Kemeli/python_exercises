from load_csv import load
from aff_pop import get_graph

def main():
	loaded = load("population_total.csv")
	print(loaded)
	campus = "France"
	other = "Belgium"
	get_graph(loaded, campus, other)


if __name__ == "__main__":
	main()
