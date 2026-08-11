# 1023- ali akbari ( $100 )


    
# data_bank = {
#     '1023': {
#         'fullname': 'ali akbari',
#         'balance': 100,
#         'history': [
#             {'type': 'deposit', 'amount': 10, 'date': '2025-03-1'}
#         ]  
#     },
#     '1024': {
#         'fullname': 'ali akbari',
#         'balance': 100,
#         'history': [
#             {'type': 'deposit', 'amount': 10, 'date': '2025-03-1'}
#         ]  
#     },
# }


import json

class DataManager():
    def __init__(self, file_name:str) -> None:
        self.file_name = file_name

    def get_data(self) -> dict:
        try:
            with open(self.file_name, 'r') as f:
                return json.load(f)
        except:
            return dict()
    
    def set_data(self, data) -> None:
        with open(self.file_name, 'w') as f:
            json.dump(data,f)
            
            


