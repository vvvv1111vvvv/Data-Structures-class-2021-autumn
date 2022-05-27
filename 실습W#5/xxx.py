class newNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

 
def getLevelUtil(node, data, level):
    if (node == None):
        return 0
 
    if (node.data == data):
        return level
 
    downlevel = getLevelUtil(node.left,
                             data, level + 1)
    if (downlevel != 0):
        return downlevel
 
    downlevel = getLevelUtil(node.right,
                             data, level + 1)
    return downlevel

 
 
def getLevel(node, data):
 
    return getLevelUtil(node, data, 1)

if __name__ == '__main__':
    root = newNode(3)
    root.left = newNode(2)
    root.right = newNode(5)
    root.left.left = newNode(1)
    root.left.right = newNode(4)
    for x in range(1, 6):
        level = getLevel(root, x)
        if (level):
            print("Level of", x,
                  "is", getLevel(root, x))
        else:
            print(x, "is not present in tree")
