import fastapi_plugins
from fastapi import FastAPI
from fastapi import exceptions

from app.handlers import router
from app.exceptions import all_exception_handler, validation_exception_handler
from app.settings import config

app = FastAPI()

app.include_router(router)

app.add_exception_handler(Exception, all_exception_handler)
app.add_exception_handler(exceptions.RequestValidationError, validation_exception_handler)


@app.on_event('startup')
async def on_startup():
    await fastapi_plugins.redis_plugin.init_app(app, config)
    await fastapi_plugins.redis_plugin.init()


@app.on_event('shutdown')
async def on_shutdown():
    await fastapi_plugins.redis_plugin.terminate()
