from os import environ
from fastapi_plugins import RedisSettings


class AppSettings(RedisSettings):
    api_name: str = 'fun_box'



config = AppSettings()
