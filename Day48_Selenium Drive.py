from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://web.telegram.org")

# Maximize window
driver.maximize_window()

# Wait for page to load
time.sleep(120)

# Get page title
print(f"📄 Page Title: {driver.title}")

# Search for something
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("laptop")
search_box.submit()

# Wait for results
time.sleep(3)

# Print results
results = driver.find_elements(By.CSS_SELECTOR, "h2 a")
for result in results[:5]:
    print(f"🔗 {result.text}")

# Close browser
driver.quit()