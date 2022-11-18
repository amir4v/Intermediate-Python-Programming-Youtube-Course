# Multiprocessing: data between processes, lock, queue, process pool

from multiprocessing import Pool

def cube(number):
    return number*number*number

if __name__ == "__main__":
    
    numbers = range(1,10)
    
    pool = Pool()
    # important methods: map,apply,join,close
    
    result = pool.map(cube, numbers) # this will creates how many Process that your machine is capable and will do it (this specific function) in all of these Processes
    
    pool.close()
    pool.join()
    
    print(result) # [1, 8, 27, 64, 125, 216, 343, 512, 729]
