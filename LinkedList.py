class Node:
	def __init__(self,data):
		self.data=data
		self.next=None


class LinkedList:
	def __init__(self):
		self.head=None

	def push(self,data):
		new_node=Node(data)
		if self.head==None:
			self.head=new_node
		else:
			new_node.next=self.head
			self.head=new_node

	def Add_at_last(self,data):
		new_node=Node(data)
		if self.head==None:
			self.head=new_node
		temp=self.head
		while temp.next!=None:
			temp=temp.next
		temp.next=new_node

	def len(self):
		temp=self.head
		count=0
		while temp is not None:
			count+=1
			temp=temp.next
		return count


	def print(self):
		temp=self.head

		while temp!=None:
			print(temp.data,end="->")
			temp=temp.next
	

	def search(self,key):
		temp=self.head
		while temp!=None:

			if temp.data==x:
				return True
			temp=temp.next
		return False


	def insert_At_k_pos(self,data,pos):
		length=self.len()
		new_node=Node(data)
		if pos> length or pos<=0:
			return "Enter appropriate position"
		elif pos==length:
			self.Add_at_last(data)
		elif pos==1:
			new_node.next=self.head
			self.head=new_node
		else:
			cur=self.head
			prev=cur
			pos-=1
			while pos!=0:
				prev=cur
				cur=cur.next
				pos-=1
			prev.next=new_node
			new_node.next=cur
		return "Insertion Succesfull!!!"

	def delete_at_beg(self):

		if self.head==None:
			return "Can't be deleted"
		else:
			self.head=self.head.next
			return "Deletion Successfull!!!"
	def delete_at_end(self):
		if self.head==None:
			return "Can't be deleted"
		else:
			temp=self.head
			prev=self.head
			while temp.next!=None:
				prev=temp
				temp=temp.next
			prev.next=None 
			return "Deletion Successfull!!!"
	def deletion_at_kth(self,pos):
		length=self.len()
		if pos> length or pos<=0:
			return "Enter appropriate position"
		elif self.head==None:
			return "Can't be deleted"
		else:
			if pos==1:
				return self.delete_at_beg()
			elif pos==length:
				return self.delete_at_end()
			else:
				cur=self.head
				pos-=1
				while pos!=1 and cur!=None:
					cur=cur.next
					pos-=1
				cur.next=cur.next.next
			return "Deletion Successfull!!!"
	def reverse(self):
		prev=None
		cur=self.head
		while cur!=None:
			up_next=cur.next 
			cur.next=prev 
			prev=cur
			cur=up_next
		self.head=prev
		return "LINKED LIST GOT REVERSED!!!"


 
    
