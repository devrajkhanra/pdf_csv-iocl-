# ./modules/generate_serials_range.py

def generateSerialsRange(firstSerial:str, lastSerial:str, difference:int, digits:int):
    
    start:int = int(firstSerial)
    end:int = int(lastSerial)
    
    serialRange:list = list(range(start, end, difference))
    
    result = []
    for i in serialRange:
        result.append(str(i).zfill(digits))
    
    return result 
    