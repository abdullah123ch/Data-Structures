class Vertex:
    def __init__(self, k=0, l=None, r=None, v=None, c=None):
        self.key = k           # Key for sorting
        self.left = l          # Left child (smaller keys)
        self.right = r         # Right child (larger keys)
        self.value = v         # Associated value
        self.color = c

class RBTree:
    def __init__(self):
        self.root = None

    def isRed(self, node):
        return node is not None and node.color == 'r'

    def rotateLeft(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = 'r'
        return x

    def rotateRight(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = 'r'
        return x

    def colorFlip(self, h):
        h.color = 'r' if h.color == 'b' else 'b'
        h.left.color = 'b' if h.left.color == 'r' else 'r'
        h.right.color = 'b' if h.right.color == 'r' else 'r'

    def insert(self, key):
        self.root = self._insertRecursive(self.root, key)
        self.root.color = 'b'  # root must always be black

    def _insertRecursive(self, ver, k):
        if ver is None:
            # Rule 1: New node is red
            return Vertex(k=k, c='r')

        if k < ver.key:
            ver.left = self._insertRecursive(ver.left, k)
        elif k > ver.key:
            ver.right = self._insertRecursive(ver.right, k)

        # Rule 2: Right red link => rotate left
        if self.isRed(ver.right) and not self.isRed(ver.left):
            ver = self.rotateLeft(ver)

        # Rule 3: Two left red links => rotate right
        if self.isRed(ver.left) and self.isRed(ver.left.left):
            ver = self.rotateRight(ver)

        # Rule 4: Both children red => color flip
        if self.isRed(ver.left) and self.isRed(ver.right):
            self.colorFlip(ver)

        return ver

    def find(self, key):
        return self._findRecursive(self.root, key)

    def _findRecursive(self, node, key):
        if node is None:
            return None  # Not found
        if key == node.key:
            return node
        elif key < node.key:
            return self._findRecursive(node.left, key)
        else:
            return self._findRecursive(node.right, key)