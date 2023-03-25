from Crypto.Hash import keccak
import re
import hashlib
import base58

def is_valid_dash_address(address):
    """
    Validates a Dash address using a regular expression.
    Returns True if the address is valid, and False otherwise.
    """
    # The regular expression for a Dash address
    pattern = re.compile("^(X|8)[a-km-zA-HJ-NP-Z0-9]{33}$")
    
    # Check if the address matches the pattern
    if pattern.match(address):
        return True
    else:
        return False