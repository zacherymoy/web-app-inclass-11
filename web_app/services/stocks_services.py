import requests
import json

#Mike showed URL in class and pasted to request_url 
# Put in API_Key this one is abc123
# Put in symbol
symbol = "AAPL"
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey=abc123"
print(request_url)

response = requests.get(request_url)
print(type(response)) #> <class 'requests.models.Response'>
print(response.status_code) #> 200
print(type(response.text)) #> <class 'str'>

#converting to text
parsed_response = json.loads(response.text)
print(type(parsed_response)) #> <class 'dict'>

#Done to investigate what you're doing wrong
breakpoint()

#Mike modified date 
latest_close = parsed_response["Time Series (Daily)"]["2020-04-24"]["4. close"]
print("LATEST CLOSING PRICE:", latest_close)

# Mike typed in python web_app/services/stocks_service.py