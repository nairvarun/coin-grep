import os, sys
import struct
from hashlib import sha3_256
from Crypto.Hash import keccak
from binascii import hexlify, unhexlify
import ed25519
import base58
# import ed25519
# sys.path.append('../libraries')


def hex2int(hex):
    ## converts a hex string to integer
    return ed25519.decodeint(unhexlify(hex))

def int2hex(int):
    ## converts an integer to a little endian encoded hex string
    return hexlify(ed25519.encodeint(int))

def keccak_256(message):
    # h = sha3.keccak_256()
    # h.update(unhexlify(message))
    h = keccak.new(data=unhexlify(message), digest_bits=256).digest()
    # return h.hexdigest()
    return str(hexlify(h))[2:-1]

def sc_reduce32(input):
    ## convert hex string input to integer
    int = hex2int(input)
    ## reduce mod l
    modulo = int % (2**252 + 27742317777372353535851937790883648493)
    ## convert back to hex string for return value
    return int2hex(modulo)

def hash_to_scalar(key):
    hash = keccak_256(key)
    return sc_reduce32(hash)

def hash_to_ec(key):
    scalar = hash_to_scalar(key)
    ## convert to point on curve by multiplying the base point by the resulting scalar
    point = ed25519.scalarmultbase(scalar)
    ## multiply by 8 for security
    return ed25519.scalarmult(point, 8)

## multiply a public key (a point on the curve) by a private key (a scalar within the field p)
def generate_key_derivation(public, private):
    point = ed25519.scalarmult(ed25519.decodepoint(unhexlify(public)), hex2int(private))
    ##multiply by 8 for security
    res = ed25519.scalarmult(point, 8)
    ## return hex encoding of the resulting point
    return hexlify(ed25519.encodepoint(res))

def derivation_to_scalar(derivation, index):
    ## concatenate index to derivation
    data = derivation + index
    return hash_to_scalar(data)

## Alias for scalarmultbase
def publickey_to_privatekey(privateKey):
    point = ed25519.scalarmultbase(hex2int(privateKey))
    return hexlify(ed25519.encodepoint(point))

def generate_random_address():
    ## generate 32 bytes (256 bits) of pseudo-random data
    seed = hexlify(os.urandom(32))

    ## reduce random data to make it a valid ed25519 scalar
    secret_spend_key = sc_reduce32(seed)

    ## use a reduced hash of the secret spend key for the deterministic secret view key
    secret_view_key = hash_to_scalar(secret_spend_key)

    ## multiply by the generator point to get public keys from private keys
    public_spend_key = publickey_to_privatekey(secret_spend_key)
    public_view_key  = publickey_to_privatekey(secret_view_key)

    ## the network byte, public spend key, and public view key are all concatenated together
    ## 0x12 is the Monero mainnet network byte
    network_byte = "12"
    ## Concatenate the three strings
    data = network_byte + str(public_spend_key)[2:-1] + str(public_view_key)[2:-1]
    # print(public_spend_key)
    # data = network_byte + public_spend_key
    hash = keccak_256(data)
    ## checksum is the first 4 bytes (8 hex characters) of the hash of the previous data
    checksum = hash[0:8]
    address = base58.b58decode(data + checksum)

    ## Priting the keys

    print("Secret_spend_key : " + secret_spend_key)
    print("Secret_view_key : " + secret_view_key)
    print("Public_spend_key : " + public_spend_key)
    print("Public_view_key : " + public_view_key)

    ## Returning address generated
    return address

generate_random_address()
