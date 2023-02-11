from config import config
import aiohttp
import asyncio


openWeatherConfig = config.get_settings()

OPEN_WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"


async def get_today_weather(cityName: str = ""):
    res: str
    apiKey = openWeatherConfig.openweather_api_key
    async with aiohttp.ClientSession() as session:
        params = {'q': cityName, 'appid': apiKey}
        async with session.get(OPEN_WEATHER_API_URL, params=params) as resp:
            res = await resp.text()

    return res
