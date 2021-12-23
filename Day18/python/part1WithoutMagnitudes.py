from ast import literal_eval as l_eval
from collections import deque
from math import ceil, floor

data = open('../data/input').readlines()
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

#Given a rootnode and data populate a tree
def populateTree(node, data):
    if type(data[0]) == int: leftChild = Node(data[0])
    else: leftChild = Node(); populateTree(leftChild, data[0])
    if type(data[1]) == int: rightChild = Node(data[1])
    else: rightChild = Node(); populateTree(rightChild, data[1])
    node.add_left_child(leftChild); node.add_right_child(rightChild)
#This basically gives one more than we want (because the numbers are 
#seperate nodes) so the one below just corrects for that
def findDepthUnmatch(root, curr):
    if root == None: return -1
    dist = -1
    if root == curr: return dist + 1
    dist = findDepthUnmatch(root.left, curr)
    if dist >= 0: return dist + 1
    dist = findDepthUnmatch(root.right, curr)
    if dist >= 0: return dist + 1
    return dist
#Find the depth of some node in certain tree
def findDepth(root, curr): return findDepthUnmatch(root, curr) - 1
#Find the parent of the some node
def findParent(root, curr):
    if root == None: return
    elif root.left == curr or root.right == curr: return root
    else:
        left = findParent(root.left, curr); right = findParent(root.right, curr)
        if left != None: return left
        else: return right
#Get the node with the most depth, the leftmost if tied
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
#Find all the leaf nodes of a tree from left to right
def getLeafNodesLTR(root, leafNodes = None):
    if leafNodes == None: leafNodes = []
    if root.left == None and root.right == None: leafNodes.append(root)
    else:
        if root.left != None: getLeafNodesLTR(root.left, leafNodes)
        if root.right != None: getLeafNodesLTR(root.right, leafNodes)
    return leafNodes

#Find the max depth of a certain tree
def getMaxDepth(node):
    if node.left == None and node.right == None: return -1
    else:
        lDepth = getMaxDepth(node.left); rDepth = getMaxDepth(node.right)
        if lDepth > rDepth: return lDepth + 1
        else: return rDepth + 1
#Add a pair to the current pair
def addition(rootNodes):
    pair1 = rootNodes.popleft(); pair2 = rootNodes.popleft()
    pair = Node(); pair.left = pair1; pair.right = pair2
    rootNodes.appendleft(pair)
    return rootNodes
#Explode a pair that is nested 4 times
def explodePair(pair, currRoot):
    leafNodes = getLeafNodesLTR(currRoot)
    idxL = leafNodes.index(pair.left); idxR = leafNodes.index(pair.right)
    l = pair.left.data; r = pair.right.data
    if idxL != 0:
        nextLeft = leafNodes[idxL-1]
        nextLeft.data += l
    if idxR != len(leafNodes)-1:
        nextRight = leafNodes[idxR+1]
        nextRight.data += r
    pair.left = None; pair.right = None; pair.data = 0
#Split a value that is 10 or above into two values with ceil and floor
def split(node):
    if node.data > 9: 
        d = node.data
        l = floor(d/2); r = ceil(d/2)
        leftNode = Node(l); rightNode = Node(r)
        node.left = leftNode; node.right = rightNode
#Populate trees that correspond to lines in data
#return a list of the root nodes
def populateAllTrees(data):
    rootNodes = deque()
    for line in data:
        currRoot = Node()
        rootNodes.append(currRoot)
        populateTree(currRoot, line)
    return rootNodes
#Calculate the magnitude of the final tree recursively
#def calculateMagnitude(finalRootNode):

#Solve part1 by adding them together line by line and then checking if
#I need to explode or split
def solvePart1(data):
    rootNodes = populateAllTrees(data)
    while len(rootNodes) > 1:
        rootNodes = addition(rootNodes)
        while True:
            if getMaxDepth(rootNodes[0]) >= 4:
                leaf = deepestLeftMostNode(rootNodes[0])
                explNode = findParent(rootNodes[0],leaf)
                leafNodes = getLeafNodesLTR(rootNodes[0])
                explodePair(explNode, rootNodes[0])
                continue
            leafNodes = getLeafNodesLTR(rootNodes[0])
            if max(leafNode.data for leafNode in leafNodes) > 9:
                values = [leafNode.data for leafNode in leafNodes]
                idx = next(i for i, value in enumerate(values) if value > 9)
                split(leafNodes[idx])
                continue
            break
    return rootNodes

finalRootNode = solvePart1(data)

print(len(finalRootNode))