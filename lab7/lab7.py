# DSA456V1A
# Lab 7
# Student: Chungon Tse
# ID: 154928188
# Date: 19 Apr 2023
# BST and AVL

from random import sample
from typing import List
import matplotlib.pyplot as plt


class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data: int):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data: int, node: Node):
        if data < node.data:
            if node.left:
                self._insert(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self._insert(data, node.right)
            else:
                node.right = Node(data)

    def height(self, node: Node) -> int:
        if not node:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1

    def imbalance(self, node: Node) -> int:
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return abs(left_height - right_height)

    def inorder(self, node: Node) -> List[int]:
        if not node:
            return []
        return self.inorder(node.left) + [node.data] + self.inorder(node.right)


def generate_permutation(n: int) -> List[int]:
    return sample(range(1, n + 1), n)


def build_bst(data: List[int]) -> BinarySearchTree:
    bst = BinarySearchTree()
    for d in data:
        bst.insert(d)
    return bst


def plot_histogram(data: List[int], title: str):
    plt.hist(data, bins='auto')
    plt.title(title)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None
        self.rotations = 0

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if not node:
            return Node(data)
        elif data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
        node.height = 1 + max(self._height(node.left),
                              self._height(node.right))
        balance = self._get_balance(node)
        if balance > 1 and data < node.left.data:
            self.rotations += 1
            return self._rotate_right(node)
        if balance < -1 and data > node.right.data:
            self.rotations += 1
            return self._rotate_left(node)
        if balance > 1 and data > node.left.data:
            node.left = self._rotate_left(node.left)
            self.rotations += 2
            return self._rotate_right(node)
        if balance < -1 and data < node.right.data:
            node.right = self._rotate_right(node.right)
            self.rotations += 2
            return self._rotate_left(node)
        return node

    def _get_balance(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))
        return new_root

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))
        return new_root


bsts = []
avls = []
data = []
for i in range(1000):
    data = generate_permutation(20)
    bst = build_bst(data)
    avl = AVLTree()
    for d in data:
        avl.insert(d)
    bsts.append(bst)
    avls.append(avl)

b_heights = []
b_imbalances = []
a_heights = []
a_imbalances = []
rotations_needed = []
for bst, avl in zip(bsts, avls):
    b_height = bst.height(bst.root)
    b_imbalance = bst.imbalance(bst.root)
    b_heights.append(b_height)
    b_imbalances.append(b_imbalance)

    a_height = avl.root.height
    a_imbalance = avl._get_balance(avl.root)
    a_heights.append(a_height)
    a_imbalances.append(a_imbalance)

    for d in data:
        avl.insert(d)
    rotations_needed.append(avl.rotations)

plot_histogram(b_heights, "BST Height Histogram")
plot_histogram(b_imbalances, "BST Imbalance Histogram")
plot_histogram(a_heights, "AVL Height Histogram")
plot_histogram(a_imbalances, "AVL Imbalance Histogram")
plot_histogram(rotations_needed, "AVL Rotations Histogram")
