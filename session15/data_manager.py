import json

file_name = 'data.json'

def get_data():
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except:
        return dict()


def set_data(data):
    with open(file_name, 'w') as f:
        json.dump(data, f)