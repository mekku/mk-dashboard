import streamlit as st
import requests

# Function to get Jenkins status
def get_jenkins_status():
    jenkins_url = 'https://mkjk.ideractive.com/api/json'  # Replace with your Jenkins URL
    response = requests.get(jenkins_url)
    data = response.json()
    build_status = data['jobs'][0]['color']
    return build_status

# Function to get BTC price
def get_btc_price():
    btc_url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(btc_url)
    data = response.json()
    btc_price = data['bpi']['USD']['rate']
    return btc_price

# st.title('Custom Dashboard')

if st.button('Refresh'):
    # jenkins_status = get_jenkins_status()
    btc_price = get_btc_price()
    
    # st.write(f'Jenkins Build Status: {jenkins_status}')
    st.write(f'# BTC Price: ${btc_price}')
else:
    st.write('Click the button to refresh the data.')
