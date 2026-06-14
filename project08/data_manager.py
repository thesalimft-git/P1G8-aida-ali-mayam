import json

f_addr = 'project08/data.json'

def get_data():
    try:
        with open(f_addr, 'r') as f:
            return json.load(f) 
    except:
        with open(f_addr, 'w') as f:
            print('file did not exist, i create one')
            return dict()


def set_data(data):
    with open(f_addr, 'w') as f:
        json.dump(data, f)
