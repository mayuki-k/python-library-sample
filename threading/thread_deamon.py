import threading
import time
from datetime import datetime

def heavy(time_num):
    print(f'開始 {datetime.now()}')
    time.sleep(time_num)
    print(f'終了 {datetime.now()}')

if __name__ == '__main__':
    thread1 = threading.Thread(target=heavy, args=(5, ))
    thread1.deamon = True
    thread1.start()
    
    thread2 = threading.Thread(target=heavy, args=(5,))
    thread2.deamon = True
    thread2.start()