"""
module_name, package_name, ClassName, method_name, ExceptionName,
function_name, GLOBAL_VAR_NAME, instance_var_name, function_parameter_name, local_var_name.
"""
class HouseClass:
    # 静态属性-->变量,类变量:类之中，方法之外
    door = "red"
    floor = "white"
    # 构造方法：
    def __init__(self,door,floor):
        # 类之中且方法之中，并且不是以self.开头的变量
        self.door = door
        self.floor =floor
        #
        self.yangtai ="big"
    # def __init__(self):
    #     print(self.door)
    #     print(self.floor)
    # 动态属性-->方法   def 定义在class外面的就是函数，定义在class里的就是方法
    def sleep_method(self):
        # 普通变量：类之中且方法之中，并且不是以self. 开头的变量

        print("sleeping_method....")
    def cook_method(self):
        print("cooking_method.....")
# chinese_house=HouseClass()
# print(chinese_house.door)
# HouseClass.door="black"
# print(chinese_house  .door)
HouseClass()

