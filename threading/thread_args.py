import threading
import time
from datetime import datetime

def heavy(data, name='a'):
    print(name)
    print(f'開始 {datetime.now()}')
    print(data)
    time.sleep(5)
    print(f'終了 {datetime.now()}')

if __name__ == '__main__':
    thread1 = threading.Thread(target=heavy, args=(5,), kwargs={'name':'mayuki'})
    thread1.start()
    thread2 = threading.Thread(target=heavy, args=(7,), kwargs={'name':'mayuki2'})
    thread2.start()
