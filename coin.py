import requests
from tabulate import tabulate
 
def get_coinmarketcap_tokens(api_key):
    headers = {
        'X-CMC_PRO_API_KEY': api_key,
        'Accept': 'application/json'
    }
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '800',
        'convert': 'USD'  # You can change the currency if needed
    }
 
    response = requests.get(url, headers=headers, params=parameters)
 
    if response.status_code == 200:
        return response.json()['data']
    else:
        print('Failed to fetch data from CoinMarketCap API')
        return None
 
def main():
    api_key = '67343690-167e-4d91-a30e-09e9bd0949c8'
    tokens = get_coinmarketcap_tokens(api_key)
 
    if tokens is None or len(tokens) == 0:
        print('No tokens found or failed to fetch data.')
        return
 
    token_data = []
 
    for token in tokens:
        token_info = [
            token['name'],
            token['symbol'],
            token['quote']['USD']['price'],
            token['quote']['USD']['market_cap']
        ]
        token_data.append(token_info)
 
    headers = ['Name', 'Symbol', 'Price', 'Market Cap']
 
    # Display tokens in groups of 50
    start = 0
    chunk_size = 50
    while start < len(token_data):
        print(tabulate(token_data[start:start+chunk_size], headers=headers, floatfmt=".2f"))
        start += chunk_size
        input("Press Enter to continue...")
 
if __name__ == '__main__':
    main()
