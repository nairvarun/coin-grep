import subprocess

def check_addr(addr: str) -> bool:
    return _check_from_electrum(addr)

def _check_from_electrum(addr: str) -> bool:
    VALIDATE_ADDRESS: list = f'./utils/lightnode/electrum/run_electrum validateaddress {addr}'.split()
    res = subprocess.check_output(VALIDATE_ADDRESS)
    return res.decode().rstrip('\n') == "true"


def test___check_from_electrum():
    # 1
    res = _check_from_electrum('3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5')
    assert res == True

    # 2
    res = _check_from_electrum('3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc6 ')
    assert res == False
