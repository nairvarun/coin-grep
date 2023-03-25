import json
from requests import get

def check_addr(addr: str) -> bool:
    return _check_from_blockcypher(addr)

def _check_from_blockcypher(addr: str) -> bool:
    res = get(f'https://api.blockcypher.com/v1/doge/main/addrs/{addr}/balance')
    return True if 'error' not in json.loads(res.text) else False


def test__check_from_blockcypher():
    # 1
    res = _check_from_blockcypher('DQ2Z7QGwL8AcRH6Y7VdZfX35wfWqEzEA4a')
    assert res == True

    # 2
    res = _check_from_blockcypher('DQ2Z7QGwL8AcRH6Y7VdZfX35wfWqEzEA4A')
    assert res == False
