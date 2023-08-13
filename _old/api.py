from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from lib.btc import BTC

# command to run api:
    # uvicorn api:api --reload
api = FastAPI()
# api.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@api.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@api.get("/get_details/{req}", response_class=HTMLResponse)
async def read_item(request: Request, req: str):
    res = BTC.get_info(req)
    return templates.TemplateResponse("item.html", {"request": request, "req": req, "res": res})

@api.get("/txn/{req}", response_class=HTMLResponse)
async def read_item(request: Request, req: str):
    res = BTC.get_info('txn', req)
    return templates.TemplateResponse("item.html", {"request": request, "req": req, "res": res})

@api.get("/addr/{req}", response_class=HTMLResponse)
async def read_item(request: Request, req: str):
    res = BTC.get_info('addr', req)
    return templates.TemplateResponse("item.html", {"request": request, "req": req, "res": res})

@api.get("/blk/{req}", response_class=HTMLResponse)
async def read_item(request: Request, req: str):
    res = BTC.get_info('blk', req)
    return templates.TemplateResponse("item.html", {"request": request, "req": req, "res": res})
