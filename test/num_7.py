# 7、输入一个三位整数，将该数的各位左右反转输出，即输入123，输出321。
'''
解题思路
判断数字是否为三位数
	是:数字转化为字符
	   枚举字符
	   反向添加（append）
	否：输出 你的输入有误
'''
'''
str = input("请输入一个三位数")
print("反转输出:"，end="")
a = int(str)
if a>=100 and a<=999:   
    for i in str:
        print(i,end="")
print()


for i in range(start,end,step):
# 额这个好像用不了
'''
str1 = int(input("请输入一个三位数："))
if str1<=999 and str1>=100:
    n1 = str1 // 100          #百位 除100 取整
    n2 = (str1 // 10) % 10    #十位 先除10 取整 在除10 取余
    n3 = str1 % 10            #百位 除10 取余
    print("%d%d%d" % (n3,n2,n1))  #反向格式化输出
