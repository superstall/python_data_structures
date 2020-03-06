def fun(number,x,y,z):
    if number==1:
        print(x,'-->',z)
    else:
        fun(number-1,x,z,y)  # 前n-1个盘子借助z由x移动到y
        print(x,'-->',z)     # 打印出第n个盘由x移向z
        fun(number-1,y,x,z)  # 前n-1个盘子借助x由移到z上
number = int(input("请输入汉诺塔的层数:"))
fun(number,"X","Y","Z")






























