# Author: El Tigre
# Description: Binary tree basic functions (traversals, insertion, deletion, etc.)

import queue


class Node:
    """Represents a single node in a binary tree."""

    def __init__(self, val=None):
        """
        Initialize a node with a value, and optional left and right children.

        Args:
            val: Value to store in the node.
        """
        self.key = val
        self.left = None
        self.right = None


class BinaryTree:
    """A binary tree with basic operations such as traversals and height calculation."""

    def __init__(self):
        """Initialize an empty binary tree."""
        self.root = None

    def create_from_file(self, filename):
        """
        Create a binary tree from a serialized file representation.

        The file must contain characters where `$` represents a null node.

        Args:
            filename (str): Path to the file containing the tree serialization.

        Returns:
            int | None: 1 if tree was created successfully, None otherwise.
        """
        try:
            handle = open(filename, "r")
        except IOError:
            return None

        self.root = self._create_from_file(handle)
        handle.close()

        if self.root is None:
            return None
        return 1

    def is_empty(self):
        """Check if the binary tree is empty."""
        return self.root is None

    def height(self):
        """Calculate the height of the binary tree."""
        return self._height(self.root)

    def delete_tree(self):
        """Delete the entire tree by removing its root reference."""
        self.root = None

    def pre_order(self):
        """Perform a pre-order traversal (root-left-right)."""
        return self._pre_order(self.root)

    def in_order(self):
        """Perform an in-order traversal (left-root-right)."""
        return self._in_order(self.root)

    def pos_order(self):
        """Perform a post-order traversal (left-right-root)."""
        return self._pos_order(self.root)

    def bfs_traversal(self):
        """Perform a breadth-first (level-order) traversal."""
        return self._bfs_traversal()

    def print_tree(self):
        """Print the tree structure in a readable format."""
        self._print_tree(" ", self.root, False)

    # --- Internal helpers ---

    def _create_from_file(self, handle):
        c = handle.read(1)
        if c == '$':
            return None

        tmp = Node(c)
        tmp.left = self._create_from_file(handle)
        tmp.right = self._create_from_file(handle)
        return tmp

    def _height(self, r):
        if r is None:
            return -1
        max_left = self._height(r.left) + 1
        max_right = self._height(r.right) + 1
        return max(max_left, max_right)

    def _pre_order(self, r):
        if r is None:
            return []
        return [r.key] + self._pre_order(r.left) + self._pre_order(r.right)

    def _in_order(self, r):
        if r is None:
            return []
        return self._in_order(r.left) + [r.key] + self._in_order(r.right)

    def _pos_order(self, r):
        if r is None:
            return []
        return self._pos_order(r.left) + self._pos_order(r.right) + [r.key]

    def _bfs_traversal(self):
        if self.root is None:
            return []

        result = []
        cola = queue.Queue()
        cola.put(self.root)

        while not cola.empty():
            tmp = cola.get()
            result.append(tmp.key)
            if tmp.left is not None:
                cola.put(tmp.left)
            if tmp.right is not None:
                cola.put(tmp.right)

        return result

    def _print_tree(self, p, r, is_left):
        if r:
            print(p, end='')
            if is_left:
                print("|--", end='')
                s = "|    "
            else:
                print("'--", end='')
                s = "    "
            print(r.key)
            self._print_tree(p + s, r.left, True)
            self._print_tree(p + s, r.right, False)
