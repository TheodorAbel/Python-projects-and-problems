import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Invalid argument. Please provide one argument.")
try:
    bitcoins=float(sys.argv[1])
except ValueError:
    sys.exit("Invalid argument")
try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    r.raise_for_status()  # Check if the request was successful
    bitcoin_data = r.json()
    rate=bitcoin_data["bpi"]["USD"]["rate"]
    rate=float(rate.replace(",",""))
    print(f"${rate*bitcoins:,.4f}")

except requests.RequestException as e:
    print(f"Error fetching data: {e}")
