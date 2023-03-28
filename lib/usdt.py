import json
import re
import os
from lib._cryptocurrency import Cryptocurrency

# TODO: add doc strings
# TODO: add tests
# TODO: add types
# TODO: derive [priv] --> [pub] --> addr (normal and segwit)
# TODO: only import needed methods from imports (??)

class USDT(Cryptocurrency):

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
        return cls.__get_info_from_fullnode(addr)

    @classmethod
    def __validate_by_prefix(cls, addr):
        return any([
            cls.__validate_by_prefix__avalanche(addr),
            cls.__validate_by_prefix__eos(addr),
            cls.__validate_by_prefix__liquid(addr),
            cls.__validate_by_prefix__polygon(addr),
            cls.__validate_by_prefix__tron(addr),
        ])

    @classmethod
    def __validate_by_fullnode(cls, addr):
        return cls.__validate_by_fullnode__omniexplorer(addr)

    @staticmethod
    def __validate_by_fullnode__omniexplorer(addr):
        header = "Content-Type: application/x-www-form-urlencoded"
        url = "https://api.omniexplorer.info/v1/address/addr/"
        command = f'curl -sS -X POST -H "{header}" -H "{header}" -d "addr={addr}" "{url}"'

        stream = os.popen(command)
        output = stream.read()

        r = json.loads(output)
        return not 'error' in r.keys()

    @classmethod
    def __get_info_from_fullnode(cls, addr):
        return cls.__get_info_from_fullnode__omniexplorer(addr)

    @classmethod
    def __get_info_from_fullnode__omniexplorer(cls, addr):
        if cls.validate(addr):
            header = "Content-Type: application/ x-www-form-urlencoded"
            url = "https://api.omniexplorer.info/v1/address/addr/"
            command = f'curl -sS -X POST -H "{header}" -H "{header}" -d "addr={addr}" "{url}"'

            stream = os.popen(command)
            output = stream.read()

            ext_data = json.loads(output)
            trimmed_data = {}
            for data in ext_data['balance']:
                if data['id'] == "31":
                    trimmed_data['amount'] = data['propertyinfo']['amount']
                    trimmed_data['category'] = data['propertyinfo']['category']
                    trimmed_data['fee'] = data['propertyinfo']['fee']
                    trimmed_data['name'] = data['propertyinfo']['name']
                    trimmed_data['totaltokens'] = data['propertyinfo']['totaltokens']
                    trimmed_data['value'] = data['value']
                    trimmed_data['symbol'] = data['symbol']

                    return trimmed_data
            return trimmed_data
        else:
            return {}

    @staticmethod
    def __validate_by_prefix__avalanche(addr):
        c_chain_pattern = r"^0x[0-9a-fA-F]{40}$"
        x_chain_pattern = r"^X-[a-zA-Z0-9]{1,102}$"
        p_chain_pattern = r"^P-[a-zA-Z0-9]+$"  # corrected pattern

        if re.match(c_chain_pattern, addr):
            return True
        elif re.match(x_chain_pattern, addr):
            return True
        elif re.match(p_chain_pattern, addr):
            return True
        else:
            return False

    @staticmethod
    def __validate_by_prefix__polygon(addr):
        polygon_address_pattern = "^0x[a-fA-F0-9]{40}$"

        # Sample string that may contain a Polygon address

        # Find all Polygon addresses in the sample string
        polygon_addresses = re.findall(polygon_address_pattern, addr)

        # Print the results
        if len(polygon_addresses) > 0:
            return(True)

        else:
            return(False)

    @staticmethod
    def __validate_by_prefix__tron(addr):
        if len(addr) != 34 and len(addr)!=42:
            return False
        if not addr.startswith('T'):

            if not addr.startswith('4'):
                return False
        for char in addr:
            if char not in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
                return False
        return True

    @staticmethod
    def __validate_by_prefix__eos(addr):
        if isinstance(addr, str):
            return addr.startswith('EOS') and len(addr) == 53 and all(c in '12345abcdefghijklmnopqrstuvwxyz' for c in addr[3:])
        return False

    @staticmethod
    def __validate_by_prefix__liquid(addr):
        # Check if the address starts with "q" or "Q"
        if not addr.startswith('q') and not addr.startswith('Q'):
            return False

        # Check if the address is a valid Liquid address format
        if not re.match(r'^[qQ][a-zA-Z0-9]{41}$', addr):
            return False

        # If both conditions are true, return True
        return True
