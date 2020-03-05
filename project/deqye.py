# 双端队列:是一种具有队列和栈的性质的数据结构。
#
# 双端队列中的元素可以从两端弹出，其限定插入和删除操作在表的两端进行。双端队列可以在队列任意一端入队和出队。

class Deque(object):
    """双端队列"""

    def __init__(self):
        self.items = []

    def is_empty(self):
        """判断队列是否为空"""
        return self.items == []

    def add_front(self, item):
        """在队头添加元素"""
        self.items.insert(0, item)

    def add_rear(self, item):
        """在队尾添加元素"""
        self.items.append(item)

    def remove_front(self):
        """从队头删除元素"""
        return self.items.pop(0)

    def remove_rear(self):
        """从队尾删除元素"""
        return self.items.pop()

    def size(self):
        """返回队列大小"""
        return len(self.items)

    def info(self):
        """返回队列所有元素"""
        return self.items


def palChecker(aString):
    chardeque = Deque()
    for ch in aString:
        chardeque.add_rear(ch)
    flag = True

    while chardeque.size() > 1 and flag:
        first = chardeque.remove_front()
        last = chardeque.remove_rear()

        if first != last:
            flag = False
    return flag

if __name__ == "__main__":
    # deque = Deque()
    # deque.add_front(1)
    # deque.add_front(2)
    # deque.add_rear(2)
    # deque.add_rear(1)
    # print( deque.size())
    #
    # print(deque.info())
    #
    # print(deque.remove_front())
    #
    # print(deque.remove_front())
    #
    # print(deque.remove_rear())
    #
    # print(deque.remove_rear())
    print(palChecker('1221'))
