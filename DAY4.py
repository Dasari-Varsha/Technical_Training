class node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_End(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            newnode=node(x)
            self.tail.next=newnode
            newnode.prev=self.tail
            self.tail=self.tail.next
            
    def insert_Begin(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            newnode=node(x)
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
    def traverse(self):
        temp=self.head
        while(temp!=None):
            print(temp.value,end="->")
            temp=temp.next
        print()
    def reverse(self):
        temp=self.tail
        while(temp!=None):
            print(temp.value,end="->")
            temp=temp.prev
        print()
    def search(self,value):
        temp1=self.head
        temp2=self.tail
        flag=0
        while(temp1!=temp2 and temp1!=temp1.next):#t!=t1 and t!=t1.next
            if temp1.value==value or temp2.value==value:
                flag=1
                break
            else:
                temp1=temp1.next
                temp2=temp2.prev
        if flag==1:
            print("Found")
        else:
            print("Not Found")
    def length(self):
        t1=self.head
        t2=self.tail
        flag=0
        while(t1!=t2 and t1!=t2.next):
            t1=t1.next
            t2=t2.prev
            if t1==t2:
                flag=1
                break
        if flag==0:
            print("Even Length")
        else:
            print("Odd length")
    def palindrome(self):
        t1=self.head
        t2=self.tail
        flag=0
        while(t1!=t2 and t1!=t2.next):
            if(t1.value==t2.value):
                t1=t1.next
                t2=t2.prev
            else:
                flag=1
                break
        if flag==1:
            print("not palindrome")
        else:
            print("Palindrome")
    def sorting(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        p1=slow
        while(slow!=fast):
            print(slow.value,end=" ")
            slow=slow.next
        p=self.head
        while(p!=p1):
            print(p.value,end=" ")
            p=p.next
    def sorting_swapping(self):
        slow=self.head
        fast=self.head
        while fast!=None:
            slow=slow.next
            fast=fast.next.next
        t1=self.head
        t2=slow
        while(t1!=t2 and t2!=None):
            t1.value,t2.value=t2.value,t1.value
            t1=t1.next
            t2=t2.next
        print()
                
l=dll()
#l.insert_Begin(10)
#l.insert_Begin(20)
#l.insert_Begin(30)
l.insert_End(10)
l.insert_End(20)
l.insert_End(30)
l.insert_End(40)
l.insert_End(50)
l.insert_End(60)
l.insert_End(70)
l.insert_End(80)
l.traverse()
l.reverse()
l.search(100)
l.length()
l.palindrome()
l.sorting()
l.sorting_swapping()
l.traverse()
            
           
            
            
            
    
    