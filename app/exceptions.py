from fastapi import status, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.responses import Response


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    response = Response('Validation Error: {}'.format(exc))
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(response),
    )


async def all_exception_handler(request: Request, exc: Exception):
    response = Response('Something get wrong: {}'.format(exc))
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder(response)
    )
