import random


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


class TreeGenerator:
    def __init__(self, total_nodes: int, leaf_nodes: int):
        if total_nodes - 1 < leaf_nodes:
            raise ValueError("Total nodes should be greater than leaf nodes")

        self.nodes_to_create = total_nodes
        self.branches_to_create = leaf_nodes

    def create_node_children(self, node: TreeNode):
        child_num = random.randint(1, self.branches_to_create) if self.nodes_to_create > self.branches_to_create\
            else self.branches_to_create

        for child_idx in range(child_num):
            if not self.nodes_to_create:
                break

            if child_idx >= 1:
                self.branches_to_create -= 1

            child_node = TreeNode(self.nodes_to_create)
            print(f'Creating element {child_node.value} under {node.value}')
            node.children.append(child_node)
            self.nodes_to_create -= 1

    def add_tree_layer(self, parents: list[TreeNode]):
        new_layer_elems = []
        for parent in parents:
            self.create_node_children(parent)
            new_layer_elems.extend(parent.children)

        return new_layer_elems

    def create_tree(self):
        root = TreeNode(self.nodes_to_create)
        self.nodes_to_create -= 1
        layer = [root]
        while self.nodes_to_create:
            layer = self.add_tree_layer(layer)

        return root
