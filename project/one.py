# 算法：
#     递推法 ：其思想是把一个复杂的庞大的计算过程转化为简单过程的多次重复；
#     递归法 ：多次重复计算，大大地减少了程序的代码量；
#     穷举法 ：列举出它的所有可能的情况；
#     贪心算法 ：一步步执行规定的最优方法；
#     分治法 ：把一个复杂的问题分成两个或更多的相同或相似的子问题 逐个击破；
#     回溯法 ：走不通回撤，找方法；
#     分支界限法：对约束条件的 最优化问题的所有可行解进行搜索；

# 递归法 上台阶，一步最多走三
def one(n):   #n太
    d = {1:1,2:2,3:3}
    if n in d.keys():
        return  d[n]
    else:
        return one(n-1)+one(n-2)+one(n-3)
#递推法
def demo(n):  # n最少为3，否则输出4错误
    a=1
    b=2
    c=4
    for i in range(n-3):
        c,b,a=a+b+c,c,b
    return c
print(demo(4))

#分治法  实现列表的快速排序

# 分区
def partition(nums = list):
    this_one = nums[0]
    lo = [x for x in nums[1:] if x < this_one]
    hi = [x for x in nums[1:] if x >=this_one ]
    return lo,this_one,hi
#快速排序
def sort_tick(nums = list):
    if len(nums) <= 1:
        return nums
    lo,this_one,hi = partition(nums)
    return sort_tick(lo) + [this_one] + sort_tick(hi)


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

#乱序字符串：第一个字符串是否是第二个字符串的乱序
def solutions1(str1,str2):
    lists1 = list(str1)
    lists2 = list(str2)
    if len(lists1) != len(lists2):
        return False
    one = dict(zip(lists1))
    two = dict(zip(lists2))
    if one == two:
        return True
    else:
        return False


# 排序比较
def two(str1,str2):

    pass