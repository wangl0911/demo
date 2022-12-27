a = [1, 4, 44, 5, 23, 55, 88, 44]

for i in range(len(a)-1):
    for u in range(len(a)-i-1):
        if a[u] < a[u+1]:
            a[u],a[u+1] = a[u+1], a[u]

print(a)

# try:
#     num = int(input("请输入："))
# except:
#     print("您输入的是非数字")
#
# if 999 > num > 100:
#     fri = num // 100
#     sec =(num // 10 ) % 10
#     fin = num % 10
#     if fri**3 + sec**3 +fin**3 == num:
#         print(f'{num}是水仙花数')
#
#     else:
#         print(f'{num}不是水仙花数')
# else:
#     print("该数不在范围内")

for i in range(0,10):
    for j in range(1,i+1):
        print(j, 'X', i, '=', i*j)


