from bank_system import BankSystem
from data_manager import DataManager
from gui import UI


dm = DataManager('data.json')
bank_data = dm.get_data()

bsm = BankSystem(bank_data)
ui = UI(bank_data)