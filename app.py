import streamlit as st
import requests

# Custom Cryptocurrency News API connection class
class CryptocurrencyNewsAPIConnection:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://crypto-news16.p.rapidapi.com/news/top/5"
        self.headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "crypto-news16.p.rapidapi.com"
        }

    def get_news_data(self):
        try:
            response = requests.get(self.base_url, headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                st.error(f"Error: Unable to fetch cryptocurrency news data. Status code: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            st.error("Error: Unable to connect to the Cryptocurrency News API.")
            return None

# Main app
def main():
    st.title("Cryptocurrency News App")
    st.write("Click the button below to get the top 5 cryptocurrency news articles!")

    if st.button("Get Cryptocurrency News"):
        api_key = 'b81c83e68bmsh04f50cb9442cba8p171b50jsnf1e1438fae4e'
        connection = CryptocurrencyNewsAPIConnection(api_key)
        news_data = connection.get_news_data()

        if news_data:
            for i, article in enumerate(news_data, 1):
                st.subheader(f"Article {i}: {article['title']}")
                st.write(f"Date: {article['date']}")
                st.write(f"Description: {article['description']}")
                st.write(f"URL: {article['url']}")
                st.write("\n")

        else:
            st.warning("No cryptocurrency news data found.")

if __name__ == "__main__":
    main()
