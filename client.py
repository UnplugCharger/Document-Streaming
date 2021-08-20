## This file pushes the data to the Api
import pandas as pd
import linecache
import json
import requests 

## starting Id and ending Id 
df=pd.read_csv("output/data.csv",nrows=200)

start=1
end = len(df)
i=start

while i <= end :

    line =linecache.getline('output/output.txt',i)

    myjson=json.loads(line)

    print(myjson)

    # Use this for dedbugging
    #print("Status code: ", response.status_code)
    #print("Printing Entire Post Request")
    #print(response.json())


## Increase i
    i=i+1



