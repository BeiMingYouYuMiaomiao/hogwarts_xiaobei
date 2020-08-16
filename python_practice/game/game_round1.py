def game() :
    my_hp = 1000
    my_power = 200
    your_hp = 1000
    your_power = 199
    my_final_hp = my_hp - your_power
    ememy_final_hp = your_hp - my_power

    # if my_final_hp > ememy_final_hp:
    #     print("我赢了！！！")
    # else:
    #     print("你赢了！！！")
    # 三目运算等同于上面的if-else 语法更简洁
    print("我赢了！！！") if my_final_hp > ememy_final_hp else  print("你赢了！！！")

game()