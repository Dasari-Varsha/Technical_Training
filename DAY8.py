class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None
        
    def create(self,data):
        if(self.root==None):
            self.root=node(data)
            return self.root
        
    def insert(self,root,data):
        if data>root.data:
            if root.right:
                self.insert(root.right,data)
            else:
                root.right=node(data)
        if data<root.data:
            if root.left:
                self.insert(root.left,data)
            else:
                root.left=node(data)
                
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
            
    def preorder(self,root):
        if root:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
            
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
            
    def addBT(self,root):
        if (root == None):
            return 0
        return (root.data + self.addBT(root.left) + self.addBT(root.right))
   
    def OddEvenDifference(self,root,s1,s2):
        if (root == None):
            return
        else:
            if (root.data % 2 == 0):
                s1.append(root.data)
            else:
                s2.append(root.data) 
        self.OddEvenDifference(root.left,s1,s2)
        self.OddEvenDifference(root.right,s1,s2)
        return s1,s2    
        
    def EvenSum(self,root):
        if root==None:
            return 0
        esum=0
        if root.data%2==0:
            esum=esum+root.data
            #print(esum)
        esum+=self.EvenSum(root.left)
        esum+=self.EvenSum(root.right)
        return esum
    
    def OddSum(self,root):
        if root==None:
            return 0
        osum=0
        if root.data%2==1:
            osum=osum+root.data
            #print(esum)
        osum+=self.OddSum(root.left)
        osum+=self.OddSum(root.right)
        return osum
    
    def Even_Odd_Diff(self,root):
        if root==None:
            return 0
        es=0
        if root.data%2==0:
            es=es+root.data
        else:
            es=es-root.data
        es+=self.Even_Odd_Diff(root.left)
        es+=self.Even_Odd_Diff(root.right)
        return es
    
    def height_of_tree(self,root):
        if root==None:
            return -1
        le=self.height_of_tree(root.left)
        re=self.height_of_tree(root.right)                      
        return max(le,re)+1
    
    def check_balanced_tree(self,root):
        return abs(self.height_of_tree(root.left)-self.height_of_tree(root.right))<=1
    '''
    def no_of_leaf_nodes(self,root):
        c=0
        if root==None:
            return 
        if root.left==None and root.right==None:
            print(root.data)
            c=c+1
        else:
            c+=self.no_of_leaf_nodes(root.left)
            c+=self.no_of_leaf_nodes(root.right)
        return c
        '''
    '''
    def sum_of_leaf_nodes(self,root):
        s=0
        if root==None:
            return
        if root.left==None and root.right==None:
            s+=root.data
        else:
            s+=self.sum_of_leaf_nodes(root.left)
            s+=self.sum_of_leaf_nodes(root.right)
        return s
        '''
    
    def search_node(self,root,x):
        if root==None:
            return False
        if root.data==x:
            return True
        
        if x>root.data:
            return self.search_node(root.right,x)
        else:
            return self.search_node(root.left,x)
        
    def depth(self,root,y,c):
        if root==None:  #depth of root node is always zero
            return -1
        if root.data==y:
            return c
        if root.data>y:
            return self.depth(root.left,y,c+1)
        else:
            return self.depth(root.right,y,c+1)
    def left_view(self,root,c,l):
        if root==None:
            return
        if c not in l:
            l.append(c)
            print(root.data,end=" ")
        self.left_view(root.left,c+1,l)
        self.left_view(root.right,c+1,l)
    def right_view(self,root,c,l):
        if root==None:
            return
        if c not in l:
            l.append(c)
            print(root.data,end=" ")
        self.left_view(root.right,c+1,l)
        self.left_view(root.left,c+1,l)
    def top_view(self,root,c,d):
        if root==None:
            return
        if c not in d:
            d[c]=root.data
            #print(d)
            print(root.data,end=" ")
        self.top_view(root.left,c+1,d)
        self.top_view(root.right,c-1,d)
    def left_sum_of_tree(self,root):
        if root is None:
            return 0
        return root.data + self.left_sum_of_tree(root.left) + self.left_sum_of_tree(root.right)
    def right_sum_of_tree(self,root):
        if root is None:
            return 0
        return root.data + self.right_sum_of_tree(root.left) + self.right_sum_of_tree(root.right)
      
        

        
    
    
t1=tree()
root=t1.create(15)
print(root.data)
t1.insert(root,4)
t1.insert(root,18)
t1.insert(root,10)
t1.insert(root,2)
#t1.insert(root,17)
#t1.insert(root,19)
#t1.insert(root,4)
#t1.insert(root,3)
#t1.insert(root,22)
t1.preorder(root)
print()
t1.inorder(root)
print()
t1.postorder(root)
print()
print("Height of the tree:",t1.height_of_tree(root))       #Height of tree=Max No.of edges in the edges
print("sum of all elemnts:",t1.addBT(root))
if(t1.check_balanced_tree(root)):
    print("YES ,IT IS BALANCED")
else:
    print("Tree NOT BALANCED")
#print("Sum:",t1.eon(root,0))
res1,res2=t1.OddEvenDifference(root,[],[])
print("Diff of even and odd::",abs(sum(res1)-sum(res2)))
#print(res1,res2)
print("Even sum of elements:",t1.EvenSum(root))
print("Odd sum of elements:",t1.OddSum(root))
print("Diff:",t1.Even_Odd_Diff(root))
#print("No.of Leaf Nodes:",t1.no_of_leaf_nodes(root))
#print("Sum of leaf Nodes:",t1.sum_of_leaf_nodes(root))
print("Searching element:")
if(t1.search_node(root,150)):
    print("Yes,Node is found")
else:
    print("Not Found")
print("Depth:",t1.depth(root,5,0))
print("Top View:")
t1.top_view(root,0,{})
print()
print("Left View:")
t1.left_view(root,0,[])
print()
print("Right View:")
t1.right_view(root,0,[])
print()
print("Sum of right Sub tree :",t1.right_sum_of_tree(root.right))
print("Sum of Left Sub tree :",t1.right_sum_of_tree(root.left))
