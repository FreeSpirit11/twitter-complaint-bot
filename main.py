from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import os

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = PROMISED_UP
        self.down = PROMISED_DOWN
        self.actions = ActionChains(self.driver)

    def get_internet_speed(self):

        self.driver.execute_script("window.open('https://www.speedtest.net/', '_blank');")
        self.driver.switch_to.window(self.driver.window_handles[1])

        time.sleep(100)
        try:
            start_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
            start_button.click()
        except ElementClickInterceptedException or NoSuchElementException :
            privacy_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
            privacy_button.click()
            time.sleep(10)
            start_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
            start_button.click()
        except StaleElementReferenceException:
            print("element class got changed.")
        time.sleep(100)
        down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        print(f"down: {down}")

        up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print(f"up: {up}")

        return f"{down}down/{up}up"

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        sign_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main'                                                 '/div/div/div[1]/div'
                                                     '/div/div[3]/div[5]/a')
        sign_in.click()
        time.sleep(30)

        email = self.driver.find_element(By.CSS_SELECTOR, 'input[name="text"]')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)

        time.sleep(20)
        password = self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"][type="password"]')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)

        self.actions.move_by_offset(100,200).click().perform()

        time.sleep(10)
        post_icon =self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        post_icon.click()
        time.sleep(10)
        text = f"Hey Internet Provider, why is my internet speed {self.get_internet_speed()} when i pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"

        time.sleep(2)
        twitter_window = self.driver.window_handles[0]
        self.driver.switch_to.window(twitter_window)

        time.sleep(6)
        message = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        message.send_keys(text)
        time.sleep(10)
        post = self.driver.find_element(By.CSS_SELECTOR,
                                           'div[data-testid="tweetButton"] span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0')
        post.click()


bot = InternetSpeedTwitterBot()
bot.tweet_at_provider()

