from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class GymBookingBot:
    def __init__(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, email, password, login_url):
        """Gym portal mein login karo"""
        self.driver.get(login_url)
        time.sleep(2)
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)

    def book_class(self, class_time, class_date):
        """Specific class book karo"""
        try:
            classes = self.driver.find_elements(By.CLASS_NAME, "class-card")
            for class_item in classes:
                if class_time in class_item.text and class_date in class_item.text:
                    if "Available" in class_item.text:
                        class_item.find_element(By.CLASS_NAME, "book-btn").click()
                        print(f"✅ Booked class at {class_time} on {class_date}")
                        return True
            print("❌ Class not available")
            return False
        except Exception as e:
            print(f"❌ Booking failed: {e}")
            return False

    def close(self):
        self.driver.quit()

# Example
bot = GymBookingBot()
bot.login("your_email@example.com", "your_password", "https://gym-portal.com/login")
bot.book_class("6:00 PM", "2026-08-22")
bot.close()