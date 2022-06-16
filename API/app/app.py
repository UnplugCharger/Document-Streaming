## working with fastapi statuses and  handling HTTPExceptions 

from sys import api_version
from fastapi import FastAPI ,status, HTTPException
import uvicorn
import json


### libraries for turning classes into jsons and turning the jsons back to classes

from fastapi.encoders import jsonable_encoder 
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime
from kafka import KafkaProducer , producer


## create a class {schema } for the json that will be coming in 
class InvoiceItem(BaseModel):
    InvoiceNo: int
    StockCode: int
    Description: str
    Quantity: int
    InvoiceDate: str
    UnitPrice : float
    CustomerID: int 
    Country: str

## initiate the fastapi app || this will be used for docker later
app = FastAPI()

## setting UP base URL
@app.get('/')
async def root():
    return {"My Capstone Project":"Starting with FASTAPI AND KAFKA"}




## adding a new Invoice Item 
@app.post("/invoiceitem")
async def post_invoice_item(item:InvoiceItem):# the body awaits invoice item information
    print("message received")
    try:
        #evaluate the timestamp if and format it to a fom you can use
        #date = datetime.strptime(item.InvoiceDate,"%d/%m/%Y  %H:%M")

        date = datetime.strptime(item.InvoiceDate, "%d/%m/%Y %H:%M")

        print("Timestamp available :  ",date)

        ## replace the strange datetime object with new formatted one 
        item.InvoiceDate = date.strftime("%d-%m-%Y %H:%M:%S")



        ##NEW FORMATTED DATE
        print ("New date : ",item.InvoiceDate)


        # parse item back to json
        json_of_item = jsonable_encoder(item)

        ## dump json out as a string 
        json_as_string= json.dumps(json_of_item)

        produce_kafka_string(json_as_string)


        print(json_as_string)

        return JSONResponse(content=json_of_item,status_code=201)


    except ValueError :
        return JSONResponse(content=jsonable_encoder(item),status_code=400)



##Kafka

def produce_kafka_string(json_as_string):
    ## producer 
    producer = KafkaProducer(bootstrap_server='kafka:9092',acks=1)
    ## encode string as bites as required by kafka
    producer.send('ingestion-topic',bytes(json_as_string,'utf-8'),)
    producer.flush()





if __name__=='__main__':
    uvicorn.run(app, host="localhost", port=8000)


