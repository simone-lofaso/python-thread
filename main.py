import threading
import time

def thread1():
    for i in range(11):
        print("Thread 1: " , i)
        time.sleep(1)
    
    
def Thread2():
    for i in range(11):
        print("Thread 2: " , 10 - i)
        time.sleep(1)
    
Thread1 = threading.Thread(target = thread1)
Thread2 = threading.Thread(target = Thread2)
Thread1.start()
Thread2.start()
