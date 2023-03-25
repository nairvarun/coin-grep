import json
from requests import get

def check_addr(addr: str) -> bool:
    return _check_from_blockcypher(addr)

def _check_from_cryptoid(addr: str) -> bool:
    res = get(f'https://btc.cryptoid.info/btc/api.dws?q=addressinfo&a={addr}')
    return True if res.text != "null" else False

def _check_from_blockcypher(addr: str) -> bool:
    res = get(f'https://api.blockcypher.com/v1/btc/main/addrs/{addr}/balance')
    return True if 'error' not in json.loads(res.text) else False
