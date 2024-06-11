'''
#input:list=[1,2,3,4,5,6]
#output:print the 3 combinations   of numbers
# 1 2 3
# 1 2 4
# 1 2 5
#1 2 6................4 5 6

l=[3,2,5,4,1,6,8] #-----------------using for loop O( N*N*N)
n=len(l)
print(l)
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            print(l[i],l[j],l[k])


def combinations(l,k):   #--------------using recursions by 2 functions
    def fun(curr,start):
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+1)
        return
    fun([],0) 
l=[3,2,5,4,1,6,8]
k=3
combinations(l,k)
#-----------------------------------------------------------------------------------

def fun(l,curr,start,n):     #----------------using recursion 1 function
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(l)):
            fun(l,curr+[l[i]],i+1,n)
        return
l=[3,2,5,4,1,6,8]
k=3
fun(l,[],0,k)
'''
#----------------------------------------------------------------------------------
'''
#input: school
#       3
#       L 2---->hoolsc
#       R 3---->oolsch
#       L 1---->chools
#output: yes  (hoc-------is anagram of(sch,cho.hoo,ool))
s="school"
n=len(s)
k=3
l=[2,3,1]
s1=""
t=""
for i in l:
    s1=s[i:]+s[:i]
    print(s1)
    t+=s1[0]
print(t)
sub1=""
s=list(s)
for i in range(len(s)):
    for j in range(i+1,len(s)):
        sub=s[i:j+1]
        if len(sub)==k:
            sub1=sub1+[sub]
print(sub1)
'''
#-----------------------------------------------------------------------------------------
'''
s=input()
n=int(input())
l1=[2,3,1]
l=[]
s=list(s)
for i in range(len(s)):
    for j in range(i+1,len(s)):
        sub=s[i:j+1]
        if len(sub)==n:
            l=l+[sub]
            #print(sub)
print(l)
s1=[]
for i in l1:
    s1=s1+list(s[i])
#s1=s1.sort()
s1.sort()
if s1 in l:
    print("yes",s1)
    
'''
#-------------------------------------------------------------------------------
'''
def isprime(n):
    if n==1:
        return 1
    if n==2:
        return 1
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    return 1
    
n=int(input())
for i in range(1,(n//2)+1):
    if isprime(i) and isprime(n-i):
        print("yes")
        break
else:
    print("No")

'''
#--------------------------------------------------------------------------
'''
#input:
#    2
#    polikujmnhytgbvfredcxswqaz
#    abcd
#    qwryupcsfoghjkldezxwbintma
#    ativedoc
#Output:
#      adca
#      codevita
n=int(input())
while(n):
    s1=input()
    s2=input()
    s=''
    for i in s1:
        if i in s2:
            s=s+(i*s2.count(i))
    print(s)
    n-=1
'''
#-----------------------------------------------------------------------------
'''
#input:
#[13,9,4,10,5,7]
#output:30
#l=[9,1,19,20,30,3]
#output:58
def fun(l):
    if len(l)==0:
        return 0
    if len(l)==1:
        return l[0]
    if len(l)==2:
        return max(l)
    left=l[0]+fun(l[2:])
    right=l[1]+fun(l[3:])
    return max(left,right)
l=[9,1,19,20,30,3]
print(fun(l))
'''
#codechef




    
     
    
    
    
    



