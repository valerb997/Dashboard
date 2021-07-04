import pandas as pd
import pathlib

df=pd.read_csv("life_expect.csv")
dff=pd.DataFrame
x,y = 103, 59
l=[x,y]
data = {'x' : x, 'y' : y}
dff=pd.DataFrame(data, index=[0])  # the `index` argument is important
df["x"]=dff["x"]
df["y"]=dff["y"]
df.to_csv("life_expect_new.csv")