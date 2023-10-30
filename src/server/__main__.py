import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from src.logger import LogMiddleware, exception_handler, logger

app = FastAPI()
app.add_middleware(LogMiddleware)
app.add_exception_handler(Exception, exception_handler)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def items(item_id: int):
    data = {
        0: "item_0",
        1: "item_1",
        2: "item_2",
        3: "item_3",
    }

    try:
        return {"item": data[item_id]}
    except KeyError:
        logger.error(f"Calling a non-existent entity. There is no item with such id: '{item_id}'")
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"message": f"there is no item with such id: '{item_id}'"},
        )


if __name__ == "__main__":
    uvicorn.run(app)
