# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 18:05:10 2022

@author: pavmb
"""
from multiprocessing import Lock
from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Value, Array
N = 8
def task(common, tid, lock):
 a = 0
 for i in range(100):
     print(f'{tid}−{i}: Non−critical Section')
     a += 1
     print(f'{tid}−{i}: End of non−critical Section')
     try:
         lock.acquire()
         print(f'{tid}−{i}: Critical section')
         v = common.value + 1
         print(f'{tid}−{i}: Inside critical section')
         common.value = v
         print(f'{tid}−{i}: End of critical section')
     finally:
         lock.release()

def main():
 lock=Lock()
 lp = []
 common = Value('i', 0)
 for tid in range(N):
     lp.append(Process(target=task, args=(common, tid, lock)))
 print (f"Valor inicial del contador {common.value}")
 for p in lp:
     p.start()
 for p in lp:
     p.join()
     
 print (f"Valor final del contador {common.value}")
 print ("fin")
if __name__ == "__main__":
 
 main()