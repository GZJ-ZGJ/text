#coding:utf-8
"""
综合项目:世行历史数据基本分类及其可视化
作者：郭振疆
日期：2020/12/31
pyecharts
"""

import csv
import math
import pygal
import pygal_maps_world  #导入需要使用的库


def read_csv_as_nested_dict(filename, keyfield, separator, quote): #读取原始csv文件的数据，格式为嵌套字典
    result={}
    with open(filename,newline="")as csvfile:
        csvreader=csv.DictReader(csvfile,delimiter=separator,quotechar=quote)
        for row in csvreader:
            rowid=row[keyfield]
            result[rowid]=row
    return result
a=read_csv_as_nested_dict('isp_gdp.csv','Country Name',",",'"')
# print(a)

# print(a)
# print(a["Country1"]['2000'])




"""
    输入参数:
      filename:csv文件名
      keyfield:键名
      separator:分隔符
      quote:引用符

    输出:
      读取csv文件数据，返回嵌套字典格式，其中外层字典的键对应参数keyfiled，内层字典对应每行在各列所对应的具体值
"""
    # result={}
    # with open(filename,newline="")as csvfile:
    #     csvreader=csv.DictReader(csvfile,delimiter=separator,quotechar=quote)
    #     for row in csvreader:
    #         rowid=row[keyfield]
    #         result[rowid]=row
    #
    # return result

# li1=[]
# with open("isp_gdp.csv","rt",newline="")as csvfile1:
#     csvreader = csv.DictReader(csvfile1,skipinitialspace=True)
#
#     for i in csvfile1:
#
#         i=i.rstrip()
#         a=i.split(',')
#         li1.append(a)
# print(li1)
# # , gdp_countries
pygal_countries = pygal.maps.world.COUNTRIES #读取pygal.maps.world中国家代码信息（为字典格式），其中键为pygal中各国代码，值为对应的具体国名(建议将其显示在屏幕上了解具体格式和数据内容）
# # print(pygal_countries)
li_pygal_countries=list(pygal_countries)#将代码变成列表形式
# print(li_pygal_countries)
# # a="pygal_countries"
# # if a in pygal_countries:
# #     print(a)
# # a=read_csv_as_nested_dict("isp_gdp.csv","Country Code",",",':')
# # b=read_csv_as_nested_dict("isp_gdp.csv",)
# def reconcile_countries_by_name(plot_countries):#返回在世行有GDP数据的绘图库国家代码字典，以及没有世行GDP数据的国家代码集合
#     c=set()
#     h={}
#     for u in li1:
#         for y in u[4:57]:
#             if y !='':
#                 for k in li_pygal_countries:
#                     if plot_countries[k]==u[0]:
#                         h[k]=u[0]
#                 break
#             else :
#                 for k in li_pygal_countries:
#                     if plot_countries[k]==u[0]:
#                         c.add(k)
#                 break
#     return c,h
# print(reconcile_countries_by_name(pygal_countries))

   # """
   #
   #  输入参数:
   #  plot_countries: 绘图库国家代码数据，字典格式，其中键为绘图库国家代码，值为对应的具体国名
   #  gdp_countries:世行各国数据，嵌套字典格式，其中外部字典的键为世行国家代码，值为该国在世行文件中的行数据（字典格式)
   #
   #  输出：
   #  返回元组格式，包括一个字典和一个集合。其中字典内容为在世行有GDP数据的绘图库国家信息（键为绘图库各国家代码，值为对应的具体国名),
   #  集合内容为在世行无GDP数据的绘图库国家代码
   #  """
   #  # pass # 编码，结束后将pass删除
   #  # # 不要忘记返回结果
# for m in pygal_countries:
#     print(pygal_countries[m])

def build_map_dict_by_name(gdpinfo, plot_countries, year):
    z={}
    x=set()
    x1=set()
    for l in plot_countries:
        for t in gdpinfo:
            if plot_countries[l] ==t:
                a1=gdpinfo[t][year]
                a2=list(gdpinfo[t])
                a3=0
                if a1!='':
                    z[l] = math.log10(float(a1))
                else:
                    for i1 in a2[4:]:
                        if gdpinfo[t][i1] == '':

                            a3=a3+1
                    if a3==56:
                        x1.add(l)
                    elif a1 == '':
                       x.add(l)

    return z,x,x1
# print(build_map_dict_by_name(a,pygal_countries,'1966'))









def render_world_map(gdpinfo, plot_countries, year, map_file): #将具体某年世界各国的GDP数据(包括缺少GDP数据以及只是在该年缺少GDP数据的国家)以地图形式可视化
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'Some countries'
    worldmap_chart.add(year,build_map_dict_by_name(gdpinfo,plot_countries,year)[0])
    worldmap_chart.add('该年没有数据',build_map_dict_by_name(gdpinfo,plot_countries,year)[1])
    worldmap_chart.add('一直没有数据',build_map_dict_by_name(gdpinfo,plot_countries,year)[2])
    worldmap_chart.render()
    worldmap_chart.render_to_file(map_file)















#程序测试和运行
print("欢迎使用世行GDP数据可视化查询")
print("----------------------")
year=input("请输入需查询的具体年份:")
print(render_world_map(a,pygal_countries,year,'isp_gdp_world_name_1980.svg'))
