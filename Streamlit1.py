import pandas as pd
import yfinance as yf
import streamlit as st
import datetime

st.write(""" # Simple Stock Price App""")
tickersymbol = st.text_input('Ticker Symbol').upper()

today = datetime.date.today()
future_date = today + datetime.timedelta(days=1)
start_date = st.date_input('Start date', today)
end_date = st.date_input('End date', future_date)
if start_date < end_date:
    #st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
    pass

else:
    st.error('Error: End date must fall after start date.')
st.write("Shown are the stock **Closing Price** and **Volume** of" , tickersymbol)
tickerData= yf.Ticker(tickersymbol)
tickerDf= tickerData.history(period='1d', start =start_date, end=end_date)
st.write("**Closing Price**", tickersymbol)
st.area_chart(tickerDf.Close)
st.write("**Volume** of ", tickersymbol)
st.line_chart(tickerDf.Volume)

#x=st.slider("Select a date")
#st.write("you selected", x)


