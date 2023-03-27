import re

def is_valid_dogecoin_address(address):

    # Check if address is of the right length
    if len(address) != 34:
        return (False)

    # Check if address starts with "D" or "9"
    if address[0] not in ['D', '9']:
        return (False)

    # Check if address contains only valid characters
    if not re.match("^[0-9A-Za-z]+$", address):
        return(False)

    return True

# a=str(input())
# print(is_valid_dogecoin_address(a))