import subprocess
import json

def check_addr(addr: str) -> bool:
    return _validate_addr_electrum(addr)

def get_addr_info(addr: str) -> dict:
    res: dict = {}
    res['balance']: dict | None = _get_addr_bal_electrum(addr)
    res['unspent']: list[dict] | None = _get_addr_unspent_electrum(addr)
    res['history']: list[dict] | None = _get_addr_hist_electrum(addr)
    return res


# validateaddress
def _validate_addr_electrum(addr: str) -> bool:
    VALIDATE_ADDRESS: list = f'./utils/lightnode/electrum/run_electrum validateaddress {addr}'.split()
    res = subprocess.check_output(VALIDATE_ADDRESS)
    return res.decode().rstrip('\n') == "true"

# getaddressbalance
def _get_addr_bal_electrum(addr: str) -> dict | None:
    if _validate_addr_electrum(addr) == False:
        return None
    GET_ADDRESS_BALANCE: list = f'./utils/lightnode/electrum/run_electrum getaddressbalance {addr}'.split()
    res = subprocess.check_output(GET_ADDRESS_BALANCE)
    addr_balance: dict = json.loads(res.decode())
    return addr_balance

# getaddressunspent
def _get_addr_unspent_electrum(addr: str) -> list[dict] | None:
    if _validate_addr_electrum(addr) == False:
        return None
    GET_ADDRESS_UNSPENT: list = f'./utils/lightnode/electrum/run_electrum getaddresshistory {addr}'.split()
    res = subprocess.check_output(GET_ADDRESS_UNSPENT)
    addr_unspent: list[dict] = json.loads(res.decode())
    return addr_unspent

# getaddresshistory
def _get_addr_hist_electrum(addr: str) -> list[dict] | None:
    if _validate_addr_electrum(addr) == False:
        return None
    GET_ADDRESS_HISTORY: list = f'./utils/lightnode/electrum/run_electrum getaddresshistory {addr}'.split()
    res = subprocess.check_output(GET_ADDRESS_HISTORY)
    addr_history: list[dict] = json.loads(res.decode())
    return addr_history


### tests

def test_check_addr():
    # 1
    res = check_addr('3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5')
    assert res == True

    # 2
    res = check_addr('3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc53')
    assert res == False

def test_get_addr_info():
    # 1
    res = get_addr_info('3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5')
    assert isinstance(res, dict)
    assert 'balance' in res
    assert 'unspent' in res
    assert 'history' in res
    assert isinstance(res['balance'], dict)
    assert isinstance(res['unspent'], list)
    assert isinstance(res['history'], list)
    assert isinstance(res['unspent'][0], dict)
    assert isinstance(res['history'][0], dict)

    # 2
    res = get_addr_info('3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc53')
    assert isinstance(res, dict)
    assert 'balance' in res
    assert 'unspent' in res
    assert 'history' in res
    assert res['balance'] is None
    assert res['unspent'] is None
    assert res['history'] is None


def test___validate_addr_electrum():
    # 1
    res = _validate_addr_electrum('3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5')
    assert res == True

    # 2
    res = _validate_addr_electrum('3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc6')
    assert res == False

def test__get_addr_bal_electrum():
    # 1
    res = _get_addr_bal_electrum('3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5')
    assert isinstance(res, dict)
    assert 'confirmed' in res
    assert 'unconfirmed' in res

    # 2
    res = _get_addr_bal_electrum('3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc53')
    assert res is None

def test__get_addr_hist_electrum():
    # 1
    res = _get_addr_hist_electrum('3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5')
    assert isinstance(res, list)
    assert isinstance(res[0], dict)
    assert 'height' in res[0]
    assert 'tx_hash' in res[0]

    # 2
    res = _get_addr_hist_electrum('3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc53')
    assert res is None

def test__get_addr_unspent_electrum():
    # 1
    res = _get_addr_unspent_electrum('3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5')
    assert isinstance(res, list)
    assert isinstance(res[0], dict)
    assert 'height' in res[0]
    assert 'tx_hash' in res[0]

    # 2
    res = _get_addr_unspent_electrum('3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc53')
    assert res is None
