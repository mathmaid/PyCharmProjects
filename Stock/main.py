import os
import sys
os.chdir('Stock')
sys.path.append(os.getcwd())
import time
import random

from getStock import getStockInfo,updateStockHistoryDeal

if __name__ == '__main__':
    df = getStockInfo()
    for item in df['dm']:
        print(item)
        updateStockHistoryDeal(item)
        time.sleep(random.randint(10,15))
