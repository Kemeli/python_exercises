from load_csv import load
from projection_life import projection_life

def main():
	income_per_person_data = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
	life_expectancy_data = load("life_expectancy_years.csv")
	projection_life(income_per_person_data, life_expectancy_data)


if __name__ == "__main__":
	main()
