#装饰器 可以后续在进一步了解

#闭包函数
name="BigFish"
def func1():
    # 在函数func1内部定义一个函数
    def func2():
        print("我是func2")
        print(name)
    print("我是func1的内容")
    print(name)
    #返回"肚子"里面的函数对象
    # return func2()
    return func2

# print(func1())
# 有()  函数的调用
func1()
# 无()  函数对象
func22=func1
print("----------------")
print(func22())