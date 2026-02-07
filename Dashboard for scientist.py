import numpy as np
import pandas as pd

Diabetes_df = pd.read_csv("diabetes copy.csv")
print(f" The first five entries are: {Diabetes_df.head()}")
print(f"Number of Rows: {Diabetes_df.shape[0]}")
print(f"Number of Columns: {Diabetes_df.shape[1]}")
print(f"Overall Shape: {Diabetes_df.shape}")
