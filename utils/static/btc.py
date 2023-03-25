from Crypto.Hash import keccak
import re
import hashlib
import base58


def is_valid_bitcoin_address(address):

    try:
        # Decode the Base58Check encoded address
        decoded_address = base58.b58decode(address)
        
    except:
        return(False)
                                      
    if(address[0:3]in['bc1','BC1','TB1','tb1']) or (address[0:4] in ['xpub','XPUB','xprv','XPRV','tpub','TPUB','tprv',"TPRV"]):
        
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
    

    if is_valid_dash_address(address):
        return False
    else:
        return checksum == new_checksum