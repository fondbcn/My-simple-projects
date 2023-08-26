class Node:
  def __init__(self, data = None): 
    self.data = data
    self.next = None
    self.prev = None

class LinkedList:
  def __init__(self):  
    self.head = None
    self.tail = None
    self.count = 0

  def insert(self, data):    
    node=Node(data)
    if self.tail:
      node.prev = self.tail
      self.tail.next = node
      self.tail = node      
    else:
      self.head = node
      self.tail = node
    self.count += 1
    
  def insert_f(self, data):    
    node=Node(data)
    if self.head:
      node.next = self.head
      self.head.prev = node
      self.head = node      
    else:
      self.head = node
      self.tail = node
    self.count += 1
  
  def insert_sort(self, data):    
    node=Node(data)
    if self.tail:
      if node.data>self.tail.data:
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
      elif node.data>self.head.data and node.data<=self.tail.data:
        cur=self.head.next
        while cur!=self.tail:
          if node.data<cur.next.data and node.data>cur.data:
            cur.next.prev=node
            node.next=cur.next
            node.prev=cur
            cur.next=node
            return
          cur=cur.next
      elif node.data<self.head.data:
        node.next=self.head
        self.head.prev=node
        self.head=node        
    else:
      self.head = node
      self.tail = node
    self.count += 1
  
  def it_forw(self):
    current = self.head
    while current:
      yield current.data
      current = current.next
  
  def it_back(self):
    current = self.tail
    while current:
      yield current.data
      current = current.prev
    
  def find(self,val):
    for i in self.it_forw():
      if i==val:
        return True
    return False

  def __getitem__(self, index):
    if index > self.count - 1:
      return "Index out of range"
    current = self.head
    for i in range(index):
      current = current.next
    return current.data

  def __setitem__(self,index,val):
    if index > self.count - 1:
      return "Index out of range"
    current = self.head
    for i in range(index):
      current = current.next
    current.data=val    
      
  def del_n(self,val):
    cur=self.head
    while cur:
      if cur.data==val:
        if cur.next!=None and cur.prev!=None:
          cur.prev.next,cur.next.prev=cur.next,cur.prev          
          del cur
          return
        elif cur.next==None:
          self.tail=cur.prev
          cur.prev.next=None
        else:
          self.head=cur.next
          cur.next.prev=None
      cur=cur.next
  
  # def del_n_s(self,val):
    # cur=self.head
    # while cur:
      # if self.head.data==val:
        # cur=cur.next
        # return
      # elif cur.next:
        # if cur.next.data==val:
          # cur.next=cur.next.next
          # return
      # cur=cur.next
      
  def rev(self):
    cur = self.head
    while cur:      
      tmp=cur.next
      cur.next=cur.prev
      cur.prev=tmp 
      cur=tmp      
    t=self.head
    self.head=self.tail
    self.tail=t

  def sort(self):
    if self.head == None:  
      return  
    else:   
      current = self.head  
      while current.next:   
        index = current.next  
        while index:  
          if current.data > index.data:  
            temp = current.data  
            current.data = index.data  
            index.data = temp  
          index = index.next  
        current = current.next     

  def mer_f(self):
    slw=self.head
    fst=self.head.next
    while fst and fst.next:
      slw=slw.next
      fst=fst.next.next
    cur=slw.next
    cur.prev=slw.next=None
    while cur:
      t=cur.next
      cur.next=cur.prev
      cur.prev=cur
      cur=t
    tr=cur
    cur=self.tail
    self.tail=tr
    fr=self.head
    cur=cur.prev
    while cur:
      tmp1=fr.next
      tmp2=cur.next
      fr.next=cur
      cur.next=tmp1
      cur.prev=fr
      fr,cur=tmp1,tmp2

l = LinkedList()
l.insert_sort(30)
l.insert_sort(40)
l.insert_sort(20)
l.insert_sort(19)
l.insert_sort(50)
l.insert_sort(33)
l.insert_sort(25)
l.insert_sort(100)
print(list(l.it_forw()))
l.mer_f()
print(list(l.it_forw()))
print(list(l.it_back()))