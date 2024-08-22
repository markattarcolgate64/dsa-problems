#Given the head of a singly linked list, reverse the list, and return the reversed list.

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Input: head = [1,2]
# Output: [2,1]

# Input: head = []
# Output: []
from custom_linked_list import LinkedList, Node

    #Need to reverse the list itself


def reverseList(linkList: LinkedList):
    
    #Add the nodes to a new list backwards
    current: Node = linkList.head 
    reverseList = LinkedList()
    reverseList.head = Node(current.value)
    
    

    while current.next != None:
        current = current.next
        #Make a new node out of current
        reverseNode = Node(current.value)
        #Attach that pointing to our reverse head, adding in like a moonwalk fashion
        reverseNode.next = reverseList.head  
        #Move reverseHead to the new node that was added to the front of the list 
        reverseList.head = reverseNode 


    return reverseList
        #5,4 
        #4,5

#Time: O(n) 
#Space: O(n)

def reverseListEfficient(linkList: LinkedList): 
    #Super efficient reverse linklist
    #Time: O(n), Space: O(1)
    if linkList == None:
        return None 

    current: Node = linkList.head 
    prevNode = None 

    while current.next != None:
        #Get the next node if it exists
        nextNode = current.next
        #Turn back the current node to previous
        current.next = prevNode
        #Reassign the prevNode to the current one
        prevNode = current
        #Move the list up by one 
        current = nextNode 

    current.next = prevNode

    return current 


# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

# Example 1:

#[1,2,3,4,5,6,29] left = 2, right = 5
#[1,5,4,3,2,6,29]

# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]

#So lets store the left neighbor and the left node
#Then lets store the right node and neighbor when we get to the end of right 
#None if there are no neighbors
#Then within the process of the while loop we can reverse the list as normal 
#At the end we connect the left node to the right neighbor and vice-versa
def reverse_list_2(head:Node, left, right):
    if head.next == None:
        return head 
    
    count = 1
    current = head
    leftNeighbor = None
    #
    prevNode = None 
    while count < right:
        if count == left - 1:
            #Store the left neighbor to be attached later
            leftNeighbor = current
        #Now we start the reversal process 
        elif count >= left:
            if count == left:
                leftNode = current
            #Get the next node 
            nextNode = current.next 
            #Turn the current node around
            current.next = prevNode 
            #Reassign the previous node which stores the reversed chain 
            prevNode = current 
            #Move up the nodes to the next one 
            current = nextNode
            count += 1 

            continue
           
           
        current = current.next 
        count += 1 

    if current.next:
        rightNeighbor = current.next
    else:   
        rightNeighbor = None
    #Should equal right node we should test this 
    rightNode = current
    rightNode.next = prevNode
    print(rightNode.value) 
    #Now we get right neighbor if it exists otherwise Null
   
    #Attach the left and right neighbors
    leftNode.next = rightNeighbor 
    leftNeighbor.next = rightNode 

    return head 
    
    


def main():
    linkedList = LinkedList()
    
    linkedList.buildList()

    #reverse = reverseListEfficient(linkedList)
    reverse = reverse_list_2(linkedList.head,2,4)
    while reverse:
        print(reverse.value)
        reverse = reverse.next
    

if __name__ == "__main__":
    main()
