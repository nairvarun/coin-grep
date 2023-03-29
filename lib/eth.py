import re
import requests
import json
from lib._cryptocurrency import Cryptocurrency

# TODO: add doc strings
# TODO: add tests
# TODO: add types
# TODO: derive [priv] --> [pub] --> addr (normal and segwit)
# TODO: only import needed methods from imports (??)

class ETH(Cryptocurrency):

    def __init__(self) -> TypeError:
        super().__init__()

    # add doc str and test and types
    @classmethod
    def derive(cls, key: str) -> dict:
        pass

    @classmethod
    def validate(cls, addr: str) -> bool:
        return cls.__validate_by_prefix(addr)
        return cls.__validate_by_fullnode(addr)

    @classmethod
    def get_info(cls, addr: str) -> dict:
        return cls.__get_info_from_fullnode(addr)

    @staticmethod
    def __validate_by_prefix(addr: str) -> bool:
        if not re.match(r'^(0x)?[0-9a-fA-F]{40}$', addr):
            return False
        elif re.match(r'^(0x)?[0-9a-fA-F]{40}$', addr) or re.match(r'^(0x)?[0-9A-Fa-f]{40}$', addr):
            return (True)
        else:
            return False

    @classmethod
    def __validate_by_fullnode(cls, addr: str) -> bool:
        return cls.__validate_by_fullnode__blockcypher(addr)

    @staticmethod
    def __validate_by_fullnode__blockcypher(addr: str) -> bool:
        res = requests.get(f'https://api.blockcypher.com/v1/eth/main/addrs/{addr}/balance')
        return True if 'error' not in json.loads(res.text) else False

    @classmethod
    def __get_info_from_fullnode(cls, addr: str) -> dict:
        return cls.__get_info_from_fullnode__blockcypher(addr)

    @classmethod
    def __get_info_from_fullnode__blockcypher(cls, addr: str) -> dict:
        if cls.validate(addr):
            res = requests.get(f'https://api.blockcypher.com/v1/eth/main/addrs/{addr}/balance')
            return json.loads(res.text)
        else:
            return {}
