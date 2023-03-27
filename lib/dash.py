from _cryptocurrency import Cryptocurrency
import requests
import json
import re

# TODO: add doc strings
# TODO: add tests
# TODO: add types
# TODO: derive [priv] --> [pub] --> addr (normal and segwit)
# TODO: only import needed methods from imports (??)

class DASH(Cryptocurrency):

    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def derive(cls, key):
        pass

    @classmethod
    def validate(cls, addr):
        return cls.__validate_by_prefix(addr)
        return cls.__validate_by_fullnode(addr)

    @classmethod
    def get_info(cls, addr):
        return cls.__get_info_from_fullnode()

    @staticmethod
    def __validate_by_prefix(addr):
        """
        Validates a Dash address using a regular expression.
        Returns True if the address is valid, and False otherwise.
        """
        # The regular expression for a Dash address
        pattern = re.compile("^(X|8)[a-km-zA-HJ-NP-Z0-9]{33}$")

        # Check if the address matches the pattern
        if pattern.match(addr):
            return True
        else:
            return False

    @classmethod
    def __validate_by_fullnode(cls, addr):
        return cls.__validate_by_fullnode__blockcypher(addr)

    @staticmethod
    def __validate_by_fullnode__blockcypher(addr):
        res = requests.get(f'https://api.blockcypher.com/v1/dash/main/addrs/{addr}/balance')
        return True if 'error' not in json.loads(res.text) else False

    @classmethod
    def __get_info_from_fullnode(cls, addr):
        return cls.__get_info_from_fullnode__blockcypher(addr)

    @classmethod
    def __get_info_from_fullnode__blockcypher(cls, addr):
        if cls.validate(addr):
            res = requests.get(f'https://api.blockcypher.com/v1/dash/main/addrs/{addr}/balance')
            return json.loads(res.text)
        else:
            return {}