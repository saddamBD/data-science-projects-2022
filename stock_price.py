import streamlit as st
import yfinance as yf
import pandas as pd


st.write("""
# simple stock price prediction

Shown are the stock **closing price** and **volume** of Google

""")
# define ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historic price for this ticker

tickerDf = tickerData.history(period='1d',start = '2010-05-31', end = '2020-05-31')

st.write(""""
### Closing Price
""")
st.line_chart(tickerDf.Close)

st.write(""""
### Volume Price
""")
st.line_chart(tickerDf.Volume)




