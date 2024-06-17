'''
def BFS(d,x):
    visited=[]  
    q=[x]    #append the start node to the queue
    while(q):
        for i in d[q[0]]: 
            if i not in visited and i not in q:  
                q.append(i) 
        a=q.pop(0)
        visited.append(a)
    return visited
d={5:[7,3],7:[5,4,3],4:[7,8,2,15],8:[4,3,2,9],3:[7,5,8,11],2:[4,8,10]}
print(BFS(d,5))
'''
#-------------------------------------------------------------------------------------------------
'''
#Dijikshtra's Algorithm
def dijikshtra(g,s):
    d={1:9999,2:9999,3:9999,4:9999,5:9999}
    d[s]=0
    visited=[]
    q=[s]
    while q:
        m=9999
        for i in q:
            if(d[i]<m):
                m=d[i]
                x=i
        for i in g[x]:
            if i[0] not in visited:
                q.append(i[0])
                if d[i[0]] > i[1] + d[x]:
                    d[i[0]] = i[1] + d[x]
        visited.append(x)
        q.remove(x)
    return d
g={1:[(2,2),(3,1)],2:[(1,2),(3,3),(4,4),(5,4)],3:[(1,1),(4,2)],4:[(2,4),(5,3)],5:[(3,4),(4,2)] }
s=1
print(dijikshtra(g,s))
'''
#----------------------------------------------------------------------------------------------------
'''
#input:
#l1=[6,3,2,9,4,7] #even 
#l2=[8,7,5,3,6,9]  #odd
#output:[13,11,9,15,9,7,5,11,11,9,7,13]
# from list1 even number should be added to every odd number in the list2
def fun(l1,l2,i,j):
    i=0
    l=[]
    while(i<len(l1)-1):
        if l1[i]%2==0:
            j=0
            while(j<len(l2)):
                if l2[j]%2==1:
                    l.append(l1[i]+l2[j])
                j+=1
                #print(l2[j])
        i+=1
        #print(l1[i])
    print(l)
l1=[6,3,2,9,4,7]
l2=[8,7,5,3,6,9]
fun(l1,l2,l1[0],l2[0])
'''
'''
def fun(l1, l2, i, j, l):
    if i >= len(l1) or j >= len(l2):
        return l
    
    if l1[i] % 2 == 0 and l2[j] % 2 == 1:
        l.append(l1[i] + l2[j])
    
    l = fun(l1, l2, i, j + 1, l)  
    return fun(l1, l2, i + 1, 0, l)

l1 = [6, 3, 2, 9, 4, 7]
l2 = [8, 7, 5, 3, 6, 9]
result = fun(l1, l2, 0, 0, [])
print(result)
'''
def fun(k,j,l2,s,l3):
    if k==len(l):
        return
    if k<len(l):
        if j<len(l1):
            #print(l[k], l1[j])
            if l[k]%2==0 and l1[j]%2!=0:
                s=s+l[k]+l1[j]
                l2.append(l[k]+l1[j])
                #print(l2)
            fun(k,j+1,l2,s,l3)
        else:
            l3.append(s)
            #print(s)
            fun(k+1,0,l2,s,l3)
l=[6,3,2,9,4,7]
l1=[8,7,5,3,6,9]
l2=[]
fun(0,0,l2,0,[])
print(l2)