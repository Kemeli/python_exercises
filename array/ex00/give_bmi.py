import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	np_height = np.array(height)
	np_weight = np.array(weight)

	try:
		assert np_height.size == np_weight.size, \
			'height and weight lists should have the same length'
		np_squared = np.square(np.array(np_height))
		bmi = np.divide(np_weight, np_squared)
	except Exception as e:
		print(f"Error: {str(e)}")
	lst = bmi.tolist()
	return lst


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	np_bmi = np.array(bmi)
	if np_bmi.any():
		bool_arr = np_bmi >= limit
		return bool_arr.tolist()
	else:
		print ("apply_limit(): empty list")
