from timeit import timeit
from time import sleep
import sys

def benchmark():
    for k in range(2,5):
        for n in range(k,k+5):
            p = "test_all_problems_G("+str(k)+","+str(n)+")"
            print(k,n)
            t = timeit(p,number=1,setup="from go import test_all_problems_G")
            print(t)

if __name__ == "__main__":
    try:
        benchmark()
    except KeyboardInterrupt:
        import os
        os._exit()
