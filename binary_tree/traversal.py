
class checkNode:
   def __init__(self, node, toProcess):
       self.node = node
       self.toProcess = toProcess

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def postorderTraversal(root: Node):
    
    postOrder = []

    stack = [checkNode(root, False)]

    while stack:
        #Get the current node
        currCheckNode = stack.pop()
        node:Node = currCheckNode.node
        toProcess = currCheckNode.toProcess
        #Check whether the current node is to be processed 

        if toProcess:
            postOrder.append(node)
        else:
            #When we don't process the node we need to get the data from both the left and right children of 
            #Our node

            #Since we are using a stack we will first push our actual node, labeled true so that we process it when we get around to it
            #Pushing it first means that it will be processed last, which is what we want 
            stack.append(checkNode(node, True))
            if node.left:
                stack.append(checkNode(node.left, False))

            if node.right:
                stack.append(checkNode(node.right, False))




# def main():





# if __name__ == "__main__":
#     main()