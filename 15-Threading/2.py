# Threading: multiple-threads, share data between threads, how to use locks to prevent raise conditions, deamon process, how to use queue for thread safe data exchange

from threading import Thread
import time

database_value = 0

def increase():
    global database_value
        
    # some processing
    local_copy = database_value
    local_copy += 1
    time.sleep(0.1)
    
    database_value = local_copy

if __name__ == "__main__":
    
    print("start")
    
    thread1 = Thread(target=increase)
    thread2 = Thread(target=increase)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print("end value", database_value)
    
    print("end main")

"""
start
end value 1
end main
"""
# Point of this example: end value == 1
