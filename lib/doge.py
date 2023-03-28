import ecdsa
import hashlib
import base58
import re
import requests
import json
from lib._cryptocurrency import Cryptocurrency

# TODO: add doc strings
# TODO: add tests
# TODO: add types
# TODO: derive [priv] --> [pub] --> addr (normal and segwit)
# TODO: only import needed methods from imports (??)

class DOGE(Cryptocurrency):

    def __init__(self) -> None:
        super().__init__()

    # add doc str and test and types
    @classmethod
    def derive(cls, key):
        private_key = key
        # Step 1: Generate the private key object from the input string
        private_key_bytes = bytes.fromhex(private_key)
        curve = ecdsa.SECP256k1
        sk = ecdsa.SigningKey.from_string(private_key_bytes, curve=curve)

        # Step 2: Derive the public key
        vk = sk.get_verifying_key()

        # Step 3: Generate the hash
        public_key_bytes = vk.to_string('compressed')
        sha256_hash = hashlib.sha256(public_key_bytes).digest()
        ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()

        # Step 4: Add the network byte
        network_byte = b'\x1e'
        hash_with_network_byte = network_byte + ripemd160_hash

        # Step 5: Generate the checksum
        first_hash = hashlib.sha256(hash_with_network_byte).digest()
        second_hash = hashlib.sha256(first_hash).digest()
        checksum = second_hash[:4]

        # Step 6: Create the address
        address_bytes = hash_with_network_byte + checksum
        dogecoin_address = base58.b58encode(address_bytes).decode('utf-8')

        return dogecoin_address

    @classmethod
    def validate(cls, addr):
        return cls.__validate_by_prefix(addr)
        return cls.__validate_by_fullnode(addr)

    @classmethod
    def get_info(cls, addr):
        return cls.__get_info_from_fullnode(addr)

    @staticmethod
    def __validate_by_prefix(addr):
        # Check if address is of the right length
        if len(addr) != 34:
            return (False)

        # Check if address starts with "D" or "9"
        if addr[0] not in ['D', '9']:
            return (False)

        # Check if address contains only valid characters
        if not re.match("^[0-9A-Za-z]+$", addr):
            return(False)

        return True

    @classmethod
    def __validate_by_fullnode(cls, addr):
        return cls.__validate_by_fullnode__blockcypher(addr)

    @staticmethod
    def __validate_by_fullnode__blockcypher(addr):
        res = requests.get(f'https://api.blockcypher.com/v1/doge/main/addrs/{addr}/balance')
        return True if 'error' not in json.loads(res.text) else False

    @classmethod
    def __get_info_from_fullnode(cls, addr):
        return cls.__get_info_from_fullnode__blockcypher(addr)

    @classmethod
    def __get_info_from_fullnode__blockcypher(cls, addr):
        if cls.validate(addr):
            res = requests.get(f'https://api.blockcypher.com/v1/doge/main/addrs/{addr}/balance')
            return json.loads(res.text)
        else:
            return {}
