from Crypto.Hash import keccak
import re
import hashlib
import base58

def is_valid_ethereum_address(address):
    if not re.match(r'^(0x)?[0-9a-fA-F]{40}$', address):
        return False
    elif re.match(r'^(0x)?[0-9a-fA-F]{40}$', address) or re.match(r'^(0x)?[0-9A-Fa-f]{40}$', address):
        return (True)
    else:
        return False