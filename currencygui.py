import requests
import tkinter as tk

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

# Create the input elements
have_currency_label = tk.Label(window, text="Currency you have:")
have_currency_label.grid(row=0, column=0, padx=10, pady=10)
have_currency_entry = tk.Entry(window)
have_currency_entry.grid(row=0, column=1, padx=10, pady=10)

want_currency_label = tk.Label(window, text="Currency you want to convert to:")
want_currency_label.grid(row=1, column=0, padx=10, pady=10)
want_currency_entry = tk.Entry(window)
want_currency_entry.grid(row=1, column=1, padx=10, pady=10)

amount_label = tk.Label(window, text="Amount:")
amount_label.grid(row=2, column=0, padx=10, pady=10)
amount_entry = tk.Entry(window)
amount_entry.grid(row=2, column=1, padx=10, pady=10)

convert_button = tk.Button(window, text="Convert", command=get_currency_conversion)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
window.mainloop()
