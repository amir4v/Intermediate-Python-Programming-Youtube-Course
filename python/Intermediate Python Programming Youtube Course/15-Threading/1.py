# Threading: multiple-threads, share data between threads, how to use locks to prevent raise conditions, deamon process, how to use queue for thread safe data exchange

from threading import Thread

def square_numbers():
    for i in range(100):
        i*i

if __name__ == "__main__":
    threads = []
    num_threads = 10
    
    # create threads
    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)
    
    # start threads
    for thread in threads:
        thread.start()
    
    # join threads: wait for them to complete
    for thread in threads:
        thread.join()
