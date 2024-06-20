'''
#input:  5
# 1  word (1----insert the string)
# 1  word ( no duplicates should be added )  
# 3 wo (3----check prefix is available in list or not)
# 4 word(4----pop the string from list)
# 2 word(2------search the string is available or not)
#output:
#      1
#      False
def insert(s,l):
    l.add(s)
    #print(l)
def search(s,l):
    for i in l:
        if i==s:
            print("True")
            break
    else:
        print("False")
def prefix(s,l):
    c=0
    for i in l:
        if s in i:
            c+=1
    print(c)
    
def pop1(s,l):
    l.remove(s)
    
n=int(input())
l=set()
while(n>0):
    choice=int(input())
    s=input()
    
    if choice==1:
        insert(s,l)
    if choice==2:
        search(s,l)
    if choice==3:
        prefix(s,l)
    if choice==4:
        pop1(s,l)
    n-=1
'''
class node:
    def __init__(self):
        self.d={}      #dictionary to strore the characters
        self.flag=0
class tries:
    def __init__(self):
        self.root=node()
        
    def insert(self,str1):
        t=self.root
        for i in str1:
            if i not in t.d:   #if character is not in dictionary ,craete a new trie
                t.d[i]=node()               
            t=t.d[i]
        t.flag=1
        
    def search(self,str1):
        t=self.root
        for i in str1:
            if i not in t.d:
                return False
            t=t.d[i]
        if t.flag==1:
            return True
        else:
            return False
        
    def search_prefix(self,s):
        t=self.root
        for i in s:
            if i not in t.d:
                return False
            t=t.d[i]
        return True
    
    def allwords_prefix(self,s1):
        def fun(t,s):
            if (t.flag==1):
                print(s)
            for i in t.d:
                fun(t.d[i],s+i)    
        t=self.root
        s=""
        for i in s1:
            if (i in t.d):
                s=s+i
                t=t.d[i]
            else:
                return
        fun(t,s)
    def largest_word_prefix(self,s):
        t=self.root
        for i in s:
            
t=tries()
n=int(input())
for i in range(n):
    a,s=input().split()
    if a=='1':
        t.insert(s)
    if a=='2':
        print(t.search(s))
    if a=='3':
        print(t.search_prefix(s))
    if a=='4':
        t.allwords_prefix(s)



#prefix with longest string
#lexicographical small longest string
#count no.of words with w
#erasing words
        
        

    
        

                
    
    