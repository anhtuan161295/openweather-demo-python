from fastapi import FastAPI
from api import router as api_router
from config import config
import uvicorn

app = FastAPI()

app.include_router(api_router)

# print database config
dbConfig = config.get_settings()
print('Database Url: ', dbConfig.database_url)
print('Database Port: ', dbConfig.database_port)
print('Database Username: ', dbConfig.database_username)
print('Database Password: ', dbConfig.database_password)
print('Database Name: ', dbConfig.database_name)


# change application port
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
