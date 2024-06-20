'''
def queen(r):
    if r==n:#row==n matrix j--row and i--col here
        return
    if r!=u:#when in row rook is not there
        for c in range(n):
            if(check(r,c)):#checking to place queen or not
                m[r][c]=1#palcing quuen at particular row or col
                break
            m[r][c]=0
        return queen(r+1)#checking next row
    else:
        queen(r+1)
       
def check(i,j):#passing row and col
    #if i==u:  #rook present in row or not
        #return 0
    if j==v:#rook present in col or not
        return
    r=i
    c=j
    for i in range(r+1):#row and col checking
        if m[i][j]==1:
            return 0
    i=r
    while(i>=0 and j>=0):#left diagional
        if m[i][j]==1:
            return 0
        i=i-1
        j=j-1
    while(r>=0 and c<n):#right diagonal
        if m[r][c]==1:
            return 0
        r=r-1
        c=c+1
    return 1     
n=5
u=1
v=3
m=[]
for i in range(n):
    m.append([0]*n)
m[0][0]=1
queen(0)
print(m)
c=0
for i in range(len(m)):
    for j in range(len(m)):
        if m[i][j]==1:
            c+=1
print("max possible queens can be placed are:",c)
'''
#------------------------------------------------------------------------------------
'''
l=[3,5,9,6,8,10]
max1=l[0]
max2=l[len(l)-1]
count=1
count1=1
for i in l:
    if i>max1:
        max1=i
        count+=1
print("sunrise",count)
for i in range(len(l)-1,-1,-1):
    if i>max2:
        max2=i
        count1+=1
print("sunset",count1)
'''
#-------------------------------------------------------------------------------------
'''
def fun(l,target,n):
    if target==0:
        return True
    if n==0:
        return False
    if l[n-1]>target:
        return fun(l,target,n-1)
    return fun(l,target,n-1) or fun(l,target-l[n-1],n-1)
        
l=[2,3,5,6]
target=11
print(fun(l,target,len(l)))
'''
#----------------------------------------------------------------------------------------
'''
#ip:[2,3,5,6]
#11
#op:yes
def fun(n):        
    l1=[0]*(n+1)
    i=l[0]
    l1[0]=1
    for j in range(1,n+1):
            if j==i:
                l1[j]=1
            else:
                l1[j]=0
    print(l1)
           
    
    for i in range(1,len(l)):
        l2=[0]*(n+1)
        print(l[i])
        l2[0]=1
        for j in range(1,n+1):
            if j<l[i]:
                l2[j]=l1[j]
            elif j==l[i]:
                l2[j]=1
            else:
                if l1[j]==1:
                    l2[j]=l1[j]
                else:
                    t=j-l[i]
                    te=l1[t]
                    l2[j]=te
        print(l2)
        l1=l2
    return l1[-1]

l=list(map(int,input().split()))
n=int(input())
t=fun(n)
if(t==1):
    print("yes")
else:
    print("no")
'''
#---------------------------------------------------------------------------------------------
'''
#input: tu5g2k1h8
#      g5g8gd6h3
#output:largest possible even number from the unique numbers aavailable from above strings
#       865312
s1="tu5g2k1h8"
s2="g5g8gd6h3"
s=set()
for i in s1:
    if i.isdigit():
        s.add(i)
for i in s2:
    if i.isdigit():
        s.add(i)
print(s)
res=""
for i in range(len(s)):
    k=max(s)
    res=res+k
    s.remove(k)
# print(res)
k1=res[::-1]
# print(k1)
for i in k1:
    if int(i)%2==0:
        j=i
        break
res+=j
res=list(res)
for i in range(len(res)):
    if res[i]==j:
        res.remove(j)
        break
f=""
for i in res:
    f=f+"".join(i)
print(f)
'''
'''
a=input()
b=input()
c=set()
for i in a:
    if (i.isdigit()):
        c.add(i)
for i in b:
    if (i.isdigit()):
        c.add(i)
d=list(sorted(c,reverse=True))
if (int(d[-1])%2==0):
    print(' '.join(d))
else:
    for i in range(len(d)-2,-1,-1):
        if(int(d[i])%2==0):
            d.append(d.pop(i))
            print(''.join(d))
            break
    else:
        print("-1")
'''
#input:121
#output: 121 print same number  if it is palindrome
#input:122
#output:131 print next nearest palindeome
#input:1234
#output:1331
#input:24
#output:33
#input:1112
#output:1221
#input:7654
#output:7667
#input:56472
#output:56565
'''
def fun(n): #-----------------Using Recursion
    t=n
    rev=0
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n//=10
    if t==rev:
        return t
    return fun(t+1)
n=int(input())
res=fun(n)
print(res)
#         OR

num=int(input())
t=num
s=str(num)
l=len(s)
rev=0
while(num>0):
    rev=rev*10+(num%10)
    num//=10
if t==rev:
    print(t)
else:
    if l%2==0: #length od string is even
        n=l//2
        left=s[:n]
        right=s[n:]
        k=left[::-1]
        if k>right:
            right=left[::-1]
            print(left+right)
        else:
            k=str(int(left)+1)
            print(k+k[::-1])
    else:
        n=l//2  #odd
        left=s[:n]
        right=s[n+1:]
        mid=s[n:n+1]
        k=left[::-1]
        if k<right:
            right=left[::-1]
            mid=str(int(mid)+1)
            print(left+mid+right)
'''
'''
#LONGEST PALINDROMIC SUBSEQUENCE --length and string
#input:abdbsdabca
#output:7,abdbdba
s1=input()
s2=s1[::-1]
m=[]
for i in range(len(s1)+1):
    l=[0]*(len(s2)+1)
    m.append(l)
#print(m)
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if(s1[i-1]==s2[j-1]):
            m[i][j]=m[i-1][j-1]+1
        else:
            m[i][j]=max(m[i][j-1],m[i-1][j])
print("Length of Longest Palindromic subsequence:",m[len(s1)][len(s2)])
u=len(s1)
v=len(s2)
s=" "
while(u>0 and v>0):
    if s1[u-1]==s2[v-1]:
        s=s+s1[u-1]
        #print(s)
        u=u-1
        v=v-1
    else:
        if m[u][v]==m[u-1][v]:
            u=u-1
        else:
            v=v-1
print("Longest Palindromic subsequence:",s[::-1])

'''


    

        
    
        
