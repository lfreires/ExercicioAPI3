from fastapi import FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse

app = FastAPI()

items = {}


@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(item: dict):
    item_id = len(items)
    items[item_id] = item

    return {
        "item_id": item_id,
        "item": item,
        "status": "created"
    }


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {
            "item_id": item_id,
            "status": "deleted"
        }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Item not found"
    )


@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    if item_id in items:
        items[item_id] = item
        return {
            "item_id": item_id,
            "item": item,
            "status": "updated"
        }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Item not found"
    )


@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id in items:
        return {
            "item_id": item_id,
            "item": items[item_id]
        }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Item not found"
    )


@app.get("/", response_class=HTMLResponse)
def hello_world():
    return "<p>Hello, World!</p>"