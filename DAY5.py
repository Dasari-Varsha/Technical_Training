'''
input:l=[4,8,4,4,4,6,6,6,6,6] #---------------O(N*N)
output: 6
l=[4,8,4,4,4,6,6,6,6,6]
max1=0
for i in l:
    if l.count(i)>max1:
        max1=l.count(i)
        p=i
print(p)



l=[1,1,2,2,3,1] #----------------------O(N)
c=0
win=l[0]
for i in l:
    if i==win:
        c+=1
    else:
        if c==0:
            c=1
            win=i
        c-=1
print(win)
'''
'''
#input:n=7
#      l=[0,5,3,6,7,2,1]
#output:4
n=7         #--------------O(N*N)
l=[0,5,3,6,7,2,1]
for i in range(n+1):
    if i in l:
        continue
    else:
        k=i
print(k)
 
n=7
l=[0,5,3,6,7,2,1]
a=sum(l)
n=(n*(n+1))//2
print(n-a)
'''
'''
#printing k th largest factor of the given number
n=12
k=3
c=0
for i in range(1,n):
    if n%i==0:
        max1=(n//i)
        c+=1
    if c==k:
        print(max1)
        break
'''
'''
#checking co-primes or not(only 1 as the common factor )
n1=12
n2=13
l1=[]
l2=[]
c=0
for i in range(1,n1+1):
    if n1%i==0:
        l1.append(i)
for i in range(1,n2+1):
    if n2%i==0:
        l2.append(i)
for i in l1:
    for j in l2:
        if i==j:
            c+=1
print(l1)
print(l2)
if c==1:
    print("Co-Primes")
else:
    print("Not Co-Primes")


import math
a=12
b=10
if math.gcd(a,b)==1:
    print("Co-primes")
else:
    print("Not co-primes")
'''
l="{{()}"
stack=[]
c=0
flag=0
for i in range(len(l)):
    if l[i]=='(' or l[i]== '{' or l[i]=='[':
        stack.append(i)
    elif(not stack):
        if (l[i]=='}' and stack[-1]=='{') or  (l[i]==']' and stack[-1]=='[') or (l[i]==')' and stack[-1]=='('):
            stack.pop()
        else:
            print(i)
            flag=1
            break
    else:
        print(i)
        flag=1
        break
    c+=1
if flag==0:
    print("-1")




            
            
    
    
        


        