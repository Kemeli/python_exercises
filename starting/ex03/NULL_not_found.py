def NULL_not_found(object: any) -> int:
	tp = type(object)
	if (tp == type(None)): #it would be comparing to anything
		print("Nothing: None", tp)
	elif (tp == float):
		print("Cheese: nan", tp)
	elif (tp == int):
		print("Zero: 0", tp)
	elif (tp == str and object == ''):
		print("Empty:", tp)
	elif (tp == bool):
		print("Fake: False", tp)
	else:
		print("Type not found")
		return 1
	return 0
