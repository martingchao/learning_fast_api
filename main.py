# https://www.youtube.com/watch?v=iWS9ogMPOI0

from fastapi import FastAPI, Body

app = FastAPI()
items: list[str] = []

@app.post("/items")
def create_item(item: str = Body(...)):  # agora vem no BODY
    items.append(item)
    return items

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
    item = items[item_id]
    return item