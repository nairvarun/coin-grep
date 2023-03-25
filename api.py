from utils import qr
from utils.fullnode import btc, eth, doge, dash, xmr
from utils.lightnode import btc as fullbtc
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import subprocess


START_ELECRUM_DAEMON: list = './utils/lightnode/electrum/run_electrum daemon -d'.split()
STOP_ELECRUM_DAEMON: list = './utils/lightnode/electrum/run_electrum stop'.split()

subprocess.run(STOP_ELECRUM_DAEMON)
subprocess.run(START_ELECRUM_DAEMON)

api = FastAPI()

api.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@api.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@api.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})


@api.options("/")
async def handle_options():
    return {"Allow": "POST"}

@api.post("/generate_output")
async def generate_output(input: dict):
    #Retrieve the input string from the request body
    input_str = input["input"]

    #TODO: Write code to generate the output string using your logic here
    output_str = input_str[::-1]

    #Return a JSON response containing the generated output
    return JSONResponse(content={"output": output_str})

@api.get("/check")
async def check(a: str, use_api: bool=False) -> str:
    return fullbtc.check_addr(a)

@api.get("/read_qr")
async def read_qr(qr: str) -> str:
    return qr.read_qr(qr)
