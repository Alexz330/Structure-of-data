class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self,index):
        return self.data[index]

    def push(self,item):
        self.data[self.length] = item
        self.length +=1
        return self.data

    def myDelete(self, index):
        
        item = self.data[index]
        self.shiftIndex(index);
        return item;

    def shiftIndex(self,index):
        for x in range(index , self.length-1):
            self.data[x] = self.data[x+1]
        del self.data[self.length -1]
        self.length -= 1
      


arreglito = MyArray();


arreglito.push('alexis')
arreglito.push('Diego')
arreglito.push('Diego')
arreglito.push('Diego')




arreglito.myDelete(0)
