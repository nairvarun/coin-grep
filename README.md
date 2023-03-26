<p align="center">
  <img src="https://user-images.githubusercontent.com/64140687/227789492-f51d8abc-29d7-4a67-86b5-8e2e6789c7b8.png">
</p>

### Indigenous technological Crypto Currency Investigation Tools with multi-blockchain platform support.

<br>

## Installation:
You can install the tool by cloning the repo using the command given below or downloading as a zip.

```bash
$> git clone https://github.com/nairvarun/coin-grep.git
```

This tool required `python3` installed on the local system. Once python is installed, you can install the dependencies using the requirements file in the directory.

```bash
$> cd coin-grep
$> pip install -r requirements.txt
```

Run the following command to start the `fastapi` server on local host.

```bash
$> uvicorn api:api --reload
```

To make API calls, read the docs below to understand the structure.

## API Routes:
Current implemented routes in the API are:

| Route | Description |
|-------|-------------|
|<p align="center">`/derive`</p>| This is an experimental feature that takes the private key for a bitcoin/doge transaction and returns the address derived from a specific elliptic curve. The parameters required are `key` and `key_type`, which takes in the key and the currency name it belongs to. Currently limited to btc and doge only.|
|<p align="center">`/read_qr`</p>| This route is designed for our APK which reads a QR Code and checks if it belongs to a specific chain or not.|
|<p align="center">`/get_details`</p>| This route requires 1 parameter `addr`, and takes the address in the form of base58 encoded string. The API returns the details about the address gathered from external API's and gives the result in JSON format.|
|<p align="center">`/check_fullnode`</p>| This route requires 1 paramter `addr`, and takes the address in the form of base58 encoded string. The address is first passed through a static check which identifies the currency type and then an external API call is made to ensure the address validity. |
|<p align="center">`/check_lighnode`</p>| This route requires 1 parameter `addr`,  and takes the address in the form of base58 encoded string. The address is passed through a static check which identifies th currency type. The tool then queries the official chain of the address and runs it through the official chain of the currency. |






