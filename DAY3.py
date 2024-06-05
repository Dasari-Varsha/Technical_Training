class node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Single_Linked_List:
    def __init__(self):
        self.head=None
    def insert_Begin(self,value):
        newnode=node(value)
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def insert_End(self,value):
        newnode=self.head
        while(newnode.next!=None):
            newnode=newnode.next
        newnode.next=node(value)
    def sum1(self):
        temp=self.head
        s=0
        while(temp!=None):
            s+=temp.value
            temp=temp.next
        print("Sum of Elements:",s)
    def addeven(self):
        temp=self.head
        s=0
        while(temp!=None):
            if(temp.value%2==0):
                s+=temp.value
            temp=temp.next
        print("Even Sum:",s)
    def addodd(self):
        temp=self.head
        s=0
        while(temp!=None):
            if(temp.value%2==1):
                s+=temp.value
            temp=temp.next
        print("Odd Sum:",s)
    def delete_Begin(self):
        if(self.head==None):
            return
        self.head=self.head.next
    def delete_End(self):
        if self.head==None:
            return
        newnode=self.head
        while(newnode.next.next!=None):
            newnode=newnode.next
        newnode.next=None
    def search(self,value):
        ele=self.head
        flag=0
        while(ele.next!=None):
            if ele.value==value:
                flag=1
                break
            ele=ele.next
        if(flag==1):
            print("Element is Found")
        else:
            print("Not Found")
    def Traverse(self):
        newnode=self.head
        while(newnode!=None):
            print(newnode.value,end="->")
            newnode=newnode.next
        print()
    def middle_ele(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        print(slow.value)
    def length(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        if fast!=None:
            print("Odd length")
        else:
            print("Even Length")
    def sliding_window_sequence_of_numbers(self):
        temp=self.head
        c=1
        m=0
        while(temp.next.next!=None):
            if temp.value==temp.next.value-1:
                c=c+1
                temp=temp.next
                if c>m:
                    m=c   
            else:
                temp=temp.next
        print("Max length of sequences", m)
    def pairs(self):
        temp=self.head
        while(temp.next):
            temp1=temp.next
            while(temp1!=None):
                print(temp.value,temp1.value)
                temp1=temp1.next
            temp=temp.next
                
    def bubblesort(self):
        temp=self.head
        temp1=temp.next
        while(temp!=None and temp1!=None):
            while(temp1!=None):
                if temp.value>temp1.value:
                     temp.value,temp1.value=temp1.value,temp.value
                     temp1=temp1.next
                else:
                    temp1=temp1.next
            temp=temp.next
            temp1=temp.next
    def bubble(self):
        c=0
        p=None
        Temp=self.head
        while(Temp.next!=None):
            flag=0
            temp=self.head
            while(temp.next!=p):
                if temp.value > temp.next.value:
                    flag=1
                    temp.value,temp.next.value=temp.next.value,temp.value
                c=c+1
                temp=temp.next
            Temp=Temp.next
            p=temp
            if flag==0:
                break
        print("No.of Interations",c)
    def reverselist(self):
        prev=None                   #a=None
        current=self.head           #b=self.head
        while(current!=None):       #while(b!=None):
            nxt=current.next            #c=b.next
            current.next=prev           #b.next=a
            prev=current                #c=b
            current=nxt                 #b=c
        self.head=prev              #self.head=a
                
                    
                    
                                     
l=Single_Linked_List()
#l.insert_Begin(6)
#l.insert_Begin(5)
#l.insert_Begin(4)
#l.insert_Begin(3)
#l.insert_Begin(7)
#l.insert_Begin(11)
l.insert_Begin(10)
l.insert_End(50)
l.insert_End(30)
l.insert_End(80)
l.insert_End(70)
l.insert_End(40)
l.insert_End(20)
l.insert_End(60)
l.insert_End(90)
l.insert_End(55)
#l.insert_End(12)
#l.delete_Begin()
#l.delete_End()
l.Traverse()
l.addeven()
l.addodd()
l.search(30)
l.middle_ele()
l.length()
l.sum1()
l.sliding_window_sequence_of_numbers()
l.pairs()
l.bubblesort()
l.Traverse()
l.bubble()
l.Traverse()
l.reverselist()
l.Traverse()



