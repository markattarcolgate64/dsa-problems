class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None 

class LinkedList: 
    
    def __init__(self):
        self.head = None 

    def buildList(self):
        for i in range(5):
            newNode = Node(i)
            if i == 0:
                self.head = newNode
                currentNode = self.head
            else:
                currentNode.next = newNode 
                currentNode = currentNode.next 

    def printList(self, node=None):
        if node:
            current = node
        else:
            current = self.head

        while current != None:
            print(current.value)
            current = current.next

    
    def insertAtEnd(self, insertValue):

        current = self.head
        while current.next != None:
            current = current.next

        insertNode = Node(insertValue)
        current.next = insertNode

            
        

    def insertAtBeginning(self):
        #3,8 9, (2),  3,8,2,9


        pass 


    def getSizeList(self):
        current = self.head
        size = 0 
        while current:
            current = current.next
            size +=1

        return size 


    def insertAtIndex(self, index, value):
        if index < 0:
            self.insertAtBeginning()
        size = self.getSizeList()
        if size <= index:
            index = size - 1
        
        current = self.head
        count = 0 
        for i in range(1, index):
            current = current.next
        print(current.value)
        priorNode = current 
        nodeAtIndex = current.next
        newNextNode = Node(value) 
        priorNode.next = newNextNode
        newNextNode.next = nodeAtIndex       
        #current should be at the node before the index


    def handleErrorIndex(self, index):
        if index < 0:
            return -1
        
        size = self.getSizeList()
        #Handles cases where index is larger than size
        if size <= index:
            index = size - 1
        
        return index 

    
    def deleteNode(self, index):
        
        
        #Moves to node behind node and then skips it in linked list
        #Need to deal with zero case
        current = self.head
        for i in range(1, index):
            current = current.next
        if index == 0:
            self.head = current.next
        else:
            current.next = current.next.next

    #Will edit the last index in the list 
    def editNode(self,index, editValue):
        index = self.handleErrorIndex(index) 
        
        if index == -1:
            print("Index was negative")
            return None
        

        current = self.head
        count = 0 
        while count < index:
            current = current.next
            count += 1
        #3
        #0 -> 1 -> 2 -> 3 
        #0 -> 1 -> 2 -> 3 
        current.value = editValue

        return current
    

    def reverseList(self):
        #Loop to the end and reassign each nodes next to the next before 
        #1.next = 2 
        #2.next = 3
        #2.next = 1 
        #Store preiovus node
        prevNode = self.head

        if prevNode.next == None:
            return prevNode

        
        #0 -> 1 -> 2 
        #Store 2 
        #Store 1 
        #Turn 1 back to zero 
        #Next iteration
        current = prevNode.next  
        prevNode.next = None
        #0 -> 1 

        #0 1
        #next = 2 
        #temp = 1 
        #1-> 0 
        #prevNode = 1 
        #current = 2 

        #next = 3 
        #temp = 2
        #2 -> 1 
        #prevNode = 2
        #

        while current != None:
            nextNode = current.next 
            temp = current 
            current.next = prevNode 
            prevNode = temp 
            current = nextNode

        return prevNode

    #Other methods: editNode

def main():
    linkedList = LinkedList()
    linkedList.buildList()
    reverseHead = linkedList.reverseList()
    linkedList.printList(reverseHead)

    


if __name__ == "__main__":
    main()