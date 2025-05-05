from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from tinydb import TinyDB

app = FastAPI()
db = TinyDB("db.json")

templates = Jinja2Templates(directory="templates")

class Item(BaseModel):
    item: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    items = db.all()
    return templates.TemplateResponse("index.html", {"request": request, "items": items})

@app.post("/add")
async def add_item(item: Item):
    db.insert({"item": item.item})
    return JSONResponse({"status": "success"})
