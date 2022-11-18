# Threading-VS-Multiprocessing: You can run code in parallel

# Threading

from threading import Thread
import time

def square_numbers():
# def square_numbers(a):
    for i in range(100):
        i*i
        time.sleep(0.1)

threads = []
num_threads = 10

for i in range(num_threads):
    t = Thread(target=square_numbers)
    # t = Thread(target=square_numbers, args=1,)
    threads.append(t)

# start
for t in threads:
    t.start()

# join
for t in threads:
    t.join() # this will block the main thread until this process finished
