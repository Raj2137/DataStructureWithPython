class node():

  def __init__(self, num):
    self.data= num
    self.next= None

class Linked_list():

  def __init__(self):
    self.head= None
    self.next= None

  def endme(self, data):
    if self.head is None:
      self.head= node(data)
    else:
      current= self.head
      while current.next is not None:
        current= current.next
      current.next= node(data)

  def lentho(self):
    count=0
    current= self.head
    while current:
      count=count+1
      current= current.next
    print(count)

  def removo(self, num):
    current= self.head
    #yo= current.next
    if current.data==num:
      #yo= self.head
      self.head= current.next
    while current is not None:
      if current.data==num:
        break
      prev= current
      current= current.next

    prev.next= current.next
  
        
    

  def printo(self):
    current= self.head
    while current:
      print(current.data)
      current= current.next

yo= Linked_list()
yo.endme(6)
yo.endme(7)
yo.endme(8)
yo.endme(8)
yo.endme(9)
yo.removo(8)
yo.printo()
yo.lentho()
