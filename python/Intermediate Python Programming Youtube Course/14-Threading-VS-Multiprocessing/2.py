# Threading-VS-Multiprocessing: You can run code in parallel

# Multiprocessing

from multiprocessing import Process
import os

processes = []
num_processes = os.cpu_count()

def square_numbers():
# def square_numbers(a):
    for i in range(100):
        i*i

for i in range(num_processes):
    p = Process(target=square_numbers)
    # p = Process(target=square_numbers, args=1,)
    processes.append(p)

# start
for p in processes:
    p.start()

# join
for p in processes:
    p.join() # this will block the main thread until this process finished
