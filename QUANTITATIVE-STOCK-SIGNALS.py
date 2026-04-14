# We are bringing in the tools we put in the terminal as yf means we r jus naming it as yf so we wont need to type sm
import yfinance as yf
import pandas as pd


ticker_symbol = input("Enter the stock market ID NAME (eg: AAPL) : ") #(Here we type the id the stockl market use to identify the stock )
periodl = input("Enter how long of data do you want prediction with from these (1mo,3mo,6mo) : ")



# We add 'auto_adjust=True' to make sure we get clean price data, if u hover or click cntrol over download u can see parameter
stock_data = yf.download(ticker_symbol, period= periodl, interval="1d", auto_adjust=True)


stock_data['Moving average 20'] = stock_data['Close'].rolling(window=20).mean()#  Calculating the average using pandas


current_price = stock_data['Close'].iloc[-1].item() #Here we are getting the most recent data integer loction of last row
average_price = stock_data['Moving average 20'].iloc[-1].item()


print("-" * 30)
print(f"Current Price: ${current_price:.2f}")
print(f"20-Day Average: ${average_price:.2f}")
print("-" * 30)

if current_price > average_price:
    print("PREDICTION: BULLISH (Price is above average)")
else:
    print("PREDICTION: BEARISH (Price is below average)")
print("-" * 30)



import matplotlib.pyplot as plt

#Create the Chart
plt.figure(figsize=(12, 6)) #Here we made a graph and put x and y axis
plt.plot(stock_data['Close'], label= f"{ticker_symbol}", color='blue')
plt.plot(stock_data['Moving average 20'], label='20-Day Average', color='orange')

# Add titles and labels
plt.title(f"{ticker_symbol} Price vs 20-Day Average")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.legend() #basically makes sure blue = price and orange = average
plt.grid(True) #shows the grid

# Show the chart
print("Opening chart window...")
plt.show()