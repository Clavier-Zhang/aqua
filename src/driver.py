from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.keys import Keys
import time
from random import randint
import logging

from src.utils import *


class Driver:

    driver = None

    target = None

    username = None

    def __init__(self, browser_version, display_window, target, name="unknown"):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('window-size=1920x1080')          
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36")
        if not display_window:
            chrome_options.headless = True
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("-—disable-gpu")
        self.driver = webdriver.Chrome(executable_path=browser_version, options=chrome_options)
        self.target = target
        self.name = name
        
    def login(self, username, password):

        self.username = username

        # go to stackoverflow
        logging.info('{0}: Login google account using Stackoverflow google login page'.format(self.username))                          # avoid security check
        
        self.driver.get('https://stackoverflow.com')
        wait_appear_and_click(self.driver, "Google-Login-Button (stackoverflow)", (By.XPATH, '/html/body/header/div/ol[2]/li[2]/a[1]'))
        wait_appear_and_click(self.driver, "Google-Login-Button (stackoverflow)", (By.XPATH, '//*[@id="openid-buttons"]/button[1]'))
        logging.info("{0}: Enter {1}".format(self.username, self.driver.title))

        # login
        wait_appear_and_send_keys(self.driver, 'Email-Input', (By.XPATH, "//input[@id='identifierId']"), username)                     # type email
        wait_appear_and_click(self.driver, "Next-Button (username page)", (By.ID, 'identifierNext'))                                   # click next
        wait_appear_and_send_keys(self.driver, 'Password-Input', (By.CSS_SELECTOR, 'div#password input[name="password"]'), password)   # type password
        wait_appear_and_click(self.driver, "Next-Button (password page)", (By.ID, 'passwordNext'))                                     # click next
        wait_appear(self.driver, 'Stackoverflow Home page', (By.ID, 'content'))                                                        # go to stackoverflow homepage

        # set ytb info, first time login setup
        self.driver.get('https://www.youtube.com/create_channel')
        try:
            wait_appear_and_click(self.driver, "Create-Channel", (By.XPATH, '//*[@id="create-channel-identity-dialog"]/form/div[2]/div/button[2]'))                                     # click next
            logging.info("{0}: First time login".format(self.username))
            delay(5)
        except:
            logging.info("{0}: Not first time login".format(self.username))
        
        # enter stream
        self.driver.get(self.target)
        logging.info("{0}: Enter {1}".format(self.username, self.driver.title))

        # enter chatframe
        wait_and_enter_frame(self.driver, 'chatframe', (By.XPATH, '//*[@id="chatframe"]'))


    def send_message(self, message):
        message = "Thread{0}: {1}".format(self.name, message)
        wait_appear_and_send_keys(self.driver, 'Message-Input', (By.ID, 'input'), message)                     # type message
        wait_appear_and_click(self.driver, "Send-Button (streaming)", (By.XPATH, '//*[@id="send-button"]'))    # click send
        logging.info("{0}: Send message <{1}>".format(self.username, message))