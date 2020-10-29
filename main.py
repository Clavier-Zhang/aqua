import logging
from src.driver import *
from src.utils import *
from src.manager import *
import sys
import time


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%I:%M:%S %p')


accounts = get_accounts('./accounts.txt')
messages = get_messages('./messages.txt')

# TARGET_STREAMING = "https://www.youtube.com/watch?v=WinQpGPnSdI"
TARGET_STREAMING = "https://www.youtube.com/watch?v=MWEINPVWv2I"
# BROWSER_VERSION = 'src/drivers/chromedriver_mac_86'
BROWSER_VERSION = 'src/drivers/chromedriver.exe'


manager = Manager(accounts=get_accounts('./accounts.txt'),
                  messages=get_messages('./messages.txt'),
                  target=TARGET_STREAMING,
                  display_window=True,
                  browser_version=BROWSER_VERSION)
