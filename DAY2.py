
'''
#input::bcdmnwc
#       9
#output:student
s=input()
n=int(input())
s1=""
k=n%26
for i in s:
    if((ord(i)-k)>=97):
        s1+=chr(ord(i)-k)
    else:
        s1+=chr(ord(i)-k+26)
print(s1)
'''
'''
#input:xyzabcdefklmnopqefgh
#output:7(longest substring in sequence)
s=input()
l=[]
c=1
m=0
for i in range(len(s)-1):
    if (ord(s[i])==ord(s[i+1])-1):
        c+=1
    else:
        if(c>m):
            m=c
        c=1
if c>m:
    m=c
print(m)
'''
'''
#input: 3
#       xyz
#       pqr
#      abc
#      yraxpazr
#output:yes
n=int(input())
m=[]
c=1
for i in range(n):
    m.append(input())
print(m)
s=input()
flag=0
for i in range(len(s)):
    if s[i] not in m[i%n]:
        print("NO")
        break
else:
    print("YES")
'''
'''
n=int(input())
m=[]
c=1
for i in range(n):
    m.append(list(map(str,input().split())))
print(m)
s=input()
flag=0
for i in range(len(s)):
    if s[i] not in m[i%n]:
        print("NO")
        flag=1
        break
    else:
        m[i].remove(s[i])
if flag==0:
     print("YES")

'''
'''
#reverse of number using recursion
def reverse(n,rev):
    if n==0:
        return rev
    rev=rev*10+(n%10)
    return reverse(n//10,rev)
    
n=int(input())
res=reverse(n,0)
if res==n:
    print("Palindrome")
else:
    print("Not Palindrome")
'''
'''

#Happy Number
#input: 15 3 2 7 8 4 (buy and sell the product to get the max profit)
#output:6
l=list(map(int,input().split()))
profit=0
k=l[0]
for i in l:
    if i<k:
        k=i
    elif (i-k)>profit:
        profit=i-k
print(profit)   #-----O(n)
#OR

l=list(map(int,input().split()))
profit=0
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if (l[i]<l[j] and l[j]-l[i]>profit):
            profit=l[j]-l[i]
print(profit)    #------O(n*n)
'''
'''
#input:5
#output: * * * * *
#        * 1 2 3 *
#        * 4 5 6 *
#        * 7 8 9 *
#        * * * * *
n=int(input())
c=1
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('*',end=" ")
        else:
            print(c,end=" ")
            c+=1
    print()
'''
#input:4
#output:
#    _ _ _ _ a_ _ _ _
#    _ _ _a  b  a _ _ _
#    _ _a  b c b  a_ _
#    _a  b  c  d  c  b  a _
n=int(input())
j=1
for i in range(n,0,-1):
    print('_'*i,end=" ")
    a=97
    for k in range(j):
        print(chr(a),end=" ")
        a+=1
    a=97
    for k1 in range(j-1):
        print(chr(a),end=" ")
        a+=1
    print('_'*i,end=" ")
    j=j+1
    print()
    
    
            
    
        
#input:5
#1 1 1 1 1 1 1
#1 2 2 2 2 2 1
#1 2 3 3 3 2 1
#1 2 3 4 3 2 1
#1 2 3 3 3 2 1
#1 2 2 2 2 2 1
#1 1 1 1 1 1 1
        