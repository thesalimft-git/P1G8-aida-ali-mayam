from datetime import datetime

class BankSystem:
    def __init__(self, bank_data) -> None:
        self.bank_data = bank_data
    
    def echo_menu(self):
        print('\n'*3)
        print('='*30)
        print('1- Create Account')
        print('2- Deposit')
        print('3- Withdraw')
        print('4- Transfer')
        print('5- Report One')
        print('6- Report List')
        print('7- Save Data')
        print('8- Save and Exit')
        
    def amount_is_number(self, amount:str) -> bool:
        try:
            float(amount)
            return True
        except:
            return False
    
    def create_account(self):
        while True:
            fullname = input('full name: ')
            if 3 < len(fullname) < 20:
                break
            else:
                print('name is not valid')
            
        while True:
            amount = input('amount: ')
            if self.amount_is_number(amount):
                amount = float(amount)
                break
            else:
                print('amount is not valid')
                
        now = datetime.now()
        date = now.strftime('%Y-%m-%d')
        id = len(self.bank_data) + 1
        
        self.bank_data[str(id)] = {
            'fullname': fullname,
            'balance': amount,
            'history': [
                {
                    'type': 'deposit', 
                    'amount': amount, 
                    'date': date
                }
            ]  
        }

        print('account created successfully')
    
    def report_list(self):
        for id in self.bank_data:
            fullname = self.bank_data[id]['fullname']
            balance = self.bank_data[id]['balance']
            print(f'{id}- {fullname} (${balance})')  

    def report_one(self):
        self.report_list()
        id = input('which id: ')
        fullname = self.bank_data[id]['fullname'] 
        balance = self.bank_data[id]['balance'] 
        print(f'{id}- {fullname} ($ {balance})') 
        
        histories = self.bank_data[id]['history'] 
        for history in histories:
            print(f'\t- ${history['amount']} {history['type']} at {history['date']}')

    def add_transaction(self, id:str, type:str, amount:int):
        balance = self.bank_data[id]['balance']
        
        if type == 'deposit':
            balance += amount
        elif type == 'withdraw':
            balance -= amount
        else:
            print('type is not valid: {type}')
            
        self.bank_data[id]['balance'] = balance
         
    
    
# 192.168.100.7:5173/abc.txt