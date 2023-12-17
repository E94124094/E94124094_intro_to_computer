import os
import matplotlib.pyplot as plt
import numpy as np
path = "Temperature.txt"

#read file and data preprocess
f=open(path,'r')
temp = []  #二維
year = []
month = list(range(1,13))
for line in f.readlines(): 
    if (line == "Tainan:\n"):
        continue
    a = list(map(float,line.rstrip("\n").split(",")))
    temp.append(a[1:])
    year.append(int(a[0]))
# print(year, temp)
f.close

def pic1(): #畫出01.png
    for i in range(len(temp)):
        plt.plot(month, temp[i], label = year[i])  #plt.plot(x_pos, y_pos, label)

    plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
    plt.xlabel('Month')
    plt.ylabel('Temperature in Degree C')
    plt.xticks(month)
    plt.legend(loc = "lower center") 
    return
def pic2(): #畫出02.png
    #pic2
    #計算每月平均
    m_temp = []
    for i in range(len(month)):
        total = 0
        for j in temp:
            total += j[i]
        m_temp.append(round(total/9, 2))
    #畫出每月平均折線圖
    plt.scatter(month, m_temp, color = "red")
    plt.plot(month, m_temp)

    # print(m_temp)
    for a, b in zip(month, m_temp):
        plt.text(a, b, b, va = 'bottom', fontsize = 10) #標出value 

    #算出年平均
    ave = round(sum(m_temp) / 12, 2)
    plt.axhline(y = ave, xmin = 0, xmax = 13, color = 'red', linestyle = "--", label = "Mean of 9 years")
    plt.text(1, ave, ave, va = 'bottom', fontsize = 10) #標出value ex: plt.text(x_pos, y_pos, string)

    plt.title('Tainan Monthly Mean Temperature Of 2013 To 2021')
    plt.xlabel('Month')
    plt.ylabel('Temperature in Degree C')
    plt.xticks(month)
    plt.yticks(range(16, 34, 2))
    plt.legend() 
    return()

pic1()
plt.savefig("lab13_01.png")
plt.show()
pic2()
plt.savefig("lab13_02.png")
plt.show()

# 1 + 2 = 3 繪製子圖
fig = plt.figure(figsize=(15,6))
plt.subplot(1,2,1)
pic1()
plt.subplot(1,2,2)
pic2()
plt.savefig('lab13_03.png')
plt.show()