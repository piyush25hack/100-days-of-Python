import requests
from twilio.rest import Client  

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# 🔥 API Keys (Environment variables use karo)
STOCK_API_KEY = "YOUR_STOCK_API_KEY"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
TWILIO_SID = "YOUR_TWILIO_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"

# 1. Stock Data Fetch
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,  
    "apikey": STOCK_API_KEY,  
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]  
# 2. Yesterday's closing price
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]  
print(f"Yesterday: {yesterday_closing_price}")

# 3. Day before yesterday's closing price
day_before_yesterday_data = data_list[1] 
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(f"Day before: {day_before_yesterday_closing_price}")

# 4. Difference and percentage
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(f"Difference: {difference}")

diff_percent = (difference / float(yesterday_closing_price)) * 100
print(f"Percentage: {diff_percent}%")

# 5. If stock changed > 4%, get news
if diff_percent > 4:
    news_params = {  
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = response.json()["articles"]
    print(f"Total articles: {len(articles)}")

    # 6. Get first 3 articles
    three_articles = articles[:3]
    
    # 7. Format articles
    formatted_articles = [
        f"Headline: {article['title']}.\nBrief: {article['description']}" 
        for article in three_articles
    ]

    # 8. Send SMS via Twilio
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create( 
            body=article,
            from_="+1234567890", 
            to="+1439583023"  
        )
        print(f"✅ SMS sent: {message.sid}")
else:
    print("📊 Stock didn't move enough for news alert.")