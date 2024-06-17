'''
#job sequencing
#input:
#l1=[(1,3),(2,5),(4 ,6),(6,7),(5,8),(7,9)]
#a=[5,6,5,4,11,2]
#output:
#[5, 6, 10, 14, 17, 16]
#Max profit::17

l1=[(1,3),(2,5),(4 ,6),(6,7),(5,8),(7,9)]
a=[5,6,5,4,11,2]
b=a.copy()
i=1
while(i<len(l1)):
    j=0
    while(j<i):
        if l1[j][1]<=l1[i][0]:
            if b[j]+a[i]>b[i]:
                b[i]=b[j]+a[i]
        j+=1
    i+=1
print(b)
print(max(b))
'''
#-----------------------------------------------------------------------------------------------
'''
#Length of longest Common Subsequence
s1="abcd"
s2="axbdc"
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
print("Length of Longest Common subsequence:",m[len(s1)][len(s2)])
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
print("Longest Common subsequence:",s[::-1])
'''
#------------------------------------------------------------------------------
'''
#input:5
#0 1 0 0 1
#1 0 0 1 1
#0 0 0 0 0
#1 0 0 0 0
#1 0 0 0 1
#output:5----count no.of islands
def fun(l,i,j,n):
    if l[i][j]==0:
        return
    if l[i][j]==1:
        l[i][j]=0
    if i>0:
        fun(l,i-1,j,n)
    if j>0:
        fun(l,i,j-1,n)
    if i<n-1:
        fun(l,i+1,j,n)
    if j<n-1:
        fun(l,i,j+1,n)
    
n=int(input())
res=0
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            res+=1
            fun(l,i,j,n)       
print(res)
'''
#--------------------------------------------------------------------------------------------
'''
#Max area of the island
#input:
#5
#0 1 0 0 1
#1 0 0 1 1
#0 0 0 0 0
#1 0 0 0 0 
#1 0 0 0 1
#output:3
def area(l,n):
    m = 0
    def fun(i,j):
        if i < 0 or i >= n or j < 0 or j >= n or l[i][j] == 0:
            return 0
        if l[i][j] == 1:
            l[i][j] = 0
        area = 1
        area +=fun(i+1,j)
        area +=fun(i-1,j)
        area +=fun(i,j+1)
        area += fun(i,j-1)
        return area
    for i in range(n):
        for j in range(n):
            if l[i][j] == 1:
                c = fun(i,j)
                m = max(m,c)
    return m
    
n = int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split( ))))
print(area(l,n))
'''
#-------------------------------------------------------------------
'''
#input:7262 sec  ----- convert into hrs min and sec
#output:2h:1m:2s
a=7262
b=60*60
h=a//b
k=a%b
print("Hours:",h)
m=k//60
print("Minutes:",m)
s=k%60
print("Sec:",s)
print(h,"h:",m,"m:",s,"s")
'''
#---------------------------------------------------------
'''
#coins=[4,3,5]
#Rs:17
#output:4
coins=[4,3,5]
amount=16
coins.sort()
r=coins[::-1]
print(r)
l=[]
for i in r:o
    k=amount//i
    l.append(k)
    amount-=k
print(l)
'''
#-----------------------------------------------------------------------
'''
#year=360
#months=30
#weeks=6
n=65476
y=n//360
k=n%360
m=k//30
k1=k%30
d=k1%6
print(y,":years",m,":months",d,":days")
'''
