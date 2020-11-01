import logging
from src.utils import *

# 浏览器版本
BROWSER_VERSION = 'src/drivers/chromedriver_mac_86'

# TARGET_STREAMING = "https://www.youtube.com/watch?v=WinQpGPnSdI"
# 目标油管直播间
TARGET_STREAMING = "https://www.youtube.com/watch?v=MWEINPVWv2I&feature=youtu.be&ab_channel=helloWorld"

# 是否显示浏览器
DISPLAY_BROWSER = False

# 是否打印日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%I:%M:%S %p')

# 谷歌账户
ACCOUNTS = get_accounts('./accounts.txt')

# 弹药库
MESSAGES = get_messages('./messages.txt')