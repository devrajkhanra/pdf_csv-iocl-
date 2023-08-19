# ./modules/get_serials.py

def getSerials():
    '''Get the first serial number and last serial of the SOR from the user'''    
    # take first and last serial number as input from user
    first_serial = input('Enter first serial number: ')
    last_serial = input('Enter last serial number: ')
    
    return [first_serial, last_serial]