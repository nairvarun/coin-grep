from _cryptocurrency import Cryptocurrency
import ecdsa
import hashlib
import base58
import json
import requests

# TODO: add doc strings
# TODO: add tests
# TODO: add types
# TODO: derive [priv] --> [pub] --> addr (normal and segwit)
# TODO: only import needed methods from imports (??)

class XMR(Cryptocurrency):

    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def derive(cls, key):
        pass

    # TODO: handle all 3 in one method
    @classmethod
    def validate(cls, addr):
        return cls.__validate_by_prefix(addr)
        return cls.__validate_by_fullnode(addr)

    @classmethod
    def get_info(cls, addr):
        pass

    @staticmethod
    def __validate_by_prefix(addr):
        if(addr[0]=='4' and len(addr)==95) or (addr[0]=='8' and len(addr)==106)or((addr[0]in['4','8'])and len(addr)==64):
            return(True)
        else:
            return(False)

    @classmethod
    def __validate_by_fullnode(cls, addr):
        return cls.__validate_by_fullnode__xmrchain(addr)
        return cls.__validate_by_fullnode__moneroexplorer(addr)

    @staticmethod
    def __validate_by_fullnode__xmrchain(addr):
        res = requests.get(f'https://xmrchain.net/search?value={addr}')
        bad_addr_msg: int = res.text.find('Cant parse address (probably incorrect format)')
        bad_format_msg: int = res.text.find('Nothing in the blockchain has been found that matches the search term :-(')
        return True if bad_addr_msg == bad_format_msg else False

    @staticmethod
    def __validate_by_fullnode__moneroexplorer(addr):
        res = requests.get(f'https://moneroexplorer.org/search?value={addr}')
        bad_addr_msg: int = res.text.find('Cant parse address (probably incorrect format)')
        bad_format_msg: int = res.text.find('Nothing in the blockchain has been found that matches the search term :-(')
        return True if bad_addr_msg == bad_format_msg else False
