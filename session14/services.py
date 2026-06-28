def normalize_time(t:str) -> int:
    hour = int(t.split(':')[0])
    minute = int(t.split(':')[1])
    response = hour*60 + minute
    return response




def normalize_price(pr:str) -> int:
    try: 
        pr = pr.strip()
        pr = pr.replace(',', '')
        return int(pr)
    except:
        print('can not read price')
        return 0
