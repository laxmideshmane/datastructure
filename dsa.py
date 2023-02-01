from array import *

class DSA():
	def Array(self):
		
		arr=array('i',[])
		def insert():
			n=int(input("How many elements?"))
			for i in range(n):
				arr.append(int(input("Enter element:")))
		def display():
			print("Elements are:")
			for i in range(len(arr)):
				print(arr[i])
			print("length of array:",len(arr))
		def update():
			print("Update Operation:")
			j=int(input("Enter index:"))
			arr[j]=int(input("Enter new element at index:"))
			for i in range(0,len(arr)):
				print(arr[i])
		def delete():
			print("Before Delete element from array:",arr)
			arr.pop()
			print("Deleted successfully:",arr)
			


		while True:
			print("Array Implimentation:")
			print("1.insert")
			print("2.display")
			print("3.update")
			print("5.Exit")
			print("4.delete")
			ch=int(input("Enter Your choice(1-4):"));
			if(ch==1):
				insert()
			elif(ch==2):
				display()
			elif(ch==3):
				update()
			elif(ch==4):
				delete()
			
			elif(ch==5):
				print("DSA Implimentation:")
				print("1.Array")
				print("2.Stack")
				print("3.Queue")
				print("4.Linkedlist")
				print("5.exit")
				ch=int(input("Enter Your choice(1-4):"))
				break;
			else:	
				print("please enter correct choice:")
			print("\n\n")
		
		
	
	def Queue(self):
	
		queue=[]	
		def enqueue():
			element=int(input("Enter element in queue:"))
				
			queue.append(element);
			print(element,"added sucessfully")
		def dequeue():
			if not queue:
				return "Empty Qupeue"
			else :
				r=queue.pop(0)
				print("Remove element",r)
					
		def display():
			print(queue)	
			
		def size():
			print("size of queue is",len(queue))


		while True:
			print("Queue Implimentation:")
			print("1.Enqueue")
			print("2.Dequeue")
			print("3.Display")
			print("4.size")
			print("5.exit")
			ch=int(input("Enter Your choice(1-4):"))
			if(ch==1):
				enqueue()
				
			elif(ch==2):
				dequeue()
			elif(ch==3):
				display()
			elif(ch==4):
				size()
			elif(ch==5):
				print("DSA Implimentation:")
				print("1.Array")
				print("2.Stack")
				print("3.Queue")
				print("4.Linkedlist")
				print("5.exit")
				ch=int(input("Enter Your choice(1-4):"))
				break;
			else:	
				print("please enter correct choice")
			print("\n\n")
	

	
	def stack(self):
		s=[]
		top=None
		def isEmpty(stk):
			if(stk==[]):
				return "Underflow"
			else:
				return False

		def push(stk,item):
			stk.append(item)#append method is used to insert data into stack
			
			top=len(stk)-1

		def s_pop(stk):
			if(isEmpty(stk)):
				return "underflow"
			else:
				i=stk.pop()
				
			return i
				
		def peek(stk):
			if (isEmpty(stk)):
				return "Underflow"
			else:
				top=len(stk)-1
				print("Peek success:",stk[top])		
		def display(stk):
			top=len(stk)-1
			print(stk[top])
			for i in range(top-1,-1,-1):
				print(stk[i])




		while True:
			print("Stack Implimentation:")
			print("1.push")
			print("2.pop")
			print("3.peek")
			print("5.Exit")
			print("4.display")
			ch=int(input("Enter Your choice(1-4):"));
			if(ch==1):
				item=int(input("Enter item into stack:"))
				push(s,item)
				print("%d added sucess"%item)
				
				
			elif(ch==2):
				item=s_pop(s);
				print('%d poped success'%item)
				
			elif(ch==3):
				peek(s)
			
				
			elif(ch==4):
				display(s)
				
			elif(ch==5):
				print("DSA Implimentation:")
				print("1.Array")
				print("2.Stack")
				print("3.Queue")
				print("4.Linkedlist")
				print("5.exit")
				ch=int(input("Enter Your choice(1-4):"))
				break;
			else:	
				print("please enter correct choice")
			print("\n\n")

class Node:
	def __init__(self,data):
		self.data=data
		self.ref=None
class linkedlist(Node):

	def __init__(self):
		self.head=None
	def print_LL(self):
		n=self.head
		if n is None:
			print("Linked list is Empty")
		while n is not None:
			print(n.data)
			n=n.ref
			print("Address of Next Node:",n)

	def add_begin(self,data):
		newnode=Node(data)
		newnode.ref=self.head
		self.head=newnode

	def add_before(self,data,x):
		if self.head is None:
			print("Linklist is empty")
			return
		if self.head.data==x:#if we have to add before first node then add newnode as head
			newnode=Node(data)
			newnode.ref=self.head
			self.head=newnode
			return
		n=self.head
		while n.ref is not None:# node ref is not none 
			if n.ref.data==x:#here find privious node of given x
				break
			n=n.ref
		if n.ref is None:
			print("Node is not present in list")
		else:
			newnode=Node(data)
			newnode.ref=n.ref
			n.ref=newnode
		 
							

	def delete_by_val(self,x):
		if self.head is None:
			print("linkList is Empty")
			return
		
		if x==self.head.data:# if given node is head then 
			self.head=self.head.ref#address of head give to second node
			return
		n=self.head
		while n.ref is not None:
			#check given value is equal to any of the list except head
			#(traverse linked list for find out privious node of given node(x))
			if x==n.ref.data:
				break
			n=n.ref# increse node by 1 if does not matches with data
		#if matches then address of prvious node of given node point to next node of given node(After break of while it's here)
		n.ref=n.ref.ref

l1=linkedlist()
print("DSA Implimentation:")
print("1.Array")
print("2.Stack")
print("3.Queue")
print("4.Linkedlist")
print("5.exit")
ch=int(input("Enter Your choice(1-4):"))
while True:
	
	
	print("Linklist Implimentation:")
	print("1.add_begin")
	print("2.add_before")
	print("3.delete_by_val")
	print("4.print_LL")
	print("5.exit")
	ch=int(input("Enter Your choice(1-4):"))
	if(ch==1):
		n=int(input("How many elements would you like to add??"))
		for i in range(n):
			data=int(input("Enter data:"))
			l1.add_begin(data)
		
	elif(ch==2):	
		
		data=int(input("Enter newdata :"))
		x=int(input("Enter existing data from list"))
		l1.add_before(data,x)		
		
	elif(ch==3):
		x=int(input("Enter data for delete from existing list:"))
		l1.delete_by_val(x)
	elif(ch==4):
		l1.print_LL()
	elif(ch==5):
			
		break;
	else:	
		print("please enter correct choice")
		print("\n\n")
				

			
my=DSA()

while True:
	print("DSA Implimentation:")
	print("1.Array")
	print("2.Stack")
	print("3.Queue")
	print("4.Linkedlist")
	print("5.exit")
	ch=int(input("Enter Your choice(1-4):"))
	if(ch==1):
		my.Array()
	elif(ch==2):			
		my.stack()
	elif(ch==3):
		my.Queue()
	elif(ch==5):
		break;
	else:	
		print("please enter correct choice")
		print("\n\n")
			
#print(my.que())
