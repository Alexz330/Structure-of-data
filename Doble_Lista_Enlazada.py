class Node:
	def __init__(self, data, next=None, previuous=None):
		self.data = data
		self.next = next
		self.previous = previuous



class ListaDoble:

    def __init__(self) :
        self.first = None
        self.last = None
        self.size = 0
    
    def AppendFinal(self, data):
        node = Node(data)

        if self.first is None:
            self.first = node
            
        else:
            
            node.next = self.first
            self.first.previous = node
            self.first = node
    
    def AppendStart(self,data):
        cuurent = self.first
        node = Node(data)

        if self.first is None:
            self.first = node
        
        else:
            while cuurent.next is not None:
                cuurent = cuurent.next
            cuurent.next = node
            node.previous = cuurent

    def Print(self):
        current =  self.first
        while current is not None:
            print(current.data)
            current = current.next
    # def Delete(self, data, data_Delete):
    #     current = self.first
    #     previous = self.

smallList = ListaDoble()

smallList.AppendStart('1')
smallList.AppendStart('2')
smallList.AppendStart('3')
smallList.AppendStart('4')

    


smallList.Print()

