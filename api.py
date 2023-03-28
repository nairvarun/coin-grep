from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import subprocess
from lib.btc import BTC
from lib.dash import DASH
from lib.doge import DOGE
from lib.eth import ETH
from lib.usdt import USDT
from lib.xmr import XMR

START_ELECRUM_DAEMON: list = './lightnode/electrum/run_electrum daemon -d'.split()
STOP_ELECRUM_DAEMON: list = './lightnode/electrum/run_electrum stop'.split()

subprocess.run(STOP_ELECRUM_DAEMON)
subprocess.run(START_ELECRUM_DAEMON)

# command to run api:
    # uvicorn api:api --reload
api = FastAPI()
# api.mount("/static", StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory="templates")


@api.options("/")
async def handle_options():
    return {"Allow": "POST"}

@api.get("/check_lightnode")
async def check(a: str, use_api: bool=False) -> str:
    return BTC.validate(a)
    return lightbtc.check_addr(a)

@api.get("/check_fullnode")
async def check(addr: str, use_api: bool=False) -> str:
    if USDT.validate(addr):
        return "usdt"
    elif BTC.validate(addr):
        return "btc" if BTC.validate(addr) else "---"
    elif DASH.validate(addr):
        return "dash" if DASH.validate(addr) else "---"
    elif DOGE.validate(addr):
        return "doge" if DOGE.validate(addr) else "---"
    elif ETH.validate(addr):
        return "eth" if ETH.validate(addr) else "---"
    elif XMR.validate(addr):
        return "xmr" if XMR.validate(addr) else "---"
    else:
        return "---"

@api.get("/get_details")
async def get_details(addr: str, use_api: bool=False) -> dict:
    if USDT.validate(addr):
        return USDT.get_info(addr)
    elif BTC.validate(addr):
        return BTC.get_info(addr)
    if DASH.validate(addr):
        return DASH.get_info(addr)
    elif DOGE.validate(addr):
        return DOGE.get_info(addr)
    elif ETH.validate(addr):
        return ETH.get_info(addr)
    elif XMR.validate(addr):
        return XMR.get_info(addr)
    else:
        return "---"

@api.get("/read_qr")
async def read_qr(qr: str, use_api: bool=False) -> str:
    addr = ""
    if ":" in qr:
        if "?" in qr:
            addr = qr[qr.find(":") + 1 : qr.find("?")]
        else:
            addr = qr[qr.find(":") + 1 : ]
    else:
        addr = qr

    ### could be either check_addr or get_addr_details
    if USDT.validate(addr):
        return "usdt"
    elif BTC.validate(addr):
        return "btc" if BTC.validate(addr) else "---"
    elif DASH.validate(addr):
        return "dash" if DASH.validate(addr) else "---"
    elif DOGE.validate(addr):
        return "doge" if DOGE.validate(addr) else "---"
    elif ETH.validate(addr):
        return "eth" if ETH.validate(addr) else "---"
    elif XMR.validate(addr):
        return "xmr" if XMR.validate(addr) else "---"
    else:
        return "---"


@api.get("/derive")
async def derive_addr(key_type: str, key: str, use_api: bool=False) -> str:
    if key_type == "doge":
        return "doge:" + DOGE.derive(key)
    elif key_type == "btc":
        return "btc:" + BTC.derive(key)
    else:
        return "Invalid Key type"

@api.post("/generate_output")
async def generate_output(input: dict):
    #Retrieve the input string from the request body
    input_str = input["input"]

    #TODO: Write code to generate the output string using your logic here
    output_str = input_str[::-1]

    #Return a JSON response containing the generated output
    return JSONResponse(content={"output": output_str})
