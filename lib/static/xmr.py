def is_valid_monero_address(address):

    if(address[0]=='4' and len(address)==95) or (address[0]=='8' and len(address)==106)or((address[0]in['4','8'])and len(address)==64):

        return(True)
    else:
        return(False)
