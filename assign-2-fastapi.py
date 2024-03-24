from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population


cities = []


class CityInput(BaseModel):
    name: str
    population: int


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.put("/city/")
def add_city(city_input: CityInput):
    city = City(name=city_input.name, population=city_input.population)
    cities.append(city)
    return {"message": "City added successfully"}


@app.get("/cities/")
def get_cities():
    return cities
