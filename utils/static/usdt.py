def is_avalanche_address(address):
    c_chain_pattern = r"^0x[0-9a-fA-F]{40}$"
    x_chain_pattern = r"^X-[a-zA-Z0-9]{1,102}$"
    p_chain_pattern = r"^P-[a-zA-Z0-9]+$"  # corrected pattern
    
    if re.match(c_chain_pattern, address):
        return True
    elif re.match(x_chain_pattern, address):
        return True
    elif re.match(p_chain_pattern, address):
        return True
    else:
        return False

def is_valid_polygon(sample_string):
    polygon_address_pattern = "^0x[a-fA-F0-9]{40}$"

# Sample string that may contain a Polygon address

# Find all Polygon addresses in the sample string
    polygon_addresses = re.findall(polygon_address_pattern, sample_string)

# Print the results
    if len(polygon_addresses) > 0:
        return(True)
    
    else:
        return(False)


def is_tron_address(address):
    if len(address) != 34 and len(address)!=42:
        return False
    if not address.startswith('T'):

        if not address.startswith('4'):
            return False
    for char in address:
        if char not in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            return False
    return True


def is_eos_address(address):
    if isinstance(address, str):
        return address.startswith('EOS') and len(address) == 53 and all(c in '12345abcdefghijklmnopqrstuvwxyz' for c in address[3:])
    return False




def is_liquid_address(address):
    # Check if the address starts with "q" or "Q"
    if not address.startswith('q') and not address.startswith('Q'):
        return False

    # Check if the address is a valid Liquid address format
    if not re.match(r'^[qQ][a-zA-Z0-9]{41}$', address):
        return False

    # If both conditions are true, return True
    return True


        
        
a=str(input())
print(is_valid_polygon(a))

print(is_avalanche_address(a))
print(is_tron_address(a))
print(is_eos_address(a))
