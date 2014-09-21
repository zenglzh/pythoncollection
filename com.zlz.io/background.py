'''
Created on 2014-9-9
@see https://bitbucket.org/agronholm/apscheduler/src/0630eaaab4521ac42cc6eb85902b4df7033ebc52/examples/schedulers/background.py?at=master
@author: zenglizhi
'''
from apscheduler.schedulers.background import BackgroundScheduler

from datetime import datetime
import time
import os


def tick():
    print('Tick! The time is :%s ' % datetime.now())
    
if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick,'interval',seconds=3)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name =='nt' else 'C'))
    
    try:
        # This is here to simulate application activity (which keeps the main thread)
        
        while True:
            time.sleep(2)
    except (KeyboardInterrupt,SystemExit):
        scheduler.shutdown()# Not strictly necessary if dameonic mode is enabled