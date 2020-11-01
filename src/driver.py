import threading
import logging
import sys

from src.utils import *
from src.browser import *
from src.config import *


class Driver(threading.Thread):

    sent_messages = 0

    def __init__(self, manager, id, account):
        threading.Thread.__init__(self)
        self.manager = manager
        self.driver = create_browser(BROWSER_VERSION, DISPLAY_BROWSER)
        self.account = account
        self.id = id
        self.start()


    def run(self):
        logging.info('Thread-{0}: Starting'.format(self.id))

        self.manager.set_account_status(self.account, 'status', 'login')

        try:
            self.login()
        except Exception as e:
            self.manager.set_account_status(self.account, 'status', 'login fail')
            logging.info('Thread-{0}: Error login'.format(self.id))
            sys.exit()


        logging.info("Thread-{0}: Finish login".format(self.id))
        while True:
            self.send_message(random_choose(MESSAGES))
            self.sent_messages += 1
            self.manager.set_account_status(self.account, 'sent_messages', self.sent_messages)
            random_delay(5)

        logging.info('Thread-{0}: Exiting'.format(self.id))


    def login(self):

        

        # go to youtube homepage
        self.driver.get('https://www.youtube.com/')
        logging.debug("{0}: Enter {1}".format(self.account[0], self.driver.title))
        wait_appear_and_click(self.driver, 'Login-Button (Youtube)', (By.XPATH, '//*[@id="buttons"]/ytd-button-renderer/a'))

        # login
        wait_appear_and_send_keys(self.driver, 'Email-Input', (By.XPATH, "//input[@id='identifierId']"), self.account[0])                     # type email
        wait_appear_and_click(self.driver, "Next-Button (username page)", (By.ID, 'identifierNext'))                                          # click next
        wait_appear_and_send_keys(self.driver, 'Password-Input', (By.CSS_SELECTOR, 'div#password input[name="password"]'), self.account[1])   # type password
        wait_appear_and_click(self.driver, "Next-Button (password page)", (By.ID, 'passwordNext'))                                            # click next
        random_delay(4)

        # set ytb info, first time login setup
        self.driver.get('https://www.youtube.com/create_channel')
        try:
            wait_appear_and_click(self.driver, "Create-Channel", (By.XPATH, '//*[@id="create-channel-identity-dialog"]/form/div[2]/div/button[2]'))                                     # click next
            logging.debug("{0}: First time login".format(self.account[0]))
            random_delay(5)
        except:
            logging.debug("{0}: Not first time login".format(self.account[0]))
        
        # enter stream
        self.driver.get(TARGET_STREAMING)
        logging.debug("{0}: Enter {1}".format(self.account[0], self.driver.title))

        # enter chatframe
        wait_and_enter_frame(self.driver, 'chatframe', (By.XPATH, '//*[@id="chatframe"]'))

        self.manager.set_account_status(self.account, 'status', 'active')

        


    def send_message(self, message):
        message = "装甲集群压力测试: Thread-{0}: {1}".format(self.id, message)
        wait_appear_and_send_keys(self.driver, 'Message-Input', (By.ID, 'input'), message)                     # type message
        wait_appear_and_click(self.driver, "Send-Button (streaming)", (By.XPATH, '//*[@id="send-button"]'))    # click send
        logging.debug("{0}: Send message <{1}>".format(self.account[0], message))