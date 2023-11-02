import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	np_height = np.square(np.array(height))
	np_weight = np.array(weight)

	bmi = np.divide(np_weight, np_height)

	lst = bmi.tolist()
	return lst


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	np_bmi = np.array(bmi)
	bool_arr = np_bmi >= limit
	return bool_arr.tolist()


if "main == __give_bmi__":
	bmi = give_bmi([2.71, 1.15], [165.3, 38.4])
	print(bmi, type(bmi))
	print(apply_limit(bmi, 26))
