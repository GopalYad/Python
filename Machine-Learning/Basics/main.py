import numpy as np
import pandas as pd
cols =["fLength","fWidth","fSize","fConc","fConc1","fAsym","fm3Long","fM3Trans","fAlpha","fDist","fClass"]
 
df = pd.read_csv(r"C:\Users\gopal\OneDrive\Desktop\ML\magic04.data",names=cols)

# print(df.head())
df["fClass"].unique()
print(df.head())


