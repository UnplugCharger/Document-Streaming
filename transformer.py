import numpy as np
import pandas as pd 

# work with a small portion of data first 
df=pd.read_csv('output/data.csv',nrows=10)

# convert the data into json strings
df['json']=df.to_json(orient='records',lines=True).splitlines()
df=df['json']

print(df)
# print out the dataframe to a file
# Note that the timestamp forward slash will be escaped to stay true to JSON schema

np.savetxt(r'output/output.txt',df.values,fmt='%s')