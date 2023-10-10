import requests

url = "https://currency-converter-by-api-ninjas.p.rapidapi.com/v1/convertcurrency"

querystring = {"have":"INR","want":"EUR","amount":"5000"}

headers = {
	"X-RapidAPI-Key": "e758985313mshfdbfc7cd6a75a11p113d71jsn5ba6f2ac6332",
	"X-RapidAPI-Host": "currency-converter-by-api-ninjas.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

# import requests

# have_currency = input("Enter the currency you have (e.g., USD): ")
# want_currency = input("Enter the currency you want to convert to (e.g., EUR): ")
# amount = float(input("Enter the amount you want to convert: "))

# url = "https://currency-converter-by-api-ninjas.p.rapidapi.com/v1/convertcurrency"

# querystring = {"have": have_currency, "want": want_currency, "amount": str(amount)}

# headers = {
#     "X-RapidAPI-Key": "e758985313mshfdbfc7cd6a75a11p113d71jsn5ba6f2ac6332",
#     "X-RapidAPI-Host": "currency-converter-by-api-ninjas.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# data = response.json()

# if "error" in data:
#     print("Failed to fetch currency conversion.")
#     print("Error message:", data["error"])
# else:
#     old_amount = data["old_amount"]
#     old_currency = data["old_currency"]
#     new_amount = data["new_amount"]
#     new_currency = data["new_currency"]
#     print(f"{old_amount} {old_currency} is equal to {new_amount} {new_currency}")
