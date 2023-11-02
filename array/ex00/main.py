from give_bmi import give_bmi, apply_limit

if "main == __give_bmi__":
	bmi = give_bmi([2.71, 1.15], [165.3, 38.4])
	print(bmi, type(bmi))
	print(apply_limit(bmi, 26))
