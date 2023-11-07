import pandas as pd

def load(path: str):
	try:
		df = pd.read_csv(path)
		print(f"Loading dataset of dimensions {df.shape}")
		return df
	except Exception as e:
		print(f'{type(e).__name__}: {str(e)}')
