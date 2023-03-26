import ecdsa
import hashlib
import base58

def generate_dogecoin_address(private_key):
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

# Take private key as user input
private_key = input("Enter the private key in hexadecimal format: ")

# Generate the Dogecoin address
address = generate_dogecoin_address(private_key)

print("Dogecoin address:", address)
