from starlette.middleware.base import BaseHTTPMiddleware

from src.logger import logger


class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        logger.info(
            f"{request.method} - path: {request.url.path} - client ip: {request.client.host}"
            f" - status code: {response.status_code}"
        )
        return response
