import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
	np_family = np.array(family)
	print(f'My shape is : {np_family.shape}')

	np_new = np_family[start:end]
	print(f'My new shape is : {np_new.shape}')

	return np_new.tolist()
#start a partir de onde começa
#end último
