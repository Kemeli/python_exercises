import pandas as pd

def load(path: str):
	df = pd.read_csv(path)
	print(f"Loading dataset of dimensions {df.shape}")
	print(df)

