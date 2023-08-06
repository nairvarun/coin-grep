import ecdsa
import hashlib
import base58
import json
import requests
from lib._cryptocurrency import Cryptocurrency
# from lightnode import is_btc_address

# TODO: add doc strings
# TODO: add tests
# TODO: derive [priv] --> [pub] --> addr (normal and segwit)
# TODO: only import needed methods from imports (??)

class BTC(Cryptocurrency):

    def __init__(self) -> TypeError:
        super().__init__()

    @classmethod
    def get_info(cls, type: str, req: str) -> dict:
        return cls.__get_info_from_fullnode(type, req)

    @classmethod
    def __get_info_from_fullnode(cls, type: str, req: str) -> dict:
        match type:
            case 'addr': return cls.__get_addr_info_from_fullnode__blockcypher(req)
            case 'txn': return cls.__get_txn_info_from_fullnode__blockcypher(req)
            case 'blk': return cls.__get_blk_info_from_fullnode__blockcypher(req)

    @classmethod
    def __get_addr_info_from_fullnode__blockcypher(cls, addr: str) -> bool:
        # bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh
        res = requests.get(f'https://api.blockcypher.com/v1/btc/main/addrs/{addr}')
        return json.loads(res.text)

    @classmethod
    def __get_txn_info_from_fullnode__blockcypher(cls, txn: str) -> bool:
        # Cca7507897abc89628f450e8b1e0c6fca4ec3f7b34cccf55f3f531c659ff4d79
        res = requests.get(f'https://api.blockcypher.com/v1/btc/main/txs/{txn}')
        return json.loads(res.text)

    @classmethod
    def __get_blk_info_from_fullnode__blockcypher(cls, blk: str) -> bool:
        # 0000000013ab9f8ed78b254a429d3d5ad52905362e01bf6c682940337721eb51
        res = requests.get(f'https://api.blockcypher.com/v1/btc/main/blocks/{blk}')
        return json.loads(res.text)
