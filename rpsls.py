#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�����
���ڣ�2020/11/21
"""

import random
answer=random.randint(0,4)#����python�Դ���ģ���������һ��0-4֮�������



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(answer):#���庯������0-4�ֱ��Ӧ����
    if answer==0:
        name="ʯͷ"
    elif answer==1:
        name="ʷ����"
    elif answer==2:
        name="ֽ"
    elif answer==3:
        name="����"
    elif answer==4:
        name="����"
    else :
        print("����")
    return name








     #��дִ�д���,������ɺ�passɾ��


def number_to_name(name):#���庯����ʹ���ֱַ��Ӧ0-4֮�������
    if name=="ʯͷ":
        number=0
    elif name=="ʷ����":
        number=1
    elif name =="ֽ":
        number=2
    elif name=="����":
        number=3
    elif name=="����":
        number=4
    else:
        print("��Error: No Correct Name����")
    return number
    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��
   #��дִ�д���,������ɺ�passɾ��
def rpsls(player_choice):#���庯�����ж��˻��߻�����ʤ
    a=number_to_name(choice_name)
    b=name_to_number(answer)
    print("���ѡ��Ϊ��",choice_name)
    print("������ѡ��Ϊ��", b)
    c=a-answer#����һ���㷨�������ж�
    if -4<=c<=-3 or 1<=c<=2:#�ж���Ӯ
        print("��Ӯ��!")
    elif c==0:
        print("ƽ��")

    else:
        print("����Ӯ��!")#�жϻ���Ӯ
    # """
    # �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    #
    # """


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    #����������ʾ��дִ�д��룬������ɺ�ɾ����pas
# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


