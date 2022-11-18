# Multiprocessing: data between processes, lock, queue, process pool

from multiprocessing import Process
from multiprocessing import Queue # This Queue does not have .task_done() and .join() methods
import time

def square(numbers, q):
    for i in numbers:
        q.put(i*i)

def make_negative(numbers, q):
    for i in numbers:
        q.put(-1*i)

if __name__ == "__main__":
    
    numbers = range(1,6)
    q = Queue()
    
    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers, q))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    while(not q.empty()):
        print(q.get())

"""
1
4
9
16
25
-1
-2
-3
-4
-5
"""
