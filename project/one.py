#求前N个整数的和
import time,timeit
def one(a):
    start_time = time.time()
    if a //2 == 0:
        num = 0
        i = 0
        for e in range(1,a+1):
            num = a-i+e
            i+=1
        end_time = time.time()
        return num,end_time-start_time
    elif a // 2 != 0:
        num = 0
        i = 1
        for e in range(1,a+1):
            num = a-i+e
            i+=1
        end_time = time.time()
        return num,end_time-start_time


print(one(5))

print('Running time: %d Seconds'%(one(500)[1]))