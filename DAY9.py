'''
#Input:[4,8,14,22,36,68]
#output:[7,13,19,31,67]---sum of 7+13+19+31+67
def isprime(i,j):
    flag=0
    l1=[]
    l2=[]
    #print(i,j)
    for k in range(i+1,j):
        l1.append(k)
    #print(l1)
    for i in l1:
        for j in range(2,(i+1)//2):
            if(i+1)%j==0:
                l2.append(i)
                flag=1
                break
    return max(l2)
    
l=[4,8,14,22,36,68]
l1=[]
sum1=0
for i in range(len(l)-1):
    t=isprime(l[i],l[i+1])
    sum1=sum1+t
print(sum1)
'''
'''
#input:[4,9,8,2,14,3,5,6]
#       4 8 9 2 14 3 5 6
#         2 8 9 14 3 5 6
#           8 9 14 3 5 6
#             3 9 14 5 6
#               5 9 14 6
#                 6 9 14
#output:4 2 8 3 5 6 9 14
l=[4,9,8,2,14,3,5,6]
l1=[]
i=0
j=1
k=2
while k<len(l)-2:
    # print(l)
    a=l[i]
    b=l[j]
    c=l[k]
    #print(a,b,c)
    if a>b:
        l[i],l[j]=l[j],l[i]
        a,b=b,a
    if a>c:
        l[i],l[k]=l[k],l[i]
        a,c=c,a
    if b>c:
        l[j],l[k]=l[k],l[j]
        b,c=c,b
         
    i=i+1
    j=i+1
    k=j+1
print(l)
'''
#input:"hello:5438,car:214,book:8799,apple:2187"
# if lenth of key is in value print the keyth value
#if not print the length-1 th value
#else print x
#output:oaxp

'''
d={"hello":5438,"car":214,"book":8799,"apple":2187}
for i in d:
    print(i,str(d[i]),end=" ")
    print()
res=""
flag=1
for i in d:
    c=len(i)
    while flag:
        if str(c) in str(d[i]):
            c=int(c)
            res+=i[c-1]
            print(res)
            flag=0
        elif c<0 :
            res+='x'
            flag=0
        elif str(c) not in str(d[i]) :
            c=int(c)
            c=c-1
    flag=1
print(res)
'''
'''
d={}
s=input().split(',')
for i in range(len(s)):
    s1=s[i].split(":")
    d[s1[0]]=s1[1]
print(d)
res=""
flag=1
for i in d:
    c=len(i)
    while flag:
        if str(c) in str(d[i]):
            c=int(c)
            res+=i[c-1]
            print(res)
            flag=0
        elif c<0 :
            res+='x'
            flag=0
        elif str(c) not in str(d[i]):
            c=int(c)
            c=c-1
    flag=1
print(res)
'''
def isprime(x):
    for i in range(2,(x//2)+1):
        if x%i==0:
            return 0
    return 1
        
        
def lprime(n,m):
    for i in range(m-1,n,-1):
        if(isprime(i)):
            return i
    return 0
        
    
a=[4,8,14,22,37,68]
s=0
for i in range(len(a)-1):
    s=s+lprime(a[i],a[i+1])

print(s)

