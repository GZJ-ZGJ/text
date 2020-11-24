#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：郭振疆
日期：2020/11/21
"""

import random
answer=random.randint(0,4)#利用python自带的模块随机产生一个0-4之间的整数



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(answer):#定义函数，让0-4分别对应名字
    if answer==0:
        name="石头"
    elif answer==1:
        name="史波克"
    elif answer==2:
        name="纸"
    elif answer==3:
        name="蜥蜴"
    elif answer==4:
        name="剪刀"
    else :
        print("报错")
    return name








     #编写执行代码,代码完成后将pass删除


def number_to_name(name):#定义函数，使名字分别对应0-4之间的整数
    if name=="石头":
        number=0
    elif name=="史波克":
        number=1
    elif name =="纸":
        number=2
    elif name=="蜥蜴":
        number=3
    elif name=="剪刀":
        number=4
    else:
        print("“Error: No Correct Name”。")
    return number
    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
    # 不要忘记返回结果
   #编写执行代码,代码完成后将pass删除
def rpsls(player_choice):#定义函数，判断人或者机器获胜
    a=number_to_name(choice_name)
    b=name_to_number(answer)
    print("你的选择为：",choice_name)
    print("机器的选择为：", b)
    c=a-answer#定义一个算法有助于判断
    if -4<=c<=-3 or 1<=c<=2:#判断人赢
        print("你赢了!")
    elif c==0:
        print("平局")

    else:
        print("机器赢了!")#判断机器赢
    # """
    # 用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    #
    # """


    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”

    #根据以上提示编写执行代码，代码完成后删除掉pas
# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)


