# Threading: multiple-threads, share data between threads, how to use locks to prevent raise conditions, deamon process, how to use queue for thread safe data exchange

from threading import Thread, current_thread, Lock
from queue import Queue

def worker(q, lock):
    while(True):
        value = q.get()
        with lock:
            print(f"in {current_thread().name} got {value}")
        q.task_done()

if __name__ == "__main__":
    q = Queue()
    lock = Lock()
    num_threads = 10
    
    for i in range(10):
        thread = Thread(target=worker, args=(q,lock))
        # Deamon-Thread will die when Main-Thread dies
        thread.deamon = True # (by default is False) , deamon thread will die when main thread dies
        thread.start()
    
    for i in range(1, 21):
        q.put(i)
    
    q.join()
    
    print("end main")

"""
in Thread-5 (worker) got 1
in Thread-6 (worker) got 2
in Thread-7 (worker) got 3
in Thread-2 (worker) got 4
in Thread-8 (worker) got 5
in Thread-3 (worker) got 6
in Thread-9 (worker) got 7
in Thread-1 (worker) got 8
in Thread-4 (worker) got 9
in Thread-4 (worker) got 19
in Thread-5 (worker) got 11
in Thread-6 (worker) got 12
in Thread-7 (worker) got 13
in Thread-2 (worker) got 14
in Thread-8 (worker) got 15
in Thread-3 (worker) got 16
in Thread-9 (worker) got 17
in Thread-1 (worker) got 18
in Thread-4 (worker) got 20
in Thread-10 (worker) got 10
end main
|
"""
