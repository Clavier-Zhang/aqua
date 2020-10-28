import time
import logging
from src.driver import *
from src.utils import *
import threading

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


accounts = get_accounts('./accounts.txt')
messages = get_messages('./messages.txt')

TARGET_STREAMING = "https://www.youtube.com/watch?v=WinQpGPnSdI"

# BROWSER_VERSION = 'src/drivers/chromedriver_mac_86'
BROWSER_VERSION = 'src/drivers/chromedriver.exe'

count = 0
lock = threading.Lock()
class Thread(threading.Thread):
    def __init__(self, t, *args):
        threading.Thread.__init__(self, target=t, args=args)
        self.start()

def task(driver, account):
    driver.login(username=account[0], password=account[1])
    for _ in range(5):
        delay(5)
        # driver.send_message(random_choose(messages))


drivers = []
threads = []
for i in range(len(accounts)):
    account = accounts[i]
    driver = Driver(browser_version=BROWSER_VERSION, 
                    display_window=False, 
                    target=TARGET_STREAMING,
                    name=str(i))
    driver.login(username=account[0], password=account[1])
    threads.append(Thread(task, driver, account))

    delay(2)               # avoid ip ban


# for driver in drivers:
#     threads.append(Thread(task, driver))


# print(get_proxy())