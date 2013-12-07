from timeit import timeit
from time import sleep
import sys

def benchmark():
    for k in range(3,5):
        for n in range(k,k+4g):
            p = "test_all_problems_G("+str(k)+","+str(n)+")"
            t = timeit(p,number=1,setup="from go import test_all_problems_G")
            print(k,n,t)

    for i in range(1,10):
        sys.stdout.write('\a')
        sys.stdout.flush()
        sleep(0.5)
