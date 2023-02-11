from fastapi import APIRouter, Request
from database import weather as db
from model import schema
from service import openweather
import json

# APIRouter creates path operations for weather module
router = APIRouter(
    prefix="/api/weather",
    tags=["Weather"],
    responses={404: {
        "code": 404,
        "message": "Not found"
    }},
)


@router.get("/search-today-weather")
async def create_weather_record(cityName: str):

    dataStr = await openweather.get_today_weather(cityName)
    data = json.loads(dataStr)
    if data['cod'] != 200:
        return {"code": 404, "message": data['message']}

    return {"code": 200, "message": "OK", "data": data}


@router.get("/records")
async def create_weather_record(request: Request, cityId: int = -1, page: int = 1, size: int = 10):
    fromDate = request.query_params.get("from")
    toDate = request.query_params.get("to")

    body = schema.GetWeathers(
        cityId=cityId, fromDate=fromDate, toDate=toDate, page=page, size=size)
    data = db.get_weathers(body)

    # convert keys from snake case to camel case
    convertedData: list[schema.GetWeathersResponse] = []
    for i in range(len(data)):
        item = data[i]
        convertedData.append(schema.GetWeathersResponse(
            id=item.id, cityId=item.city_id, time=item.time, data=item.data))

    return {"code": 200, "message": "OK", "data": convertedData}


@router.post("/record")
async def create_weather_record(body: schema.CreateWeather):
    db.create_weather(body)
    return {"code": 200, "message": "OK"}


@router.put("/record/{id}")
async def update_weather_record(id: int, body: schema.UpdateWeather):
    body.id = id
    db.update_weather(body)
    return {"code": 200, "message": "OK"}


@router.delete("/record/{id}")
async def delete_weather_record(id: int):
    body = schema.DeleteWeather(id=id)
    db.delete_weather(body)
    return {"code": 200, "message": "OK"}
