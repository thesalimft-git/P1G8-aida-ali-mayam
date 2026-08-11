from bank_system import BankSystem
from data_manager import DataManager

dm = DataManager('data.json')
bank_data = dm.get_data()

bsm = BankSystem(bank_data)

def main():
    while True:
        print(bank_data)
        bsm.echo_menu()
        dm.set_data(bank_data)
        command = input('select from menu: ')
        
        match command:
            case '1':
                bsm.create_account()
                
            case '2':
                bsm.report_list()
                id = input('which id: ')
                amount = int(input('how much: '))
                bsm.add_transaction(id, 'deposit', amount)
                
            case '3':
                bsm.report_list()
                id = input('which id: ')
                amount = int(input('how much: '))
                bsm.add_transaction(id, 'withdraw', amount)
                
            case '4':
                bsm.report_list()
                id_from = input('from which id: ')
                id_to = input('to which id: ')
                amount = int(input('how much: '))
                
                bsm.add_transaction(id_from, 'withdraw', amount)
                bsm.add_transaction(id_to, 'deposit', amount)
                
            case '5':
                bsm.report_one()
                
            case '6':
                bsm.report_list()
                
            case '7':
                dm.set_data(bank_data)
                print('data is saved')
                
            case '8':
                dm.set_data(bank_data)
                print('data is saved')
                break



main()



