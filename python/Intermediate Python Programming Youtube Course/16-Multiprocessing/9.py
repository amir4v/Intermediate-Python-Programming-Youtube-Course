# Multiprocessing: data between processes, lock, queue, process pool

from multiprocessing import Pool

def cube(number):
    return number*number*number

if __name__ == "__main__":
    
    numbers = range(1,10)
    
    pool = Pool()
    # important methods: map,apply,join,close
    
    # result = pool.map(cube, numbers) # this will creates how many Process that your machine is capable and will do it (this specific function) in all of these Processes
    
    result = pool.apply(cube, (numbers[5],) ) # like map BUT does apply the function (cube) to a single value
    # result = pool.apply(cube, numbers) # in jori ham mishe vali injori hameye element haye numbers ro (ya iterable ro) yekja mide be cube (function), mesle inke yedafe 10 ta argument ro pass mide be cube function
    
    # AND _async functions of Pool class #
    
    pool.close()
    pool.join()
    
    print(result) # 216
