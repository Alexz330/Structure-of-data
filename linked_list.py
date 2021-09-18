class Node:
	def __init__(self, data, next=None, previuous=None):
		self.data = data
		self.next = next
		self.previous = previuous


class SinglyLinkedList: 
	def __init__(self):
		self.tail = None
		self.size = 0


	def append(self, data):
		node = Node(data)

		if self.tail == None:
			self.tail = node
		else:
			current = self.tail

			while current.next:
				current = current.next
			current.next = node
		self.size += 1


	def size(self):
		return str(self.size)


	def iter(self):
		current = self.tail
		while current:
			val = current.data
			current = current.next
			yield val


	def delete(self, data):
		current = self.tail
		previus =  self.tail

		while current:
			if current.data == data:
				if current == self.tail:
					self.tail = current.next
				else:
					previus.next = current.next
					self.size-= 1
					print(f'mi loco se borro el valor {current.data}')
			previus = current
			current = current.next

	def search(self, data):
		for node in self.iter():
			if data == node:
				print(f"data {data} found!")
				return node

	def remplazar(self,data,dataReplace):
		current =  self.tail

		while current is not None:
			if(current.data == data):
				current.data = dataReplace
				return current.data
			current = current.next

		if(current == None):
			print(f'data not founded {data}')

			
		

					

wordList = SinglyLinkedList()
wordList.append('egg')
wordList.append('ham')
wordList.append('sausage')
wordList.append('spam')

dataReaplaace = wordList.remplazar('eg', 'karrot')
print(dataReaplaace)
