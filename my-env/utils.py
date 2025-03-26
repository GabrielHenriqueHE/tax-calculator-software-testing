def read_float(message: str) -> float:
        
    while True:
        value = input(message).replace(",", ".")
        
        try:
            return float(value)
        except:
            pass

    
def read_int(message: str) -> int:
    while True:
        value = input(message).replace(",", ".")
        
        try:
            return int(value)
        except:
            pass