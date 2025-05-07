class Vertex:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BSTmap:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key, value):
        self.root = self.insert_recursive(self.root, key, value)
        self.size += 1
    
    def insert_recursive(self, node, key, value):
        if node is None:
            return Vertex(key, value)
    
        if key < node.key:
            node.left = self.insert_recursive(node.left, key, value)
        elif key > node.key:
            node.right = self.insert_recursive(node.right, key, value)
    
        return node
    
    def find(self, key):
        return self._find_recursive(self.root, key)

    def _find_recursive(self, node, key):
        if node is None:
            return False

        if key == node.key:
            return True
        elif key < node.key:
            return self._find_recursive(node.left, key)
        else:
            return self._find_recursive(node.right, key)
  
def display_aux(self):
      """Returns list of strings, width, height, and horizontal coordinate of the root."""
      # No child.
      if self.right is None and self.left is None:
          line = '< ' + str(self.key) + ' , ' + str(self.value) + ' >'
          width = len(line)
          height = 1
          middle = width // 2
          return [line], width, height, middle

      # Only left child.
      if self.right is None:
          lines, n, p, x = display_aux(self.left)
          #s = '%s' % self.key
          s = '< ' + str(self.key) + ' , ' + str(self.value) + ' >'
          u = len(s)
          first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
          second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
          shifted_lines = [line + u * ' ' for line in lines]
          return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

      # Only right child.
      if self.left is None:
          lines, n, p, x = display_aux(self.right)
          #s = '%s' % self.key
          s = '< ' + str(self.key) + ' , ' + str(self.value) + ' >'
          u = len(s)
          first_line = s + x * '_' + (n - x) * ' '
          second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
          shifted_lines = [u * ' ' + line for line in lines]
          return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

      # Two children.
      left, n, p, x = display_aux(self.left)
      right, m, q, y = display_aux(self.right)
      #s = '%s' % self.key
      s = '< ' + str(self.key) + ' , ' + str(self.value) + ' >'
      u = len(s)
      first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
      second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
      if p < q:
          left += [n * ' '] * (q - p)
      elif q < p:
          right += [m * ' '] * (p - q)
      zipped_lines = zip(left, right)
      lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
      return lines, n + m + u, max(p, q) + 2, n + u // 2

def display(self):
      lines, *_ = display_aux(self)
      for line in lines:
          print(line)
      print()

