class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.children = [child for child in self.children
                         if child is not child_node]

    def traverse(self):
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            yield current_node.value
            nodes_to_visit += current_node.children

    def get_min(self):
        min_val = self.value
        for node_val in self.traverse():
            if node_val < min_val:
                min_val = node_val
        return min_val


root = TreeNode(5)
a1 = TreeNode(2)
a2 = TreeNode(-2)
root.add_child(a1)
root.add_child(a2)

b1 = TreeNode(-3)
a1.add_child(b1)

print(root.get_min())
