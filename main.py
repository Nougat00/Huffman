inputFile = "input.txt"
outputFile = "output.txt"

class Tree:
    def __init__(self, amount, letter, leftChild=None, rightChild=None):
        self.amount = amount
        self.letter = letter
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.code = ''

def printTree(leaf, value=''):
    f = open("output.txt", 'a')
    newCode = value + str(leaf.code)

    if leaf.leftChild:
        printTree(leaf.leftChild, newCode)
    if leaf.rightChild:
        printTree(leaf.rightChild, newCode)
    if not leaf.leftChild and not leaf.rightChild:
        f.writelines(leaf.letter + " -> " + newCode + "\n")

def buildTree(file):
    occurs = amount(file)
    leaves = []

    for k, v in occurs.items():
        leaves.append(Tree(v, k))

    while len(leaves) > 1:
        HeapSort(leaves)

        left = leaves[len(leaves) - 1]
        HeapSort(leaves)
        right = leaves[len(leaves) - 2]

        left.code = 0
        right.code = 1

        newLeaf = Tree(left.amount + right.amount, left.letter + right.letter, left, right)

        leaves.remove(left)
        leaves.remove(right)
        leaves.append(newLeaf)
    return leaves


def heapify(tab, i, size):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i

    if l < size and tab[l].amount > tab[largest].amount:
        largest = l
    if r < size and tab[r].amount > tab[largest].amount:
        largest = r

    if largest != i:
        tab[i], tab[largest] = tab[largest], tab[i]
        heapify(tab, largest, size)


def HeapSort(tab):
    size = len(tab)

    for i in range(size // 2 - 1, -1, -1):
        heapify(tab, i, size)

    for i in range(size - 1, 0, -1):
        tab[i], tab[0] = tab[0], tab[i]
        heapify(tab, 0, i)

def amount(file):
    txt = open(file, 'r').read()
    dict = {}
    for char in txt:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict


def encrypt(leaf, str, txt):
    if leaf is None:
        return txt
    if leaf:
        if len(leaf.letter) <= 1:
            txt = txt.replace(leaf.letter, str)
    txt = encrypt(leaf.leftChild, str + "0", txt)
    txt = encrypt(leaf.rightChild, str + "1", txt)
    return txt


def saveToFile(tree, destination):
    f = open(destination, 'w')
    f.writelines("Word: " + open("input.txt", 'r').read() + "\n")
    f.writelines("Code: " + encrypt(tree[0], "", open("input.txt", 'r').read()) + "\n")
    f.writelines("\nChar | Huffman code \n")
    f.close()
    printTree(tree[0])

tree = buildTree(inputFile)
saveToFile(tree, outputFile)