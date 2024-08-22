#Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
from custom_linked_list import LinkedList, Node

def remove_nth_node(nums: LinkedList, n):
    #the ideal solution is just to preprocess and get the size of the list 

    size = nums.getSizeList()
    count = 0 
    current: Node = nums.head
    while (size - 2) - count >= n: 
        current = current.next
        count += 1 
    # [2,4,7] 3 len
    # n = 1 elem = 4
    #0, 1
    print(current.value)


def main():
    testList = LinkedList()
    testList.buildList()
    remove_nth_node(testList,4)
    testList.printList()


if __name__ == "__main__":
    main()