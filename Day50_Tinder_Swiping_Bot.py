from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

# Tinder Open
driver.get("https://tinder.com")
time.sleep(3)

# Login Button Click
login_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()
time.sleep(2)

# Facebook Login Option
fb_login = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()
time.sleep(3)

# Switch to Facebook Login Window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# Facebook Credentials
email = driver.find_element(By.ID, "email")
email.send_keys("your_facebook_email")

password = driver.find_element(By.ID, "pass")
password.send_keys("your_facebook_password")
password.send_keys(Keys.ENTER)
time.sleep(5)

# Switch back to Tinder
driver.switch_to.window(base_window)
time.sleep(5)

# Allow Location
allow_location = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location.click()
time.sleep(2)

# Allow Notifications
notifications = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications.click()
time.sleep(2)

# Start Swiping
for _ in range(100):
    try:
        like_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
        time.sleep(0.5)
    except:
        # Skip if no profile
        try:
            close_button = driver.find_element(By.CLASS_NAME, "its-a-match")
            close_button.click()
        except:
            pass
        time.sleep(1)

print("✅ Swiping complete!")
# driver.quit()