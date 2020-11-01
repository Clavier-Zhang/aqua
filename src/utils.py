import time
from random import randint


# random choose an item from the list
def random_choose(arr):
    return arr[randint(0, len(arr) - 1)]


# load accounts from the file
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


# load messages from the file
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


# thread wait (with some random time)
def random_delay(n):
    time.sleep(n + randint(1, 3))


# thread wait
def delay(n):
    time.sleep(n)
