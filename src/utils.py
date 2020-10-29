from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.keys import Keys
import time
from random import randint
import logging
import requests
from src.utils import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
TIME_OUT = 20

def random_choose(arr):
    return arr[randint(0, len(arr) - 1)]

def get_accounts(path):
    accounts = []
    f = open(path, 'r')
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue
        data = line.split()
        accounts.append((data[0], data[1]))
    return accounts

def get_messages(path):
    messages = []
    f = open(path, 'r')
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue
        messages.append(line)
    return messages

def random_delay(n):
    time.sleep(n + randint(1, 3))

def delay(n):
    time.sleep(n)

def create_browser(browser_version, display_window):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('window-size=1920x1080')
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36")
    # chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36")
    if not display_window:
        chrome_options.headless = True
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("-—disable-gpu")
    return webdriver.Chrome(executable_path=browser_version, options=chrome_options)


def wait_appear_and_click(driver, name, selector):
    logging.debug('Looking for <{0}>'.format(name))
    WebDriverWait(driver, TIME_OUT).until(                     
        expect.presence_of_element_located(selector) ,  # wait for element to appear
    )
    WebDriverWait(driver, TIME_OUT).until(                     
        expect.element_to_be_clickable(selector)        # wait for element clickable
    )
    driver.find_element(*selector).click()              # click element
    logging.debug('Click <{0}>'.format(name))

def wait_appear_and_send_keys(driver, name, selector, keys):
    logging.debug('Looking for <{0}>'.format(name))
    WebDriverWait(driver, TIME_OUT).until(                    # wait for element to appear
        expect.presence_of_element_located(selector) ,
    )
    WebDriverWait(driver, TIME_OUT).until(                    # wait for element to appear
        expect.visibility_of_element_located(selector),
    )
    WebDriverWait(driver, TIME_OUT).until(                    # wait for element to appear
        expect.element_to_be_clickable(selector)        # wait for element clickable
    )
    driver.find_element(*selector).send_keys(keys)      # send msg
    logging.debug('Send <{0}> to <{1}>'.format(keys, name))

def wait_appear(driver, name, selector):
    logging.debug('Looking for <{0}>'.format(name))
    WebDriverWait(driver, TIME_OUT).until(                    # wait for element to appear
        expect.presence_of_element_located(selector) 
    )
    logging.debug('Found <{0}>'.format(name))


def wait_and_enter_frame(driver, name, selector):
    logging.debug('Looking for iframe:<{0}>'.format(name))
    WebDriverWait(driver, TIME_OUT).until(
        expect.presence_of_element_located(selector),       # wait charframe to appear
    )
    iframe = driver.find_element(*selector)                 # locate chatframe, cannot use id to select frame
    driver.switch_to.frame(iframe)                          # enter chatframe
    logging.debug('Enter iframe:<{0}>'.format(name))