class Node:
    def __init__(self, val):
        self.val = val
        self.edges = []
        self.parentNode = None
        self.childrenNodes = []

    def insertNode(self, new_node):
        self.childrenNodes.append(new_node)
        self.edges.append(Edge(self, new_node))

    def print_val(self, pad_idx=1):
        pad = (pad_idx-1) * "\t"
        print(pad, self.val)
        for childrenNode in self.childrenNodes:
            childrenNode.print_val(pad_idx+1)


class Edge:
    def __init__(self, firstNode, secondNode):
        self.firstNode = firstNode
        self.secondNode = secondNode


class Tree:
    def __init__(self, root=None):
        self.root = root

    def add_root_node(self, new_node):
        self.root = new_node

    def add_node(self, base_node, new_node):
        if not self.root:
            print("Add root node first!")
            return
        base_node.insertNode(new_node)

    def print(self):
        self.root.print_val()


root_node = Node(0)
tree = Tree(root_node)

tree.add_node(root_node, Node("a1"))
tree.add_node(root_node, Node("a2"))
tree.add_node(root_node, Node("a3"))

tree.add_node(root_node.childrenNodes[0], Node("b1"))
tree.add_node(root_node.childrenNodes[0].childrenNodes[0], Node("c1"))

tree.print()
