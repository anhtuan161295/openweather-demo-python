from sqlalchemy.orm import Session, Query
from model import model, schema
from database import database
import datetime


def get_weathers(req: schema.GetWeathers):
    session: Session = next(database.get_session())

    pageIndex = req.page - 1
    limit = req.size
    offset = pageIndex * limit

    fromDateObj = datetime.datetime.strptime(req.fromDate, "%Y-%m-%d")
    toDateObj = datetime.datetime.strptime(req.toDate, "%Y-%m-%d")
    fromTime = fromDateObj.timestamp()
    toTime = toDateObj.timestamp()

    db_weathers: list[model.Weather] = []
    query: Query[model.Weather]
    if req.cityId == -1:
        query = session.query(model.Weather).filter(model.Weather.time.between(fromTime, toTime)).offset(
            offset=offset).limit(limit=limit)
    else:
        query = session.query(model.Weather).filter_by(city_id=req.cityId).filter(model.Weather.time.between(fromTime, toTime)).offset(
            offset=offset).limit(limit=limit)

    db_weathers = query.all()

    return db_weathers


def create_weather(req: schema.CreateWeather):
    session: Session = next(database.get_session())
    db_weather = model.Weather(
        city_id=req.cityId, time=req.time, data=req.data)
    session.add(db_weather)
    session.commit()
    session.refresh(db_weather)
    return db_weather.id


def update_weather(req: schema.UpdateWeather):
    session: Session = next(database.get_session())
    db_weather = model.Weather(
        id=req.id, city_id=req.cityId, time=req.time, data=req.data)

    session.merge(db_weather)
    session.commit()
    return True


def delete_weather(req: schema.DeleteWeather):
    session: Session = next(database.get_session())
    session.query(model.Weather).filter_by(id=req.id).delete()
    session.commit()
    return True
