def normalize_time(t:str) -> int:
    hour = int(t.split(':')[0])
    minute = int(t.split(':')[1])
    response = hour*60 + minute
    return response



# IRHT
def normalize_price(pr:str) -> int:
    
    # ???
    
    return pr