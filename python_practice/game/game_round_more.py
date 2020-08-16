def game() :
    my_hp = 1000
    my_power = 200
    your_hp = 1000
    your_power = 199

    while True :
        my_hp = my_hp - your_power
        your_hp = your_hp - my_power
        print(my_hp)
        if my_hp<=0:
            print("我赢了！！！")
            break
        elif your_hp<=0:
            print("你赢了！！！")
            break

game()