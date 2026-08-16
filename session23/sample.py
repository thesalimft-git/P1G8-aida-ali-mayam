


# import tkinter as tk


# class BankGUI:

#     def __init__(self, root, bank_data):
#         self.root = root
#         self.bank_data = bank_data

#         self.root.title("Simple Bank System")
#         self.root.geometry("850x500")

#         self.create_widgets()

#     # ----------------------------
#     # Create GUI
#     # ----------------------------
#     def create_widgets(self):

#         # ========= Left Side =========
#         tk.Label(
#             self.root,
#             text="Accounts",
#             font=("Arial", 14, "bold")
#         ).grid(row=0, column=0, padx=10, pady=10)

#         self.account_list = tk.Listbox(
#             self.root,
#             width=35,
#             height=20
#         )

#         self.account_list.grid(
#             row=1,
#             column=0,
#             rowspan=10,
#             padx=10,
#             pady=5
#         )

#         scrollbar = tk.Scrollbar(
#             self.root,
#             command=self.account_list.yview
#         )

#         scrollbar.grid(
#             row=1,
#             column=1,
#             rowspan=10,
#             sticky="ns"
#         )

#         self.account_list.config(
#             yscrollcommand=scrollbar.set
#         )

#         # ========= Right Side =========
#         tk.Label(
#             self.root,
#             text="Account Information",
#             font=("Arial", 14, "bold")
#         ).grid(row=0, column=2, padx=20)

#         tk.Label(self.root, text="ID :").grid(row=1, column=2, sticky="w")
#         self.lbl_id = tk.Label(self.root, text="-")
#         self.lbl_id.grid(row=1, column=3, sticky="w")

#         tk.Label(self.root, text="Name :").grid(row=2, column=2, sticky="w")
#         self.lbl_name = tk.Label(self.root, text="-")
#         self.lbl_name.grid(row=2, column=3, sticky="w")

#         tk.Label(self.root, text="Balance :").grid(row=3, column=2, sticky="w")
#         self.lbl_balance = tk.Label(self.root, text="-")
#         self.lbl_balance.grid(row=3, column=3, sticky="w")

#         tk.Label(
#             self.root,
#             text="History"
#         ).grid(row=4, column=2, columnspan=2)

#         self.history = tk.Text(
#             self.root,
#             width=40,
#             height=12
#         )

#         self.history.grid(
#             row=5,
#             column=2,
#             columnspan=2,
#             padx=10
#         )

#         # ========= Buttons =========
#         tk.Button(
#             self.root,
#             text="Load Accounts",
#             width=18,
#             command=self.load_accounts
#         ).grid(row=11, column=0, pady=15)

#         tk.Button(
#             self.root,
#             text="Exit",
#             width=18,
#             command=self.root.destroy
#         ).grid(row=11, column=2)

#     # ----------------------------
#     # Load account list
#     # ----------------------------
#     def load_accounts(self):

#         self.account_list.delete(0, tk.END)

#         for account_id, account in self.bank_data.items():

#             text = f"{account_id} - {account['fullname']} ($ {account['balance']})"

#             self.account_list.insert(tk.END, text)


    # if __name__ == "__main__":

    #     # Demo data if you run gui.py directly
    #     demo_data = {
    #         "1": {
    #             "name": "Ali",
    #             "balance": 300,
    #             "history": []
    #         },
    #         "2": {
    #             "name": "Reza",
    #             "balance": 500,
    #             "history": []
    #         },
    #         "3": {
    #             "name": "Sara",
    #             "balance": 900,
    #             "history": []
    #         }
    #     }

    #     root = tk.Tk()

    #     app = BankGUI(root, demo_data)

    #     root.mainloop()


