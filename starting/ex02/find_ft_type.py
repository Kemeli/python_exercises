def all_thing_is_obj(object: any) -> int:
	tp = type(object)
	if (tp == list):
		print("List :", tp)
	elif (tp == tuple):
		print("Tuple :", tp)
	elif (tp == set):
		print("Set :", tp)
	elif (tp == dict):
		print("Dict :", tp)
	elif (tp == str):
		print("Brian is in the kitchen :", tp)
	else:
		print("Type not found")
	return 42
