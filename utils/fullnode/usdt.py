import json
import os

def check_addr(addr: str) -> bool:
    return _check_from_curlapi(addr)

def _check_from_curlapi(addr: str) -> bool:
    header = "Content-Type: application/x-www-form-urlencoded"
    url = "https://api.omniexplorer.info/v1/address/addr/"
    command = f'curl -sS -X POST -H "{header}" -H "{header}" -d "addr={addr}" "{url}"'

    stream = os.popen(command)
    output = stream.read()

    r = json.loads(output)
    return not 'error' in r.keys()


def test__check_from_curlapi():
    result = check_addr('3MbYQMMmSkC3AgWkj9FMo5LsPTW1zBTwXL')
    assert result == True
    result = check_addr('3MbYQMMmSkC3AgWkj9FMo5LsPTW1zBTwXn')
    assert result == False

def get_addr_details(addr: str) -> bool:
    return _get_details_curlapi(addr)

def _get_details_curlapi(addr: str):
    if check_addr(addr):
        header = "Content-Type: application/x-www-form-urlencoded"
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


def test__get_details_curlapi():
    result = get_addr_details('3MbYQMMmSkC3AgWkj9FMo5LsPTW1zBTwXL')
    # print(result)
    result = get_addr_details('3MbYQMMmSkC3AgWkj9FMo5LsPTW1zBTwXn')
    # print(result)
