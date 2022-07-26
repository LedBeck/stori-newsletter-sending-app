from typing import Union
from dotenv import dotenv_values
from fastapi import FastAPI

from db import create_connection, getRecipients

configEnv = dotenv_values(".env")
conn = create_connection(configEnv["SQLITE_DB"])

app = FastAPI()


@app.get("/")
def read_root():
    return getRecipients(conn)


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}