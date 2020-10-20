import streamlit as st
import pandas as pd
import random

n = 1000

st.write(f"""
# Law of Large Number Example
Shown are the average of {n} random dice rolls!
""")


randomlist = [random.choice(range(1, 7)) for x in range(n)]
c=[]
for i in range(n):
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