import threading
from src.utils import *
from src.driver import *
from prettytable import PrettyTable

class Manager(threading.Thread):

    accounts_status = {}
    accounts_status_lock = threading.Lock()
    

    def __init__(self, accounts, messages, target, display_window, browser_version):
        threading.Thread.__init__(self)
        self.accounts_status = self.create_accounts_status(accounts)
        self.accounts = accounts
        self.messages = messages
        self.target = target
        self.browser_version = browser_version
        self.display_window = display_window
        self.start()

    
    def create_accounts_status(self, accounts):
        count = 0
        status = {}
        for account in accounts:
            status[account[0]] = {
                'id': count,
                'email': account[0],
                'status': 'inactive',
                'retries': 0,
                'sent_messages': 0,
                'password': account[1]
            }
            count += 1
        return status

    def set_account_status(self, account, key, val):
        self.accounts_status_lock.acquire()
        self.accounts_status[account[0]][key] = val
        self.accounts_status_lock.release()

    def print_account_status(self):
        table = PrettyTable(['ID', 'Email', 'Status', 'Retries', 'Sent Messages', 'Password'])
        for account in self.accounts_status:
            table.add_row(self.accounts_status[account].values())
        print(table)


    def run(self):
        for account in self.accounts:
            Driver(browser_version=self.browser_version, 
                   display_window=self.display_window, 
                   target=self.target,
                   id=self.accounts_status[account[0]]['id'],
                   manager=self,
                   account=account,
                   messages=self.messages)

        while True:
            self.print_account_status()
            delay(10)


