from custom_linked_list import LinkedList, Node

#Check if there is a cycle in the linked list where the tail of the list links to another node in the list instead of null

def check_cycle(linkList: LinkedList):
    nodeSet = set()
    current = linkList.head
    while current:
        setLength = len(nodeSet)        
        nodeSet.add(current)
        if len(nodeSet) == setLength:
            return True 
        current = current.next 
        

    return False

#Return the node where the cycle starts 
def check_cycle_2(head:Node):
    #Make a hashmap that stores all of the nodes and their positions 
    #Then simply loop through until you get that node and then you already have its position because you stored it so return the position
    node_positions = {}
    current = head
    pos = 0 
    while current:
        potentialPos = node_positions.get(current)
        if potentialPos:
            return potentialPos
        else: 
            node_positions[current] = pos
        pos += 1
        current = current.next



def main():
    newList = LinkedList()
    newList.head = Node(1)
    newList.head.next = Node(2)

    oneNode = newList.head
    twoNode = oneNode.next
    twoNode.next = oneNode
    print(check_cycle_2(newList.head))


if __name__ == "__main__":
    main()