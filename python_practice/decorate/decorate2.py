#装饰器 可以后续在进一步了解


def func1(func):
    # func() 放在这也可以用，但是吧，不符合规范 当使用复杂后，就无用了
    # 在函数func1内部定义一个函数
    def func2():
        func()
        print("我是func2")
        # return func()
        return func
    print("我是func1的内容")

    #返回"肚子"里面的函数对象
    return func2
@func1
def be_decorate():
    print("我是一个被装饰器修饰的函数")
be_decorate()