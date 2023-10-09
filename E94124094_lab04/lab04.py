list1=['A']
list2=['B']
list3=["C"]
list_t =[list1,list2,list3]
listC=('A','B','C')
for i in range(0,3):
    print("請輸入"+listC[i]+"的學生成績",sep='')
    list_t[i].append(int(input("國文：")))
    list_t[i].append(int(input("數學：")))   
    list_t[i].append(int(input("英文：")))
    list_t[i].append((list_t[i][1]+list_t[i][2]+list_t[i][3])/3)


    
print(list1)
print(list2)
print(list3)