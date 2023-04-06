class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None

    def printlist(self):
        current=self.head
        while current!=None:
            print(current.data)
            current=current.next
    
    def insertATbegining(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
        else: 
            newnode.next=self.head
            self.head=newnode

    def insertbetween(self,prev,data):
        newnode=Node(data)
        newnode.next=prev.next
        prev.next=newnode


    def insertATEnd(self,data):
        newnode=Node(data)
        prev=self.head
        if self.head==None:
            self.head=newnode
        else:
            while prev.next !=None:
                prev=prev.next
            prev.next=newnode
    def delete(self,key):
        temp=self.head
        if temp.next!=None:
            if temp.data==key:
                self.head=temp.next
                temp=None
            else:
                while temp!=None:
                    if temp.data==key:
                        break
                    prev=temp
                    temp=temp.next
                #if Node not Found to delete
                if temp==None:
                    print("node which you want to be deleted is not found")
                    return
                # if Node found to delete
                prev.next=temp.next
                temp=None
                return
        else:
            self.head=None

    def search(self,key):
        temp=self.head
        while temp!=None:
            if temp.data==key:
                print("Node is found")
                return True
            temp=temp.next
        print("The Node is Not Found Cry!!!")
        return False







l=LinkedList()
l.insertATEnd(12)
l.insertATEnd(1)
l.insertATEnd(15)
l.insertATEnd(200)
l.insertbetween(l.head.next, 100)
l.delete(200)
l.printlist()
l.search(15)
print(l.search(12))
print(l.search(1000))


            

        


