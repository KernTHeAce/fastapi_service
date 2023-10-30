import logging

from src import LOGS_PATH

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler(LOGS_PATH)
formatter = logging.Formatter("%(levelname)s:\t  %(asctime)s - %(message)s", datefmt="[%d-%b-%y %H:%M:%S]")
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logger.handlers = [stream_handler, file_handler]
logger.setLevel(logging.DEBUG)

uvicorn_acess = logging.getLogger("uvicorn.access")
uvicorn_acess.disabled = True
