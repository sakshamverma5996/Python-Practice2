# # problem 1 
i=1
while i<100:
    print(i)
    i+=1
# # problem 2 
m=100 
while m>0:
    print(m)
    m-=1
# # problem 3
n=int(input("enter the number"))
k=1
while k<11:
    print(n*k)
    k+=1
# # problem 4
num =[1,4,9,16,25,36,49,64,81,100]
u=0
while u<9:
    print(num[u])
    u+=1


# problem 6
# for i in num:
    print(i)

#  problem 7
x=input("enter the number")
idx=0
for i in num:
    if (i==x):
        print("the number is present",idx)
        idx+=1
# problem 8
num= int(input("enter the number"))
sum=0
while num>0:
    sum= sum+num
    num-=1
print("total sum is ", sum)

# problem 9
n= int(input("enter the number"))
mul=1
for i in range(1,n+1,1):
    mul=mul*i
print("the multiplication is ", mul)