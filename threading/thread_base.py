import threading
import time
from datetime import datetime

def heavy():
    print(f'開始 {datetime.now()}')
    time.sleep(5)
    print(f'終了 {datetime.now()}')

if __name__ == '__main__':
    thread1 = threading.Thread(target=heavy)
    thread1.start()
    thread2 = threading.Thread(target=heavy)
    thread2.start()
