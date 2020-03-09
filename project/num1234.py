# aList=[1,2,3,4,5,6,3,8,9]
# sign=False              #初始值为没找到
# x=int(input("请输入要查找的整数："))
# for i in range(len(aList)):
#    if aList[i]==x:
#       print("整数%d在列表中，在第%d个数"%(x,i+1))
#       sign=True
# if sign==False:
#    print("整数%d不在列表中"%x)
#
#
#
#
# def binary_chop2(alist, data):
#     """
#     递归解决二分查找
#     """
#     n = len(alist)
#     if n < 1:
#         return False
#     mid = n // 2
#     if alist[mid] > data:  #0(n)
#         return binary_chop2(alist[0:mid], data) #O(K)
#     elif alist[mid] < data:
#         return binary_chop2(alist[mid+1:], data)
#     else:
#         return True


#HasH查找

class HashTable:
    def __init__(self):
        self.size = 10
        self.slots = [None]*self.size #key
        self.data = [None]*self.size  #value
    def hash(selfself,key,size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def put(self,key,data):
        hash_value = self.hash(key,len(self.slots))
        print(hash_value)
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data   #$存储完成A:不存在
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data     #$存储完成B： 无key值
            else:
                next_slot = self.rehash(hash_value,len(self.slots))     #$存储完成C：此key已存在值 位置+1
                while self.slots[next_slot] is not None and self.slots[next_slot]!=key: #   u  确定为新的标注点key已存在value不同
                    next_slot = self.rehash(next_slot,len(self.slots)) #继续找新位置
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data #此key无value
    def get(self,key):
        start_slot = self.hash(key,len(self.slots))

        data = None
        stop = False
        found = False
        pos = start_slot

        while self.slots[pos] is not None and not found and not stop: #查出的值不为空
            if self.slots[pos] == key: #是否存在值
                found = True
                data = self.data[pos]
            else:
                pos = self.rehash(pos,len(self.slots))
                if pos == start_slot:
                    stop = True
        return data

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.put(key, value)


h = HashTable()
h[54] = 'cat'
h[26] = 'dog'
h[93] = 'lion'
# h[17] = 'tiger'
# h[77] = 'bird'
# h[85] = 'bee'
# h[34] = 'fish'

print(h.slots)
print(h.data)
print(h.get(54))













