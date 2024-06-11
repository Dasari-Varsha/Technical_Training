'''
#input:[1,2,3,4,1,2,3,1,2]
#output:[[1,2,3,4],[1,2,3],[1,2]]
#----['a','a','a','a',1,2,3,1,2]   [[1,2,3,4]]
#----['a','a','a','a','a','a',1,2]    [[1,2,3,4],[1,2,3]]
#----['a','a','a','a','a','a','a','a']    [[1,2,3,4],[1,2,3],[1,2]]


#input:[2,3,1,3,4,3,2]
#output:[[2,3,1,4],[3,2],[3]]
#----['a','a','a',3,'a',3,2]   [[2,3,1,4]]
#----['a','a','a','a','a',3,'a']    [[2,3,1,4],[3,2]]
#----['a','a','a','a','a','a','a']    [[2,3,1,4],[3,2],[3]]

#input:[4,5,2,1]
#outpit:[[4,5,2,1]]

l=[2,3,1,3,4,3,2]
result=[]
i=0
c=0
while(c!=len(l)):
    temp=[]
    for i in range(len(l)):
        if(not str(l[i]).isalpha()):
            if( l[i] not in temp):
                c+=1
                temp.append(l[i])
                l[i]='a'
    result.append(temp)
print(result)
'''
'''
#input:'the quick brown fox jumps over the lazy dog'
#output:yes ----it contains all the 26 characters in the string
s='the quick brown fox jumps over the lazy dog'
s1='abcdefghijklmnopqrstuvwxyz'
for i in range(97,123):
    if chr(i) not in s:
        print("NO")
else:
    print("YES")
    
a="the quick brown fox jumps over the lazy dog"
d=[0]*26
for i in a:
    if(i.islower()):
        d[ord(i)-97]+=1
print(all(d))


s="the 4quick br$%ownx fovEND jh45ums q.werp the lazy dogs"
flag=0
s1=set()
for i in s:
    if i.islower():
        s1.add(i)
if len(s1)==26:
    print("YES")
else:
    print("NO")
'''
'''
#printing the longest substring without repeating the character
#input:abfgresagtyuiofde
#outpit:12
a="abfgresagtyuiofde"
i=0
m=0
d={}
s=""
while(i<len(a)):
    while(i<len(a)):
        if (a[i] not in s):
            s=s+a[i]
            d[s[i]]=i
            print(d)
        else:
            if(len(s)>m):
                m=len(s)
            s=""
            break
        i=i+1
    i=d[a[i]]+1
print(m)
'''
'''

#Input:6
# 0 1 1 1 0 1
# 0 1 0 1 0 0
# 1 0 1 1 0 0
# 0 0 0 1 1 1
# 1 1 0 0 0 1
# 1 1 1 0 1 0
# position ---4 6

#output:  8 (remaining unburnt trees)
def fun(i,j,a,n):
    if i<0 or j<0 or i>=n or j>=n or a[i][j]!=1 :
        return
    if a[i][j]==1 :
        a[i][j]=2
    fun(i,j-1,a,n)
    fun(i-1,j,a,n)
    fun(i+1,j,a,n)
    fun(i,j+1,a,n)
    
a=[]
n=int(input())
for i in range(n):
    a.append(list(map(int,input().split())))
i=int(input())
j=int(input())
fun(i-1,j-1,a,len(a))
print(a)
c=0
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            c+=1
print(c)
'''
'''
#input:: 4
#t u e d
#f w o w
#r o e r
#d r u i
#word
#output: yes

def fun(i,j,k,t):
    if k==len(s):
        return 1
    if i<0 or j<0 or i>=n or j>=n or a[i][j]!=s[k]:
        return
    if a[i][j]==s[k]: 
        a[i][j]=0
    if(t!=1):
        t=fun(i+1,j,k+1)
        t=fun(i-1,j,k+1)
        t=fun(i,j-1,k+1)
        t=fun(i,j+1,k+1)
a=[]
n=int(input())
for i in range(n):
    a.append(input())
s="word"
c=0
for i in range(n):
    for j in range(n):
        if a[i][j]==s[0]:
            c=fun(i,j,1,0)
            if c==1:
                print("yes")
                break
if c==0:
    print("no")
'''
'''    
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
    def create(self,root,x):
        if(root==None):
            self.root=node(x)
        elif(root.data>x):
            self.create(root.left,data)
        else:
            self.create(root.right,data)
    def inorder(self,root):
        if root:
            inorder(root.left)
            print(root.data,end="")
            inorder(root.right)
    def preorder(self,root):
        if root:
            print(root.data)
            preorder(root.data)
            preorder(root.right,end="")
    def postorder(self,root):
        if root:
            postorder(root.left)
            postorder(root.right)
            print(root.data,end="")
t1=tree()
t1.create(root,10)
t1.create(root,20)
t1.create(root,30)
t1.create(root,15)
t1.create(root,5)
t1.preorder()
'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 

def inorder(root, answer):
    if root is None:
        return
    inorder(root.left, answer)
    answer.append(root.val)
    inorder(root.right, answer)
    return

root = TreeNode(10)
print(inorder(root))