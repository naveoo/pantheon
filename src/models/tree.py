class Node:
    def __init__(self, name: str, price: int, feedback: bool = False):
        """A node to use in the class Tree.

        Args:
            name (str): The name of the node.
            price (int): The price of the node.
            feedback (bool, optional): Send returns in the console. Defaults to False.
        """
        self.name = name
        self.price = price
        self.children = []
        self.feedback = feedback

    def __str__(self) -> str:
        return f"{self.name} : {self.price}"

    def add_child(self, child_node: 'Node') -> None:
        """Add a child to the node.

        Args:
            child_node (Node): The child to add.

        Raises:
            ValueError: The node is already a child.
            TypeError: The argument provided is not an instance of Node.
        """
        if not isinstance(child_node, Node):
            raise TypeError("child_node must be an instance of Node")
        if child_node in self.children:
            raise ValueError("The node is already a child.")
        else:
            self.children.append(child_node)
        if self.feedback:
            print(f"Child {child_node.name} successfully added to the node {self.name}.")

    def remove_child(self, child_node: 'Node') -> None:
        """Remove a child from the node.

        Args:
            child_node (Node): The child to remove.

        Raises:
            ValueError: If the node does not have this child.
            TypeError: The argument provided is not an instance of Node.
        """
        if not isinstance(child_node, Node):
            raise TypeError("child_node must be an instance of Node")
        if child_node not in self.children:
            raise ValueError("The node doesn't have this child.")
        else:
            self.children = [child for child in self.children if child != child_node]
        if self.feedback:
            print(f"Child {child_node.name} successfully removed from the node {self.name}.")

    def has_child(self, child_node: 'Node') -> bool:
        """Check if a node is a direct child.

        Args:
            child_node (Node): The child to check.

        Returns:
            bool: True if the child_node is a direct child, False otherwise.
        """
        return child_node in self.children

class Tree:
    def __init__(self, root: Node):
        """A tree usable with the class Node.

        Args:
            root (Node): The root node of the tree.
        """
        self.root = root

    def _find_node(self, current_node: Node, target_node: Node) -> bool:
        """Recursively search for a node in the tree.

        Args:
            current_node (Node): The current node being searched.
            target_node (Node): The target node to find.

        Returns:
            bool: True if the target node is found, False otherwise.
        """
        if current_node == target_node:
            return True
        for child in current_node.children:
            if self._find_node(child, target_node):
                return True
        return False

    def add_node(self, parent: Node, child: Node) -> None:
        """Add a node in the tree.

        Args:
            parent (Node): The parent node.
            child (Node): The node to add.

        Raises:
            ValueError: If the parent node is not found in the tree.
        """
        if not self._find_node(self.root, parent):
            raise ValueError("The parent node is not in the tree.")
        parent.add_child(child)

    def display_tree(self) -> None:
        """Display the entire tree structure."""
        if self.root:
            self.root.display()
        else:
            print("The tree is empty.")