import time
import logging
from src.driver import *
import threading

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


accounts = get_accounts('./accounts.txt')
TARGET_STREAMING = "https://www.youtube.com/watch?v=WinQpGPnSdI"
BROWSER_VERSION = 'src/drivers/chromedriver_mac_86'


count = 0
lock = threading.Lock()

class Thread(threading.Thread):
    def __init__(self, t, *args):
        threading.Thread.__init__(self, target=t, args=args)
        self.start()

def run_driver(account):
    driver = Driver(browser_version=BROWSER_VERSION, display_window=False, target=TARGET_STREAMING)
    driver.login(username=account[0], password=account[1])
    driver.send_message("Multithreading chrome headless test")
    delay(10)
    driver.send_message("msg2")
    delay(10)
    driver.driver.quit()

tasks = []
for account in accounts:
    print(account[0])
    # tasks.append(Thread(run_driver, account))
    # delay(10)
