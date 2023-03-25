import subprocess

def check_addr(addr):
    VALIDATE_ADDRESS: list = f'./utils/lightnode/electrum/run_electrum validateaddress {addr}'.split()
    res = subprocess.check_output(VALIDATE_ADDRESS)
    return res.decode().rstrip('\n') == "true"
