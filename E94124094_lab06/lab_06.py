list_rem = list()#建立字典
def gcd(a,b):#定義數值a與b的最大公因數
    if a == 0 or b == 0:
        return 'error'
    list1 = sorted([a,b])
    list_rem.append(list1[0])
    rem = list1[1]%list1[0]
    list_rem.append(rem)
    if rem != 0:
        return gcd(list1[0],rem)
    else:
        return list_rem[-2]


for i in range(3):
    a = int(input('輸入兩個整數求最大公因數'))
    b = int(input('輸入兩個整數求最大公因數'))
    if gcd(a,b) == 'error':
        print('0 沒有gcd')
    elif gcd(a,b) == 1:
        print(a,'和',b,'互質')
    else:
        print(a,'和',b,'的gcd =',gcd(a,b))