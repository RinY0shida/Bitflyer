from bitcoin_ohcl_fetcher import BitcointOhclFetcher

def main():
    bitcoin_ohcl_fetcher = BitcointOhclFetcher()
    
    minute_ohcl_result = bitcoin_ohcl_fetcher.FetchOhclData("histominute")
    hour_ohcl_result = bitcon
    print(f"取得した分速データの個数: {len(minute_ohcl_result)}個")

if __name__ == "__main__":
    main()
