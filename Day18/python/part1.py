from ast import literal_eval as l_eval
from collections import deque
from math import ceil, floor

data = open('../data/firstExample').readlines()
data = [l_eval(d.strip()) for d in data]

class Node:
    def __init__(self, data = None): self.left = None; self.right = None; self.data = data

    def add_data(self, data): self.data = data

    def add_left_child(self, obj): self.left = obj
    
    def add_right_child(self, obj): self.right = obj

    def PrintTree(self):
        if self.left: self.left.PrintTree()
        print(self.data)
        if self.right: self.right.PrintTree()

rootNode = Node(None)
leafNodes = []

def populateTree(node, data):
    if type(data[0]) == int: leftChild = Node(data[0])
    else: leftChild = Node(); populateTree(leftChild, data[0])
    if type(data[1]) == int: rightChild = Node(data[1])
    else: rightChild = Node(); populateTree(rightChild, data[1])
    node.add_left_child(leftChild); node.add_right_child(rightChild)

def findDepthUnmatch(root, curr):
    if root == None: return -1
    dist = -1
    if root == curr: return dist + 1
    dist = findDepthUnmatch(root.left, curr)
    if dist >= 0: return dist + 1
    dist = findDepthUnmatch(root.right, curr)
    if dist >= 0: return dist + 1
    return dist

def findDepth(root, curr): return findDepthUnmatch(root, curr) - 1

def findParent(root, curr):
    if root == None: return
    elif root.left == curr or root.right == curr: return root
    else:
        left = findParent(root.left, curr); right = findParent(root.right, curr)
        if left != None: return left
        else: return right

def deepestLeftMostNode(root):
    if root is None: return None
    q = deque([root])
    while q:
        lst = []
        for _ in range(len(q)):
            lst.append(q.popleft())
            if lst[-1].left: q.append(lst[-1].left)
            if lst[-1].right: q.append(lst[-1].right)
    return lst[0]

def getLeafNodesLTR(root):
    if not root.left and not root.right: leafNodes.append(root)
    if root.left: getLeafNodesLTR(root.left)
    if root.right: getLeafNodesLTR(root.right)

def getMaxDepth(node):
    if node.left == None and node.right == None: return -1
    else:
        lDepth = getMaxDepth(node.left); rDepth = getMaxDepth(node.right)
        if lDepth > rDepth: return lDepth + 1
        else: return rDepth + 1

def addition(pair): return

def explodePair(pair):
    idxL = leafNodes.index(pair.left); idxR = leafNodes.index(pair.right)
    l = pair.left.data; r = pair.right.data
    if idxL != 0:
        nextLeft = leafNodes[idxL-1]
        nextLeft.data += l
    if idxR != len(leafNodes)-1:
        nextRight = leafNodes[idxR+1]
        nextRight.data += r
    pair.left = None; pair.right = None; pair.data = 0

def splitPair(node):
    if node.data > 9: 
        d = node.data
        l = floor(d/2); r = ceil(d/2)
        leftNode = Node(l); rightNode = Node(r)
        node.left = leftNode; node.right = rightNode