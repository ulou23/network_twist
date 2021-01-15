#synchro PROBLEM CPU BOUND

import time

import multiprocessing

def cpu_bound(nr):
    return sum(i*i for i in range(nr))

def res_sum(nrs):
    for nr in nrs:
        cpu_bound(nr)

def multipro_sum(nrs):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound,numbers)


if __name__=="__main__":                                 

    numbers=[500000+x for x in range(20)]

    start_t=time.time()
    res_sum(numbers)
    dura=time.time()-start_t
    print(f" synchro Duration {dura} sec ")

    start_t=time.time()
    multipro_sum(numbers)
    dura=time.time()-start_t
    print(f" Multiprocessing  Duration {dura} sec ")