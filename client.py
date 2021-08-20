## This file pushes the data to the Api
import pandas as pd
import linecache
import json
import requests 

## starting Id and ending Id 
df=pd.read_csv("output/data.csv",nrows=5)

start=1
end = 4  #len(df)
i=start

while i <= end :

    line =linecache.getline('output/output.txt',i)

    print(line)
## Increase i
    i=i+1



