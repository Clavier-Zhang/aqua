from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.keys import Keys
import time
from random import randint
import logging
from src.utils import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

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

def delay(n):
    time.sleep(randint(2, n))

def wait_appear_and_click(driver, name, selector):
    # logging.info('Looking for <{0}>'.format(name))
    WebDriverWait(driver, 10).until(                     
        expect.presence_of_element_located(selector) ,  # wait for element to appear
    )
    WebDriverWait(driver, 10).until(                     
        expect.element_to_be_clickable(selector)        # wait for element clickable
    )
    driver.find_element(*selector).click()              # click element
    # logging.info('Click <{0}>'.format(name))

def wait_appear_and_send_keys(driver, name, selector, keys):
    # logging.info('Looking for <{0}>'.format(name))
    WebDriverWait(driver, 10).until(                    # wait for element to appear
        expect.presence_of_element_located(selector) ,
    )
    WebDriverWait(driver, 10).until(                    # wait for element to appear
        expect.visibility_of_element_located(selector),
    )
    WebDriverWait(driver, 10).until(                    # wait for element to appear
        expect.element_to_be_clickable(selector)        # wait for element clickable
    )
    driver.find_element(*selector).send_keys(keys)      # send msg
    # logging.info('Send <{0}> to <{1}>'.format(keys, name))

def wait_appear(driver, name, selector):
    # logging.info('Looking for <{0}>'.format(name))
    WebDriverWait(driver, 10).until(                    # wait for element to appear
        expect.presence_of_element_located(selector) 
    )
    # logging.info('Found <{0}>'.format(name))


# enter chatframe
def wait_and_enter_frame(driver, name, selector):
    # logging.info('Looking for iframe:<{0}>'.format(name))
    WebDriverWait(driver, 10).until(
        expect.presence_of_element_located(selector),       # wait charframe to appear
    )
    iframe = driver.find_element(*selector)                 # locate chatframe, cannot use id to select frame
    driver.switch_to.frame(iframe)                                                    # enter chatframe
    # logging.info('Enter iframe:<{0}>'.format(name))