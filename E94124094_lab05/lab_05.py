dic1={"index":["國文","英文","數學","自然","社會"],"stuA":[50,60,70,80,90],"stuB":[57, 86, 73, 82, 43] , "stuC":[97, 96, 86, 97, 83]}#建立字典

print(dic1)
print("A學生平均成績 :",(dic1["stuA"][0]+dic1["stuA"][1]+dic1["stuA"][2]+dic1["stuA"][3]+dic1["stuA"][4])/5)#a平均成績
print("B學生平均成績 :",(dic1["stuB"][0]+dic1["stuB"][1]+dic1["stuB"][2]+dic1["stuB"][3]+dic1["stuB"][4])/5)#b平均成績
print("C學生平均成績 :",(dic1["stuC"][0]+dic1["stuC"][1]+dic1["stuC"][2]+dic1["stuC"][3]+dic1["stuC"][4])/5)#c平均成績
print('\n')#換行

for i in range(5):
    print(dic1['index'][i],"平均成績為 : ",(dic1["stuA"][i]+dic1["stuB"][i]+dic1["stuC"][i])/3,sep='')
    i +=1