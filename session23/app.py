import tkinter as tk
from data_manager import DataManager
from gui import BankGUI

# Load data
dtm = DataManager("data.json")
bank_data = dtm.get_date()

root = tk.Tk()

app = BankGUI(root, bank_data)

root.mainloop()