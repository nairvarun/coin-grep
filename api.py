from utils import qr
from utils.fullnode import btc, eth, doge, dash, xmr, usdt
from utils.static import btc as static_btc, eth as static_eth, doge as static_doge, dash as static_dash, xmr as static_xmr
from utils.lightnode import btc as lightbtc
from utils.derive import btc as derive_btc, doge as derive_doge
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import subprocess


START_ELECRUM_DAEMON: list = './utils/lightnode/electrum/run_electrum daemon -d'.split()
STOP_ELECRUM_DAEMON: list = './utils/lightnode/electrum/run_electrum stop'.split()

subprocess.run(STOP_ELECRUM_DAEMON)
subprocess.run(START_ELECRUM_DAEMON)

# command to run api:
    # uvicorn api:api --reload
api = FastAPI()
api.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@api.options("/")
async def handle_options():
    return {"Allow": "POST"}

@api.get("/check_lightnode")
async def check(a: str, use_api: bool=False) -> str:
    return lightbtc.check_addr(a)

@api.get("/check_fullnode")
async def check(addr: str, use_api: bool=False) -> str:
    if static_btc.is_valid_bitcoin_address(addr):
        return "btc" if btc.check_addr(addr) else "---"
    elif static_dash.is_valid_dash_address(addr):
        return "dash" if dash.check_addr(addr) else "---"
    elif static_doge.is_valid_dogecoin_address(addr):
        return "doge" if doge.check_addr(addr) else "---"
    elif static_eth.is_valid_ethereum_address(addr):
        return "eth" if eth.check_addr(addr) else "---"
    elif static_xmr.is_valid_monero_address(addr):
        return "xmr" if xmr.check_addr(addr) else "---"
    elif usdt.check_addr(addr):
        return "usdt"
    else:
        return "---"

@api.get("/get_details")
async def get_details(addr: str, use_api: bool=False) -> dict:
    if static_btc.is_valid_bitcoin_address(addr):
        return btc.get_addr_details(addr)
    if static_dash.is_valid_dash_address(addr):
        return dash.get_addr_details(addr)
    elif static_doge.is_valid_dogecoin_address(addr):
        return doge.get_addr_details(addr)
    elif static_eth.is_valid_ethereum_address(addr):
        return eth.get_addr_details(addr)
    elif static_xmr.is_valid_monero_address(addr):
        return xmr.get_addr_details(addr)
    elif usdt.check_addr(addr):
        return usdt.get_addr_details(addr)
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
    if usdt.check_addr(addr):
        return "usdt"
    elif static_btc.is_valid_bitcoin_address(addr):
        return "btc" if btc.check_addr(addr) else "---"
    elif static_dash.is_valid_dash_address(addr):
        return "dash" if dash.check_addr(addr) else "---"
    elif static_doge.is_valid_dogecoin_address(addr):
        return "doge" if doge.check_addr(addr) else "---"
    elif static_eth.is_valid_ethereum_address(addr):
        return "eth" if eth.check_addr(addr) else "---"
    elif static_xmr.is_valid_monero_address(addr):
        return "xmr" if xmr.check_addr(addr) else "---"
    else:
        return "---"


@api.get("/derive")
async def derive_addr(key_type: str, key: str, use_api: bool=False) -> str:
    if key_type == "doge":
        return "doge:" + derive_doge.generate_dogecoin_address(key)
    elif key_type == "btc":
        return "btc:" + derive_btc.generate_bitcoin_address(key)
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
