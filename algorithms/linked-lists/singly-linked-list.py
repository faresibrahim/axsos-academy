class SLNode:
  def __init__(self, value):
    self.value= value
    self.next=None

class SList:
  def __init__(self): #initialize an empty Single Linked List
    self.head=None

  def add_to_front(self, val):
    new_node=SLNode(val)
    new_node.next=self.head
    self.head=new_node
    return self #for chaining

  def print_values(self):
    runner=self.head
    while (runner != None):
      print(runner.value)
      runner = runner.next
    return self

  def add_to_back(self,val):
    new_node=SLNode(val)
    if(self.head == None): #means the list is empty
      self.head=new_node
      return self
    runner=self.head
    while(runner.next != None):
      runner=runner.next
    runner.next=new_node
    return self

  def remove_from_front(self):
    if self.head == None:
      return self
    current_head=self.head
    self.head=current_head.next
    return self

  def remove_from_back(self):
    if self.head == None: #if the list is empty then return
      return self

    if self.head.next==None: #if there is only one node in the list then we remove it
      self.head=None
      return self
    
    previous = None
    runner=self.head
    while(runner.next != None):
      previous=runner
      runner = runner.next
    previous.next=None
    return self


  def insert_at(self, index, value):
    if self.head == None:
      self.add_to_front(value)
      return self

    new_node=SLNode(value)
    current_index=0
    if current_index==index:
      self.add_to_front(value)
      return self

    runner=self.head
    while(runner != None):
      previous=runner
      runner=runner.next
      current_index += 1
      if(current_index==index):
        new_node.next=runner
        previous.next=new_node
        return self

    
