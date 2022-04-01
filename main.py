import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWNLOAD_SPEED = 150
PROMISED_UPLOAD_SPEED = 10
CHROME_DRIVER_PATH = r"C:\selenium_web_driver\chromedriver.exe"
TWITTER_USERNAME = "T_USERNAME"
TWITTER_PASSWORD = "T_PASSWORD"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.down = 0
        self.up = 0

    # tests internet speed
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        go_button = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                             '1]/a/span[4]')
        go_button.click()

        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                       '3]/div/div[3]/div/div/div[2]/div[1]/'
                                                       'div[2]/div/div[2]/span').text

        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                     '3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")

        # sign in button
        time.sleep(10)
        sign_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div['
                                                     '1]/div/div[3]/div[5]/a/div/span/span')
        sign_in.click()

        # enters email
        time.sleep(5)
        email_entry = self.driver.find_element(By.NAME, 'text')
        email_entry.send_keys(TWITTER_USERNAME)
        email_entry.send_keys(Keys.ENTER)

        # enters password
        time.sleep(20)
        password_entry = self.driver.find_element(By.NAME, 'password')
        password_entry.send_keys(TWITTER_PASSWORD)
        password_entry.send_keys(Keys.ENTER)

        time.sleep(20)
        compose_tweet = self.driver.find_element(By.XPATH,
                                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                                 '2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                 '1]/div/div/div/div/div/div/div/div/div/label/div['
                                                 '1]/div/div/div/div/div[ '
                                                 '2]/div/div/div/div')
        time.sleep(20)
        complaint = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay" \
                    f" for {PROMISED_DOWNLOAD_SPEED}down/{PROMISED_UPLOAD_SPEED}up? "
        compose_tweet.send_keys(complaint)

        time.sleep(20)
        final_tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div['
                                                                '2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                                                                '1]/div/div/div/div[2]/div[3]/div/div/div['
                                                                '2]/div/div/span/span')
        final_tweet_button.click()
        time.sleep(80)
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
