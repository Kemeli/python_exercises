from load_csv import load
from aff_pop import get_graph

def main():
	loaded = load("population_total.csv")
	# print(loaded)
	get_graph(loaded)


if __name__ == "__main__":
	main()
