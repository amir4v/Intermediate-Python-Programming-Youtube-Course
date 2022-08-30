# Threading: multiple-threads, share data between threads, how to use locks to prevent raise conditions, deamon process, how to use queue for thread safe data exchange

from threading import Thread, Lock
from queue import Queue

if __name__ == "__main__":
    q = Queue()
    q.put(1)
    q.put(2)
    # 2 1
    first = q.get() # front
    print(first) # 1
    e = q.empty() # is the Queue Empty -> bool
    print(e) # False
    
    q.task_done() # tells the queue that the processing on the task is complete.
    q.join() # Blocks until all items in the Queue have been gotten and processed.
