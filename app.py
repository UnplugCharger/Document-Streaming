## working with fastapi statuses and  handling HTTPExceptions 

from fastapi import FastAPI ,status, HTTPException
import json


### libraries for turning classes into jsons and turning the jsons back to classes

from fastapi.encoders import jsonable_encoder 
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime
from kafka import KafkaProducer , producer


## create a class {schema } for the json that will be coming in 
class InvoiceItem(BaseModel):
    InvoiceNumber: int
    StockCode: str
    Description: str
    Quantity: int
    InvoiceDate: str
    UnitPrice : str 
    CustomerID: int 
    Country: str

## initiate the fastapi app || this will be used for docker later
app = FastAPI()
