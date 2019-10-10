'''
6、编写一个程序，运行程序后，分别输入姓名、性别、年龄、单位、联系方式等数据，并用变量分别接收
输入完成后，最后打印出姓名、性别、年龄、单位、联系方式等信息，输出的格式自行设定，尽量美观
输出需使用上格式化输出。
'''

name = input("请您输入姓名：")
sex = input("请您输入性别：")
age = int(input("请您输入年龄："))
company = input("请您输入单位：")
tel = int(input("请您输入电话："))

'''
print("#"*15,end="")
print("您的基本信息",end="")
print("#"*15)
print(" "*10,end="")
print(name)

print(" "*10,end="")
print("性别："+sex)

print(" "*10,end="")
print("年龄："+str(age))    #强制类型转换
print(" "*10,end="")
print("单位："+company)
print(" "*10,end="")
print("电话："+str(tel))
print("#"*15,end="")
print("××××××",end="")
print("#"*15)

'''
print("#"*15,end="")
print("您的基本信息",end="")
print("#"*15)
print(" "*10,end="")
print(name)
print()
print(" "*10,end="")
print("性别："+sex)
print(" "*10,end="")
print("年龄:%d" % age) # 格式化输出
print(" "*10,end="")
print("单位："+company)
print(" "*10,end="")
print("电话：%d" % tel) # 格式化输出
print("#"*15,end="")
print("您的基本信息",end="")
print("#"*15)
