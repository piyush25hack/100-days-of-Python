# Import Libraries
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# ---------- STEP 1: SCRAPE DATA ----------
# Target URL - Example using a dummy site
# Real project mein yahan Zillow ya kisi rental site ka URL daalo
URL = "http://books.toscrape.com/"

# Headers add karo (anti-block ke liye)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Data extract karo (example: book titles aur prices)
titles = []
prices = []

# CSS selector se elements find karo
for book in soup.select("article.product_pod"):
    title = book.h3.a.get("title")
    price = book.select_one("p.price_color").text
    
    titles.append(title)
    prices.append(price)

# Structured data banao
data = {"Title": titles, "Price": prices}
df = pd.DataFrame(data)
print(f"✅ Scraped {len(df)} items!")
print(df.head())

# ---------- STEP 2: CSV SAVE ----------
df.to_csv("scraped_data.csv", index=False)
print("✅ Data saved to scraped_data.csv")

# ---------- STEP 3: DATA ENTRY AUTOMATION ----------
# Manually created Google Form ka URL
# Apna Google Form banao aur uski link yahan daalo
FORM_URL = "https://forms.gle/YOUR_GOOGLE_FORM_ID"

# Selenium setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

driver.get(FORM_URL)
time.sleep(3)

# CSV se data read karo
data = pd.read_csv("scraped_data.csv")

for index, row in data.iterrows():
    try:
        # Form fields find karo (Google Form ke structure ke hisaab se)
        # Pehle inspect karo Google Form mein actual field IDs
        title_field = driver.find_element(By.XPATH, '//input[@aria-label="Title"]')
        price_field = driver.find_element(By.XPATH, '//input[@aria-label="Price"]')
        
        # Data entry
        title_field.send_keys(row["Title"])
        price_field.send_keys(row["Price"])
        
        # Submit button
        submit_btn = driver.find_element(By.XPATH, '//span[text()="Submit"]')
        submit_btn.click()
        time.sleep(2)
        
        # Next entry ke liye "Submit another response"
        try:
            another_btn = driver.find_element(By.XPATH, '//a[text()="Submit another response"]')
            another_btn.click()
            time.sleep(2)
        except:
            driver.get(FORM_URL)
            time.sleep(2)
            
        print(f"✅ Entry {index+1} submitted!")
        
    except Exception as e:
        print(f"❌ Error in row {index}: {e}")

print("🎉 All data entry complete!")
# driver.quit()  # Uncomment to close browser