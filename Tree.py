class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class Tree:   
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root.val

    def add(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            return self._add(val, self.root)        

    def _add(self, val, curnode):
        if val>curnode.val:
          if curnode.right !=None:
            self._add(val,curnode.right)
          else:
            curnode.right=Node(val)
        elif val<curnode.val:
          if curnode.left !=None:
            self._add(val,curnode.left)
          else:
            curnode.left=Node(val)
        else:
          print(f'{val} already exist!')
          return          

    def array_to_bst(self,nums):    
        nums.sort()
        if not nums:
          return None
        mid_val = len(nums)//2
        node = Node(nums[mid_val])       
        self.add(node.val)       
        node.left = self.array_to_bst(nums[:mid_val])
        node.right = self.array_to_bst(nums[mid_val+1:])       
    
    def find(self, value):
        if self.root:
            print(bool(self._find(value, self.root)))
        else:
            print(False)

    def _find(self, value, node):
        if value == node.val:
            return node
        elif value < node.val and node.left:
            return self._find(value, node.left)
        elif value > node.val and node.right:
            return self._find(value, node.right)

    def deleteTree(self):
        self.root = None

    def print_in(self):
        if self.root:
            self._print_in(self.root)

    def _print_in(self,node):
        if node:
          self._print_in(node.left)
          print(node.val)
          self._print_in(node.right)      
    
    def print_pre(self):
        if self.root:
            self._print_pre(self.root)

    def _print_pre(self,node):
        if node:
          print(node.val)
          self._print_pre(node.left)         
          self._print_pre(node.right)
          
    def print_post(self):
        if self.root:
            self._print_post(self.root)

    def _print_post(self,node):
        if node:
          self._print_post(node.left)        
          self._print_post(node.right)
          print(node.val)
    
    def clos(self,target):
        if self.root:
          print(self._clos(self.root,target))
    
    def _clos(self,curnode,value):
        a=curnode.val
        kid=curnode.right if value>a else curnode.left
        if not kid:
          return a
        b=self._clos(kid,value)
        return min(a,b,key=lambda x:abs(value-x))        

    def is_BST(self):
        l1=list(self._in_BST(self.root))
        l2=l1[1:]
        return all(a<b for a,b in zip(l1,l2))
    
    def _in_BST(self,node):
        if node:
          yield from self._in_BST(node.left)
          yield node.val
          yield from self._in_BST(node.right)

    def minValueNode(node):
        current = node
        while current.left:
          current = current.left
        return current

    def maxValueNode(node):
        current = node
        while current.right:
          current = current.right
        return current 

    def delt(self, value):
        if self.root:
          return self._deleteNode(self.root, value)
      
    def _deleteNode(self,curnode, value):        
        if value < curnode.val:
          curnode.left = self._deleteNode(curnode.left, value)
        elif value > curnode.val:
          curnode.right = self._deleteNode(curnode.right, value)
        else:  
          if curnode.left is None:
            temp = curnode.right
            curnode = None
            return temp
          if curnode.right is None:
            temp = curnode.left
            curnode = None
            return temp
          temp = self.minValueNode(curnode.right)          
          curnode.right = self._deleteNode(curnode.right, temp.val)
          curnode.val = temp.val
        return curnode   

    def height(self,value):
        if self.root!=None:
          return self._height(self.find(value))
        else:
          return 0   
    
    def _height(self,curnode):
        if curnode is None:
          return 0
        return max(self._height(curnode.left), self._height(curnode.right))+1

    def smallest(self,value):
        for i,j in enumerate(self._in_BST(self.root)):
          if i+1==value:
            return j
                 
    def _printTree(self, M, node, col, row, height):
        if node is None:
          return
        M[row][col] = node.val
        self._printTree(M, node.left, col-pow(2, height-2), row+1, height-1)
        self._printTree(M, node.right, col+pow(2, height-2), row+1, height-1)
 
    def getcol(self,h):
        if h == 1:
          return 1
        return 2*self.getcol(h-1)+1

    def TreePrinter(self):
        h = self._height(self.root)
        col = self.getcol(h)
        print(col)
        M = [[0 for _ in range(col)] for __ in range(h)]
        self._printTree(M, self.root, col//2, 0, h)
        for i in M:
          for j in i:
            if j == 0:
                print(h*" ", end=" ")
            else:
                print('(',j,')', end=" ")
          print("\n")
    

tree = Tree()
l=[7,2,14,5,4,13,3,17,22,1]
tree.array_to_bst(l)