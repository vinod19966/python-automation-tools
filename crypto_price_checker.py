import requests

coin = input("Enter coin (bitcoin/ethereum): ")

url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"

data = requests.get(url).json()

print(f"{coin} price: ${data[coin]['usd']}")
