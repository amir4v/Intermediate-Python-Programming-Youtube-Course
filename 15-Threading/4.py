# Threading: multiple-threads, share data between threads, how to use locks to prevent raise conditions, deamon process, how to use queue for thread safe data exchange

from threading import Thread, Lock
import time

database_value = 0

def increase(lock):
    global database_value
    
    with lock:
        # ( some processing
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1) # )
        database_value = local_copy

if __name__ == "__main__":
    
    lock = Lock()

    print("start")

    
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print("end value", database_value)
    
    print("end main")

"""
start
end value 2
end main
"""
