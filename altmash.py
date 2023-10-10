import requests
import tkinter as tk
from tkinter import ttk

def get_currency_conversion():
    have_currency = have_currency_entry.get()
    want_currency = want_currency_entry.get()
    amount = float(amount_entry.get())

    url = "https://currency-converter-by-api-ninjas.p.rapidapi.com/v1/convertcurrency"

    querystring = {"have": have_currency, "want": want_currency, "amount": str(amount)}

    headers = {
        "X-RapidAPI-Key": "e758985313mshfdbfc7cd6a75a11p113d71jsn5ba6f2ac6332",
        "X-RapidAPI-Host": "currency-converter-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()

    if "error" in data:
        result_label.config(text="Failed to fetch currency conversion.\nError message: " + data["error"])
    else:
        old_amount = data["old_amount"]
        old_currency = data["old_currency"]
        new_amount = data["new_amount"]
        new_currency = data["new_currency"]
        result_label.config(text=f"{old_amount} {old_currency} is equal to {new_amount} {new_currency}")

# Create the main window
window = tk.Tk()
window.title("Currency Converter")

# Create a notebook to hold multiple file tabs
notebook = ttk.Notebook(window)
notebook.pack()

# Create a new file tab
file_tab = ttk.Frame(notebook)
notebook.add(file_tab, text="File")

# Create the input elements in the file tab
have_currency_label = tk.Label(file_tab, text="Currency you have:")
have_currency_label.grid(row=0, column=0, padx=10, pady=10)
have_currency_entry = tk.Entry(file_tab)
have_currency_entry.grid(row=0, column=1, padx=10, pady=10)

want_currency_label = tk.Label(file_tab, text="Currency you want to convert to:")
want_currency_label.grid(row=1, column=0, padx=10, pady=10)
want_currency_entry = tk.Entry(file_tab)
want_currency_entry.grid(row=1, column=1, padx=10, pady=10)

amount_label = tk.Label(file_tab, text="Amount:")
amount_label.grid(row=2, column=0, padx=10, pady=10)
amount_entry = tk.Entry(file_tab)
amount_entry.grid(row=2, column=1, padx=10, pady=10)

convert_button = tk.Button(file_tab, text="Convert", command=get_currency_conversion)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(file_tab, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
window.mainloop()

