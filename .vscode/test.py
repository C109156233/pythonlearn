
'''
for i in range(1,10):
    for j in range(1,10):
        ans=i*j
        print("%d*%d=%-2d"%(i,j,ans),end=" ")
    print()#換行

for i in range(1,6):
    for j in range(1,i+1):
        print("#",end='')#end不能忘記
    print()

f=int(input("大樓層數:"))
for i in range(1,f+1):
    if(i==4):
        continue
    print(i,end='')

'''
'''
total=n=0
while(n<10):
    n+=1
    total+=n
print(total)
'''
'''
for i in range(6):
    for j in range(0,5-i):#做空格
        print(" ",end="")
    for j in range(i):#作米字
        print("*",end="")
    print("")
'''
'''
for i in range(6): #i是行數,j是補*
    for j in range(0,5-i): #做空格
        print(" ",end="")
    for j in range(0,i):
        print("*",end="")
    for j in range(i-1): #從第二行開始做
        print("*",end="")
    print("")
'''
'''
for i in range(7):
    for j in range(0,7-i): #做空格
        print(" ",end="")
    for j in range(0,i-1):
        print("*",end=" ")
    print()
'''
for i in range(7):
    for j in range(0,7-i):
        print(" ",end="")
    for j in range(0,i-1):
        print("*",end=" ")

    print(" ")

