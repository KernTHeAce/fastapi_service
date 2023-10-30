import sys

from fastapi import Request
from fastapi.responses import PlainTextResponse

from . import logger


async def exception_handler(request: Request, exc: Exception) -> PlainTextResponse:
    exception_type, exception_value, _ = sys.exc_info()
    exception_name = getattr(exception_type, "__name__", None)
    logger.error(
        f"{request.method} - path: {request.url.path} - client ip: {request.client.host}"
        f" - status code: 500 - message: Internal Server Error <{exception_name}: {exception_value}>"
    )
    return PlainTextResponse(str(exc), status_code=500)
