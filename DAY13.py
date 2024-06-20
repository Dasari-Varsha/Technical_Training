'''
#Leetcode 42
#Tapping Rain Water
#input:l=[4,3,4,5,6,1,0,6,7]
#output:12
#input:[2,7,2,3,6,7,1,0,5,7]
#output:20
#l=[2,5,2,3,6,7,1,0,5,7]
#2 5 5 5 6 7 7 7 7 7 ---->front to back
#7 7 7 7 7 7 7 7 7 7----->back to front
#take minimum from those 2 arrays and subtract respective building height then store that value is nothing but water stored


l=[4,3,4,5,6,1,0,6,7]
max1=l[0] 
max2=l[len(l)-1]
count=0
for i in range(0,len(l)):
    if l[i]>max1:
        max1=l[i]
    for j in range(0,len(l),-1):
        if l[j]>max2:
            max2=l[j]
    k=min(max1,max2)
    count+=abs(k-l[i])
print(count)
               #OR
l=[4,3,4,5,6,1,0,6,7]
left=[0]*len(l)
right=[0]*len(l)
m=0
m1=0
for i in range(len(l)):
    if l[i]>m:
        m=l[i]
    left[i]=m
for i in range(len(l)-1,-1,-1):
    if l[i]>m1:
        m1=l[i]
    right[i]=m1
s=0
for i in range(len(l)):
    s=s+abs(min(left[i],right[i])-l[i])
print(s)
'''
'''
##Leetcode 322. Coin Change
#input:[1,3,4,5]
#amount:17

#   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
#1  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
#3  0 1 2 1 2 3 2 3 4 3  4  5  4  5  6  5  6  7 
#4  0 1 2 1 1 2 2 2 2 3  3  3  3  4  4  4  4  5
#5  0 1 2 1 1 1 2 3 2 2  2  3  3  3  3  3  4  4
#output: 4 coins
l=[1,3,4,5]
amt=17
dp=[[0] *(amt+1)] *(len(l)+1)
for i in range(len(l)):
    for j in range(amt+1):
        if i==0:
            dp[i][j]=j
            #print(dp)
        if j<l[i]:
            dp[i][j]=dp[i-1][j]
        if j>l[i]:
            k=j-l[i]
            dp[i][j]=min(dp[i-1][j],dp[i][k]+1)
#print(dp)
print("Minimum no.of coins required is:",dp[len(l)-1][amt-1])
                      #OR
#using list

def fun(l,n):
    l1=[-1]*(n+1)
    l1[0]=0
    for i in l:
        for j in range(1,n+1):
            if(j>=i):
                if(l1[j-i]!=-1):
                    if(l1[j]!=-1):
                        l1[j] = min(l1[j],l1[j-i]+1)
                    else:
                        l1[j]=l1[j-i]+1
    return (l1[-1])
l=list(map(int,input().split( )))
n=int(input())
print(fun(l,n))
'''

#input:4X3

# s - - -
# - - - -
# - - - e
#no.of paths from start to reach end
#output:38
def fun(i,j,c):
    if(i<0 or i>=n or j>=m or j<0 or (i==k and j==l)):
        return c
    if (i==n-1 and j==m-1):
        c = c+1
        return c
    vi.append((i,j))
    if((i-1,j) not in vi):
        c = fun(i-1,j,c)
    if((i+1,j) not in vi):
        c = fun(i+1,j,c)
    if((i,j-1) not in vi):
        c = fun(i,j-1,c)
    if((i,j+1) not in vi):
        c = fun(i,j+1,c)
    vi.pop()
    return c
n = int(input())
m = int(input())
vi=[]
k=int(input()) #index value of abstacle
l=int(input()) #index of abstacle
print(fun(0,0,0))
    
        
        
        

        
    
    

                                                                                
        
        
    

        
    
        
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
        