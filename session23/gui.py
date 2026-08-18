import tkinter as tk
from tkinter import Toplevel
from data_manager import DataManager
from bank_system import BankSystem
from datetime import datetime

class UI:
    def __init__(self) -> None:
        self.dm = DataManager('data.json')
        self.bank_data = self.dm.get_data()
        
        self.root = tk.Tk()
        self.root.title('Bank System App') 
        self.root.geometry("1000x600")   
        
    def save_data(self):
        self.dm.set_data(self.bank_data)
    
    def click_account(self, event):
        account = self.get_selected_id()
        self.show_account_detail()
        print(account)
          
    def load_accounts_list(self):
        account_label = tk.Label(self.root, text="Accounts: ")   
        account_label.grid(row=0, column=0)
        self.account_listbox = tk.Listbox(self.root)
        self.account_listbox.bind("<<ListboxSelect>>", self.click_account)
        
        for id in self.bank_data:
            fullname = self.bank_data[id]['fullname']
            balance = self.bank_data[id]['balance']
            self.account_listbox.insert(id, f'{id}: {fullname} ${balance}')
                        
        self.account_listbox.grid(row=1, column=0, rowspan=10, padx=20)
        if self.account_listbox.size() > 0:
            self.account_listbox.selection_set(0)
        
    def get_selected_id(self):
        selected = self.account_listbox.curselection()
        if selected:
            index = selected[0]
            list_item = self.account_listbox.get(index)
            id = list_item.split(':')[0]
            return id

        return None
    
    def create_account_wizard(self):
        create_account_area_label = tk.Label(self.root, text="Create new Account")   
        create_account_area_label.grid(row=0, column=1, columnspan=2, pady=10)
        
        fullname_label = tk.Label(self.root, text="Full Name: ")   
        fullname_label.grid(row=1, column=1)
        
        amount_label = tk.Label(self.root, text="First Deposit: ")   
        amount_label.grid(row=2, column=1)
 
        
        fullname_entry = tk.Entry(self.root)
        amount_entry = tk.Entry(self.root)

        fullname_entry.grid(row=1, column=2)
        amount_entry.grid(row=2, column=2)
        
        create_account_button = tk.Button(
            self.root, 
            text="Create", 
            width=25, 
            command=lambda: self.create_account_handler(
                fullname_entry.get(),
                amount_entry.get()
            )
        )
        create_account_button.grid(row=3, column=1, columnspan=2)

    def create_account_handler(self, fullname, amount):
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
        
        self.save_data()
        self.load_wizard()

        print('account created successfully')
     
    def show_account_detail(self):
        show_account_area_label = tk.Label(self.root, text="Account Details:")   
        show_account_area_label.grid(row=0, column=3, columnspan=2, padx=20)
        
        account_name_label = tk.Label(self.root, text="Name")   
        account_name_label.grid(row=1, column=3)
        
        try:
            fullname = self.bank_data.get(self.get_selected_id()).get('fullname')
            account_name_value_label = tk.Label(self.root, text=fullname)   
            account_name_value_label.grid(row=1, column=4)
        except:
            pass
    
    
        account_balance_label = tk.Label(self.root, text="balance")   
        account_balance_label.grid(row=2, column=3, padx=30, pady=1)
        
        try:
            balance = self.bank_data.get(self.get_selected_id()).get('balance')
            account_balance_value_label = tk.Label(self.root, text=balance)   
            account_balance_value_label.grid(row=2, column=4)
        except:
            pass
                
        account_history_label = tk.Label(self.root, text="history")   
        account_history_label.grid(row=0, column=6)
        
        
        try:
            histories = self.bank_data.get(self.get_selected_id()).get('history')
            self.history_listbox = tk.Listbox(self.root)
            
            for index, history in enumerate(histories):
                type = history.get('type')
                amount = history.get('amount')
                date = history.get('date')
                self.history_listbox.insert(index, f'${amount} is {type} at {date}')
                                
            self.history_listbox.grid(row=1, column=6, rowspan=10)
        except:
            pass
        
        deposit_button = tk.Button(
            self.root, 
            text="Deposit", 
            width=15, 
            command=lambda: self.second_level("Deposit")
        )
        
        deposit_button.grid(row=4, column=3)
        
        withdraw_button = tk.Button(
            self.root, 
            text="Withdraw", 
            width=15, 
            command=lambda: self.second_level("Withdraw")
        )
        
        withdraw_button.grid(row=4, column=4, padx=10)
        
    # TODO: add top level
    def second_level(self, mode):
        top = Toplevel(self.root)
        top.title(mode)
        top.geometry("250x120")

        amount_label = tk.Label(top, text="Amount:")
        amount_label.grid(row=0, column=0, padx=10, pady=10)

        amount_entry = tk.Entry(top)
        amount_entry.grid(row=0, column=1, padx=10, pady=10)

        confirm_button = tk.Button(
            top,
            text="Confirm",
            command=lambda: self.transaction_handler(mode, amount_entry.get(), top)
        )
        confirm_button.grid(row=1, column=0, columnspan=2, pady=10)
        
    def transaction_handler(self, mode, amount, top):
        print(f"{mode}: {amount}")
        top.destroy()    
          
        
    def load_wizard(self):
        self.load_accounts_list()
        self.create_account_wizard()
        self.show_account_detail()
        self.root.mainloop()
        
        







ui = UI()
ui.load_wizard()