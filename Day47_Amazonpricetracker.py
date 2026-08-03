import requests
from bs4 import BeautifulSoup
import smtplib
import os
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Email Configuration
EMAIL = os.environ.get("EMAIL")
APP_PASSWORD = os.environ.get("APP_PASSWORD")
TO_EMAIL = os.environ.get("TO_EMAIL")

# Product Configuration
PRODUCT_URL = os.environ.get("PRODUCT_URL")
TARGET_PRICE = float(os.environ.get("TARGET_PRICE", 50000))


def get_product_price(url):
    """
    Fetch product price from Amazon
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Try multiple selectors for price
        price_selectors = [
            "span.a-price-whole",
            "span.a-offscreen",
            "span#priceblock_ourprice",
            "span#priceblock_dealprice",
            "span.a-price span.a-offscreen"
        ]
        
        price = None
        for selector in price_selectors:
            try:
                price_element = soup.select_one(selector)
                if price_element:
                    price_text = price_element.get_text().strip()
                    # Clean price text
                    price_text = price_text.replace("₹", "").replace(",", "").replace(" ", "").strip()
                    if price_text:
                        price = float(price_text)
                        break
            except:
                continue
        
        if price is None:
            print("❌ Could not find price. Website structure may have changed.")
            return None
            
        return price
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Request error: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None


def get_product_title(url):
    """
    Get product title from Amazon
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    }
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        
        title_selectors = [
            "span#productTitle",
            "h1#title",
            "h1.a-size-large"
        ]
        
        for selector in title_selectors:
            title_element = soup.select_one(selector)
            if title_element:
                title = title_element.get_text().strip()
                if title:
                    return title[:100]  # Limit length
        
        return "Unknown Product"
        
    except:
        return "Unknown Product"


def send_email(subject, body):
    """
    Send email notification
    """
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=APP_PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=TO_EMAIL,
                msg=f"Subject: {subject}\n\n{body}"
            )
        print(f"✅ Email sent to {TO_EMAIL}")
        return True
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return False


def log_price(product_title, current_price, target_price):
    """
    Log price to file
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} | {product_title[:30]} | ₹{current_price} | Target: ₹{target_price}\n"
    
    try:
        with open("price_history.txt", "a") as file:
            file.write(log_entry)
        print(f"📝 Logged: {log_entry.strip()}")
    except:
        pass


def send_sms(message):
    """
    Send SMS notification (Twilio)
    """
    try:
        from twilio.rest import Client
        
        TWILIO_SID = os.environ.get("TWILIO_SID")
        TWILIO_AUTH = os.environ.get("TWILIO_AUTH_TOKEN")
        TWILIO_PHONE = os.environ.get("TWILIO_PHONE")
        YOUR_PHONE = os.environ.get("YOUR_PHONE")
        
        if not all([TWILIO_SID, TWILIO_AUTH, TWILIO_PHONE, YOUR_PHONE]):
            print("⚠️ Twilio credentials not set. SMS not sent.")
            return False
            
        client = Client(TWILIO_SID, TWILIO_AUTH)
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE,
            to=YOUR_PHONE
        )
        print(f"✅ SMS sent! SID: {message.sid}")
        return True
        
    except Exception as e:
        print(f"❌ SMS failed: {e}")
        return False


def main():
    print("\n" + "="*50)
    print("🛒 AMAZON PRICE TRACKER 🛒")
    print("="*50 + "\n")
    
    print(f"📦 Tracking: {PRODUCT_URL}")
    print(f"🎯 Target Price: ₹{TARGET_PRICE}")
    print("-" * 50)
    
    # Get product title
    product_title = get_product_title(PRODUCT_URL)
    print(f"📝 Product: {product_title}")
    
    # Get current price
    current_price = get_product_price(PRODUCT_URL)
    
    if current_price is None:
        print("❌ Could not get price. Exiting...")
        return
    
    print(f"💰 Current Price: ₹{current_price}")
    print(f"🎯 Target Price: ₹{TARGET_PRICE}")
    print("-" * 50)
    
    # Log price
    log_price(product_title, current_price, TARGET_PRICE)
    
    # Check if price is below target
    if current_price < TARGET_PRICE:
        print("🔊 PRICE DROP ALERT! 🔊")
        
        # Build notification message
        discount = ((TARGET_PRICE - current_price) / TARGET_PRICE) * 100
        message = f"""
🔊 AMAZON PRICE DROP ALERT! 🔊

📦 Product: {product_title}
💰 Current Price: ₹{current_price}
🎯 Target Price: ₹{TARGET_PRICE}
📉 Discount: {discount:.1f}%
🔗 Link: {PRODUCT_URL}

Buy now before price goes up!
        """
        
        # Send email notification
        subject = f"🛒 Price Drop! ₹{current_price} - {product_title[:30]}..."
        send_email(subject, message)
        
        # Send SMS (if configured)
        send_sms(message[:160])  # SMS length limit
        
        print("\n" + "="*50)
        print("🎉 ALERT SENT! Check your email/SMS!")
        print("="*50)
        
    else:
        print(f"📊 Price is still above target.")
        difference = current_price - TARGET_PRICE
        print(f"📉 Need ₹{difference:.2f} more drop to reach target.")
        
        if current_price > TARGET_PRICE:
            print("⏳ Keep waiting for the price to drop...")
        else:
            print("✅ Price is at or below target!")
    
    print("\n" + "="*50)
    print("🛒 Tracker run complete!")
    print("="*50)


if __name__ == "__main__":
    main()