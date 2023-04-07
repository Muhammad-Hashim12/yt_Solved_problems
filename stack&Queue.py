class Stack:
    def __init__(self):
        self.list=[]
    
    def push(self,data):
        self.list.append(data)
        print(self.list)
    def pop(self):
        if self.list!=[]:
            self.list.pop()
            print(self.list)

Stack_object=Stack()

Stack_object.push(1)
Stack_object.push(2)
Stack_object.push(3)
Stack_object.pop()
Stack_object.pop()
Stack_object.pop()


class Queue:
    def __init__(self):
        self.list=[]
    def add(self,data):
        self.list.append(data)
        print(self.list)

    def remove(self):
        if self.list != []:
            self.list.pop(0)
            print(self.list)

Queue_object=Queue()

Queue_object.add(10)
Queue_object.add(20)
Queue_object.add(30)
Queue_object.remove()
Queue_object.remove()
Queue_object.remove()