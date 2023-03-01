# Binary search tree:
# { 1- in the left subtree the value of a node is less than or equal to parent's node value.
#   2- in the right subtree the value of the node is greater than the parent's node value.}

# why binary search tree ?
# { it's faster than binary tree for inserting and deleting an element.}

from queue_using_linkedlist import Queue


class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertion(rootNode, nodeValue):
    if rootNode.data is None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BinarySearchTree(nodeValue)
        else:
            insertion(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BinarySearchTree(nodeValue)
        else:
            insertion(rootNode.rightChild, nodeValue)
    return "Success"

#{Time : O(logN)
# Space : O(logN) }


newBST = BinarySearchTree(None)
insertion(newBST, 70)
insertion(newBST, 50)
insertion(newBST, 90)
insertion(newBST, 30)
insertion(newBST, 60)
insertion(newBST, 80)
insertion(newBST, 10)
insertion(newBST, 100)
insertion(newBST, 20)
insertion(newBST, 40)
# print(newBST.data)
# print(newBST.leftChild.data)
# print(newBST.rightChild.data)

#_____________________________________________________


def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrder(rootNode.leftChild)
    preOrder(rootNode.rightChild)


# preOrder(newBST)

# {Time : O(n)
# Space: O(n)}

#______________________________________________________


def inOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.leftChild)
    print(rootNode.data)
    inOrder(rootNode.rightChild)


# inOrder(newBST)

# {Time: O(n)
# Space: O(n)}

#_______________________________________________________


def postOrder(rootNode):
    if not rootNode:
        return
    postOrder(rootNode.leftChild)
    postOrder(rootNode.rightChild)
    print(rootNode.data)


# postOrder(newBST)

# {Time: O(n)
# Space: O(n)}
#_________________________________________________________


def levelOrder(rootNode):
    if not rootNode:
        return
    else:
        customQ = Queue()
        customQ.enQueue(rootNode)
        while not customQ.isEmpty():
            root = customQ.deQueue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQ.enQueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQ.enQueue(root.value.rightChild)


# levelOrder(newBST)

#{Time: O(n)
# Space: O(n) }

#_______________________________________________________


def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("found")
        else:
            searchNode(rootNode.rightChild, nodeValue)
    return "not found"


searchNode(newBST, 40)
# searchNode(newBST, 60)

#{Time: O(log N)
# Space: O(log N)}
#_______________________________________________________


def minValue(BST):
    current = BST
    while current.leftChild is not None:
        current = current.leftChild
    return current


def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode

    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)

    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp

        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        temp = minValue(rootNode.rightChild)
        rootNode = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode


#{ Time: O(log N)
# Space: O(log N) }
# ________________________________________________________________________


def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return " finished."

#{Time: O(1)
# Space: O(1)}
#_________________________________________________________________________
