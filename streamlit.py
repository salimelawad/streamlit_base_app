import streamlit as st
import pandas as pd
import random


n = st.sidebar.slider("random dice rolls", min_value=0, max_value=250, value=100)

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
## Random roll result
""")
st.line_chart(randomlist)
st.write("""
## Cummulative average
""")
st.line_chart(c)