# 888tNkZrPN6JsEgekjMnABU4TBzc2Dt29EPAvkRxbANsAnjyPbb3iQ1YBRk1UXcdRsiKc9dhwMVgN5S9cQUiyoogDavup3H
import json
from requests import get

def check_addr(addr: str) -> bool:
    return _check_from_moneroexplorer(addr)

def _check_from_xmrchain(addr: str) -> bool:
    res = get(f'https://xmrchain.net/search?value={addr}')
    bad_addr_msg: int = res.text.find('Cant parse address (probably incorrect format)')
    bad_format_msg: int = res.text.find('Nothing in the blockchain has been found that matches the search term :-(')
    return True if bad_addr_msg == bad_format_msg else False

def _check_from_moneroexplorer(addr: str) -> bool:
    res = get(f'https://moneroexplorer.org/search?value={addr}')
    bad_addr_msg: int = res.text.find('Cant parse address (probably incorrect format)')
    bad_format_msg: int = res.text.find('Nothing in the blockchain has been found that matches the search term :-(')
    return True if bad_addr_msg == bad_format_msg else False


def test__check_from_xmrchain():
    # 1
    res = _check_from_xmrchain('888tNkZrPN6JsEgekjMnABU4TBzc2Dt29EPAvkRxbANsAnjyPbb3iQ1YBRk1UXcdRsiKc9dhwMVgN5S9cQUiyoogDavup3H')
    assert res == True

    # 2
    res = _check_from_xmrchain('888tNkZrPN6JsEgekjMnABU4TBzc2Dt29EPAvkRxbANsAnjyPbb3iQ1YBRk1UXcdRsiKc9dhwMVgN5S9cQUiyoogDavup3h')
    assert res == False

    # 3
    res = _check_from_xmrchain('appls')
    assert res == False

def test__check_from_moneroexplorer():
    # 1
    res = _check_from_moneroexplorer('888tNkZrPN6JsEgekjMnABU4TBzc2Dt29EPAvkRxbANsAnjyPbb3iQ1YBRk1UXcdRsiKc9dhwMVgN5S9cQUiyoogDavup3H')
    assert res == True

    # 2
    res = _check_from_moneroexplorer('888tNkZrPN6JsEgekjMnABU4TBzc2Dt29EPAvkRxbANsAnjyPbb3iQ1YBRk1UXcdRsiKc9dhwMVgN5S9cQUiyoogDavup3h')
    assert res == False

    # 3
    res = _check_from_moneroexplorer('appls')
    assert res == False
