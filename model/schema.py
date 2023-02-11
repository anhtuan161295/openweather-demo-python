from pydantic import BaseModel


class GetWeathers(BaseModel):
    cityId: int
    fromDate: str
    toDate: str
    page: int
    size: int


class GetWeathersResponse(BaseModel):
    id: int
    cityId: int
    time: int
    data: str


class CreateWeather(BaseModel):
    cityId: int
    time: int
    data: str


class UpdateWeather(BaseModel):
    id: int = None
    cityId: int
    time: int
    data: str


class DeleteWeather(BaseModel):
    id: int
