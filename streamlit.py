import streamlit as st
import pandas as pd
import random

st.write("""
# Simple cosa Price App
Shown are the stock **closing price** and ***volume*** of Google!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
#get data on this ticker
randomlist = [random.choice(range(1, 7)) for x in range(1000)]
c=[]
for i in range(1000):
    c.append(sum(randomlist[:i+1])/(i+1))
#get the historical prices for this ticker
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(randomlist)
st.write("""
## Volume Price
""")
st.line_chart(c)