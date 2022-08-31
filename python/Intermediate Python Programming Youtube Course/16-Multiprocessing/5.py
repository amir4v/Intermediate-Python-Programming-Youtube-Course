# Multiprocessing: data between processes, lock, queue, process pool

from multiprocessing import Process, Value, Array, Lock
import time

def add_100(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for j in range(len(numbers)):
            numbers[j] += 1

if __name__ == "__main__":
    shared_array = Array('d', [0.0, 100.0, 200.0]) # 'd'==double , [0.0, 100.0, 200.0]==default-value
    print(f"Array at beginning is {shared_array[:]}")
    
    lock = Lock()
    
    process1 = Process(target=add_100, args=(shared_array,lock))
    process2 = Process(target=add_100, args=(shared_array,lock))
    
    process1.start()
    process2.start()
    
    process1.join()
    process2.join()
    
    print(f"Array at end is {shared_array[:]}")

"""
Array at beginning is [0.0, 100.0, 200.0]
Array at end is [173.0, 289.0, 388.0]
"""
