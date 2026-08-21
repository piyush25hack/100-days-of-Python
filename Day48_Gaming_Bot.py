from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

# Game URL open karo
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)

# Language select karo (English)
language = driver.find_element(By.ID, "langSelect-EN")
language.click()
time.sleep(5)

# Cookie element find karo
cookie = driver.find_element(By.ID, "bigCookie")


timeout = time.time() + 300

print("🍪 Cookie Clicker Bot start ho gaya! 5 minute chalega...")

while time.time() < timeout:
    # Cookie click karo
    cookie.click()
    
    # Har 5 second pe upgrades check karo
    if int(time.time()) % 5 == 0:

        upgrades = driver.find_elements(By.CLASS_NAME, "product.unlocked")
        
        if upgrades:

            upgrades[-1].click()
            print("⬆️ Upgrade purchased!")

# Total cookies print karo
cookies = driver.find_element(By.ID, "cookies").text
print(f"🍪 Total Cookies: {cookies}")