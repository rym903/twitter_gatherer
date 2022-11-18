import os
from dotenv import load_dotenv
import tweepy
import time

# from fake_useragent import UserAgent
from selenium import webdriver

# from selenium.webdriver.common.by import By


# def crawler(request=""):
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     options.add_argument("--disable-gpu")
#     options.add_argument("--window-size=1280x1696")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--hide-scrollbars")
#     options.add_argument("--enable-logging")
#     options.add_argument("--log-level=0")
#     options.add_argument("--v=99")
#     options.add_argument("--single-process")
#     options.add_argument("--ignore-certificate-errors")
#     options.add_argument("--disable-dev-shm-usage")
#     # options.add_argument("user-agent=" + UserAgent().random)
#     options.binary_location = os.getcwd() + "/headless-chromium"
#     driver = webdriver.Chrome(os.getcwd() + "/chromedriver", chrome_options=options)

#     driver.get("https://en.wikipedia.org/wiki/Special:Random")
#     line = driver.find_element_by_class_name("firstHeading").text
#     print(line)
#     driver.quit()
#     return line


def auth(request=""):
    """seleniumの初期化と、twitter APIのauth

    Returns:
        driver: selenium driver
        api: twitter api (認証済み)
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--no-sandbox")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--enable-logging")
    options.add_argument("--log-level=0")
    options.add_argument("--v=99")
    options.add_argument("--single-process")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-dev-shm-usage")
    options.binary_location = os.getcwd() + "/headless-chromium"
    driver = webdriver.Chrome(os.getcwd() + "/chromedriver", chrome_options=options)

    # 認証情報の読み込み
    # TODO: google secretsからの読み込み
    load_dotenv()
    consumer_key = os.getenv("API_KEY")
    consumer_secret = os.getenv("API_SECRET_KEY")
    access_key = os.getenv("ACCESS_TOKEN")
    access_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    driver.get("https://t.co/RYqUGZXmqh")
    time.sleep(5)

    res = f"""
        {api.verify_credentials().screen_name}
        
        {driver.page_source}
        """
    # return driver, api
    return res
