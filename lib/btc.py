import ecdsa
import hashlib
import base58
import json
import requests
from lib._cryptocurrency import Cryptocurrency
from lightnode import is_btc_address

# TODO: add doc strings
# TODO: add tests
# TODO: derive [priv] --> [pub] --> addr (normal and segwit)
# TODO: only import needed methods from imports (??)

class BTC(Cryptocurrency):

    def __init__(self) -> TypeError:
        super().__init__()

    # TODO: redo
    @classmethod
    def derive(cls, key: str) -> dict:
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
        network_byte = b'\x00'
        hash_with_network_byte = network_byte + ripemd160_hash

        # Step 5: Generate the checksum
        first_hash = hashlib.sha256(hash_with_network_byte).digest()
        second_hash = hashlib.sha256(first_hash).digest()
        checksum = second_hash[:4]

        # Step 6: Create the address
        address_bytes = hash_with_network_byte + checksum
        bitcoin_address = base58.b58encode(address_bytes).decode('utf-8')

        return bitcoin_address

    # TODO: handle all 3 in one method
    @classmethod
    def validate(cls, addr: str) -> bool:
        return cls.__validate_by_lightnode(addr)
        return cls.__validate_by_prefix(addr)
        return cls.__validate_by_fullnode(addr)

    @classmethod
    def get_info(cls, addr: str) -> dict:
        return cls.__get_info_from_fullnode(addr)
        return cls.__get_info_from_lighnode(addr)

    @staticmethod
    def __validate_by_prefix(addr: str) -> bool:
        try:
            # Decode the Base58Check encoded address
            decoded_address = base58.b58decode(addr)

        except:
            return(False)

        if(addr[0:3]in['bc1','BC1','TB1','tb1']) or (addr[0:4] in ['xpub','XPUB','xprv','XPRV','tpub','TPUB','tprv',"TPRV"]):

            return(True)
        # Extract the checksum from the decoded address
        checksum = decoded_address[-4:]

        # Calculate the hash of the address without the checksum
        address_hash = decoded_address[:-4]

        # Calculate the double SHA256 hash of the hash of the address
        double_hash = hashlib.sha256(hashlib.sha256(address_hash).digest()).digest()

        # Take the first 4 bytes of the double hash as the new checksum
        new_checksum = double_hash[:4]

        # Compare the new checksum with the original checksum


        # if dash.is_valid_dash_address(address):
        #     return False
        # else:
        #     return checksum == new_checksum

    @staticmethod
    def __validate_by_lightnode(addr: str) -> bool:
        return is_btc_address(addr)
        return lightnodes. bitcoin.is_address(addr)

    @classmethod
    def __validate_by_fullnode(cls, addr: str) -> bool:
        return cls.__validate_by_fullnode__blockcypher(addr)

    @staticmethod
    def __validate_by_fullnode__blockcypher(addr: str) -> bool:
        res = requests.get(f'https://api.blockcypher.com/v1/btc/main/addrs/{addr}/balance')
        return True if 'error' not in json.loads(res.text) else False

    @staticmethod
    def __get_info_from_lighnode():
        pass

    @classmethod
    def __get_info_from_fullnode(cls, addr: str) -> dict:
        return cls.__get_info_from_fullnode__blockcypher(addr)

    @classmethod
    def __get_info_from_fullnode__blockcypher(cls, addr: str) -> bool:
        if cls.validate(addr):
            res = requests.get(f'https://api.blockcypher.com/v1/btc/main/addrs/{addr}/balance')
            return json.loads(res.text)
        else:
            return {}
