# Multiprocessing: data between processes, lock, queue, process pool

from multiprocessing import Process, Value, Array, Lock
import time

def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1

if __name__ == "__main__":
    shared_number = Value('i', 0) # 'i'==int , 0==default-value
    print(f"Number at beginning is {shared_number.value}")
    
    lock = Lock()
    
    process1 = Process(target=add_100, args=(shared_number,lock))
    process2 = Process(target=add_100, args=(shared_number,lock))
    
    process1.start()
    process2.start()
    
    process1.join()
    process2.join()
    
    print(f"Number at end is {shared_number.value}")

"""
Number at beginning is 0
Number at end is 200
"""
