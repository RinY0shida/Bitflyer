from bitcoin_ohcl_fetcher import BitcointOhclFetcher

def main():
    bitcoin_ohcl_fetcher = BitcointOhclFetcher()
    
    minute_ohcl_result = bitcoin_ohcl_fetcher.FetchOhclData("histominute")
    printf(f"取得した分速データの個数: {len(minute_ohlc_result)}個")

main()