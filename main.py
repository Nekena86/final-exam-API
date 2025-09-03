import code
from tokenize import String

from fastapi import FastAPI
from pydantic import BaseModel

from starlette.responses import JSONResponse

app = FastAPI()

list:object = []

class Characteristic:
    max_speed:int
    max_fuel_capacity:int

@app.get("/ping")
def ping():
    return {"message": "pong"}

object (BaseModel)
  id:String
  brand:String
  model:String
  characteristique:Characteristic


@app.post("/cars")
def cars():
    return {}

@app.get("/cars")
def read_car():
    return {object}

@app.get("/cars/{id}")
def read_car(id:String):
    if id in list:
        return {JSONResponse(object)}
    else:
        return {JSONResponse("id fourni n'existe pas ou n'a pas ete trouve",status_code=404)}


@app.put("/cars/{id}/characteristics")
def update_characteristics(max_speed:int,max_fuel_capacity:int,id:String):
    if id in list:
        object.max_speed = max_speed
        object.max_fuel_capacity = max_fuel_capacity
        return {JSONResponse(object )}
    else:
        return {JSONResponse("id fourni n'existe pas ou n'a pas ete trouve",status_code=404)}




