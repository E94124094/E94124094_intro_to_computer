nums=[3, 2, 2, 3, 6, 5, 4, 3, 2, 1]

print("輸入的list為:",nums,end='')
val = int(input("要刪除的數字是"))
print(",要刪除的數字是",val)
print("刪除後!")
print("list變成: [",end='')
i = 0
while i < len(nums):
    if int(val) == nums[i]:
        pass
    else:
        print(nums[i],', ',sep='',end='')
    i += 1
print(']')