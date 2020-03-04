from pythonds.basic.stack import Stack
def parChecker(symbolString):
    s = Stack()
    flag = True
    index = 0
    while index < len(symbolString) and flag:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                flag = False

            else:
                top = s.pop()
                start = '([{'
                end = ')]}'
                if not start.index(top) == end.index(symbol):
                    flag =  False
        index = index+1
    if flag and s.isEmpty():
        return True
    else:
        return  False

print(parChecker('({{[]}})'))


# 十进制转二进制

def tentoTwo(num):
    s = Stack()
    flag = True
    index = 0
    while num > 0:

        two_num = num % 2
        s.push(two_num)
        num = num // 2

    binString = ""
    while not s.isEmpty():
        binString = binString + str(s.pop())
    return binString

print(tentoTwo(233))


#十进制转十六进制 八进制 二进制
def eighttoSixteen(num,base):
    digits = "0123456789ABCDEF"
    s = Stack()

    while num >0:
        rem = num %base
        s.push(rem)
        num = num //base
    binString = ""
    while not s.isEmpty():
        binString = binString + digits[s.pop()]

    return binString

print(eighttoSixteen(233,2))

