import json
from requests import get

def check_addr(addr: str) -> bool:
    return _check_from_blockcypher(addr)

def _check_from_blockcypher(addr: str) -> bool:
    res = get(f'https://api.blockcypher.com/v1/eth/main/addrs/{addr}/balance')
    return True if 'error' not in json.loads(res.text) else False


def test__check_from_blockcypher():
    # 1
    res = _check_from_blockcypher('fbcbfb55662a8f34231bcdac39873f01dc036131')
    assert res == True

    # 2
    res = _check_from_blockcypher('fbcbfb55662a8f34231bcdac39873f01dc0361311')
    assert res == False

def get_addr_details(addr: str) -> dict:
    return _get_from_blockcypher(addr)
    

def _get_from_blockcypher(addr: str) -> dict:
    if check_addr(addr):
        res = get(f'https://api.blockcypher.com/v1/eth/main/addrs/{addr}/balance')
        return json.loads(res.text)
    else:
        return {}

def test__get_addr_details_blockcypher():
    # 1
    details = get_addr_details('fbcbfb55662a8f34231bcdac39873f01dc036131')
    assert (not details) == False

    # 2
    details = get_addr_details('fbcbfb55662a8f34231bcdac39873f01dc0361311')
    assert (not details) == True