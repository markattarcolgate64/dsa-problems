import sys
    

class MaxHeap:

    def __init__(self, maxSize):
        self.maxNum = 1 
        self.maxSize = maxSize
        self.heap = [0] * maxSize
        self.root = sys.maxsize
        self.size = 0 


    def parent(self, pos):
        return pos//2
    
    def leftChild(self, pos):
        return pos * 2
    
    def rightChild(self, pos):
        return (pos*2) + 1
    
    def swap(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = (self.heap[pos2], self.heap[pos1])

    def addNode(self, value: int):
        #First we have to check if we are over size
        if self.size == self.maxSize:
            return False 
    
        self.size += 1
        #Then we have to add the node at the end of the heap
        self.heap[self.size] = value
        #Then we need to swim the node up the max heap to find where it should land 
        #
        if (self.heap[self.size] > self.heap[self.parent(self.size)]):
            
         
            nodePos = self.size
            parentPos = self.parent(nodePos)
            while (self.heap[nodePos] > self.heap[parentPos]):
                self.swap(nodePos, parentPos)
                parentPos = self.parent(nodePos)
                nodePos = parentPos

    #Heapify at a particular node's position
    def heapify(self,pos):
        pass

    def printHeap(self):
        for i in range(1, (self.size //2) +1):
            print("Parent:", self.heap[i], "Left:", self.heap[self.leftChild(i)], "Right:", self.heap[self.rightChild(i)])


        print("[", end="")
        for i in range(1, self.size+1):
            print(str(self.heap[i]) +", ", end="") 
        print("]")

def main():
    maxHeap = MaxHeap(10)
    maxHeap.addNode(0)
    maxHeap.addNode(6)
    maxHeap.addNode(2)
    maxHeap.addNode(6)
    maxHeap.addNode(2)
    maxHeap.addNode(8)
    maxHeap.addNode(9)
                

    maxHeap.printHeap()


if __name__ == "__main__":
    main()



       
            

        
