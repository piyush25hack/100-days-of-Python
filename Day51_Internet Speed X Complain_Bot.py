from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# ---------- CONFIGURATION ----------
PROMISED_DOWN = 100  # Mbps - jo ISP ne promise kiya
PROMISED_UP = 20     # Mbps
TWITTER_EMAIL = "your_twitter_email"
TWITTER_PASSWORD = "your_twitter_password"
PROVIDER_HANDLE = "@YourISP"  # e.g., @JioCare, @Airtel_Presence


class InternetSpeedXBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        """Speedtest.net se speed scrape karo"""
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)

        # "Go" button click karo
        go_button = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a'
        )
        go_button.click()
        print("⏳ Speed test running...")

        # Test complete hone ka wait karo (approx 60 seconds)
        time.sleep(60)

        # Download speed scrape karo
        try:
            self.down = self.driver.find_element(
                By.XPATH,
                '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'
            ).text
            self.down = float(self.down)
        except:
            self.down = 0

        # Upload speed scrape karo
        try:
            self.up = self.driver.find_element(
                By.XPATH,
                '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
            ).text
            self.up = float(self.up)
        except:
            self.up = 0

        print(f"📊 Download: {self.down} Mbps")
        print(f"📊 Upload: {self.up} Mbps")
        return self.down, self.up

    def tweet_at_provider(self):
        """Twitter/X pe complaint tweet karo [citation:5]"""
        self.driver.get("https://x.com/i/flow/login")
        time.sleep(3)

        # Email enter karo
        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@autocomplete="email"]'))
        )
        email_field.send_keys(TWITTER_EMAIL)
        email_field.send_keys(Keys.ENTER)
        time.sleep(2)

        # Password enter karo
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@autocomplete="current-password"]'))
        )
        password_field.send_keys(TWITTER_PASSWORD)
        password_field.send_keys(Keys.ENTER)
        time.sleep(5)

        # Tweet button click karo
        tweet_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-testid="tweetButtonInline"]'))
        )
        tweet_button.click()
        time.sleep(2)

        # Tweet text area find karo
        tweet_text = self.driver.find_element(
            By.XPATH, '//*[@data-testid="tweetTextarea_0"]'
        )

        # Complaint tweet likho [citation:1]
        tweet_content = f"""Hey {PROVIDER_HANDLE}, why is my internet so slow?

        Promised: {PROMISED_DOWN} Mbps
        Actual: {self.down} Mbps
        Upload: {self.up} Mbps

        This is unacceptable! #SlowInternet #ISP #Complaint"""

        tweet_text.send_keys(tweet_content)
        time.sleep(2)

        # Tweet post karo
        post_button = self.driver.find_element(
            By.XPATH, '//*[@data-testid="tweetButton"]'
        )
        post_button.click()
        print("✅ Tweet posted successfully!")

    def run(self):
        """Bot run karo [citation:2]"""
        self.get_internet_speed()

        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            print("🔊 Speed below promised! Posting complaint...")
            self.tweet_at_provider()
        else:
            print("✅ Speed is good! No complaint needed.")


# ---------- RUN THE BOT ----------
if __name__ == "__main__":
    bot = InternetSpeedXBot()
    bot.run()
    # bot.driver.quit()  # Browser close karne ke liye uncomment