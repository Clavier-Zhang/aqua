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

TIME_OUT = 20


def create_browser(browser_version, display_window):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('window-size=1915x1068')          
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36")
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
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