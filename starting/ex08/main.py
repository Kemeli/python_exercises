from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

elements = ft_tqdm(1)
for elem in elements:
	sleep(0.005)
print()

elements = tqdm(range(333))
for elem in elements:
	sleep(0.005)
print()
