# Multiprocessing: data between processes, lock, queue, process pool

from multiprocessing import Process, Value, Array
import os

def square_numbers():
    for i in range(100):
        i*i

if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()
    # Number of CPUs (CPU cores) on the machine. Usually a good choice for the number of processes
    
    for i in range(num_processes):
        process = Process(target=square_numbers)
        processes.append(process)
    
    for process in processes:
        process.start()
    
    # wait for all processes to finish
    # block the main programm untill these processes are finished
    for process in processes:
        process.join()
