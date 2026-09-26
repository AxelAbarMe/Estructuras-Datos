# Búsqueda de elemento en árbol binario

## Iterativa

```python

    def iterative_search(self, key):
        return self._iterative_search(key)

    def _iterative_search(self, k):
        if self.root is None:
            return None
        cola = collections.deque()
        cola.append(self.root)

        while cola:
            tmp = cola.popleft()
            if tmp.key == key:
                return tmp
            if tmp.left is not None:
                cola.append(tmp.left)
            if tmp.right is not None:
                cola.append(tmp.right)
        return None
```

## Recursiva

```python
    def recursive_search(self, key):
        return self._recursive_search(self.root, key)
    
    def _recursive_search(self, current_node, key):
        if current_node is None:
            return None
        if current_node.key == key:
            return current_node
        if current_node.left is not None:
            tmp = self._recursive_search(current_node.left, key)
            if tmp is not None:
                return tmp    
        if current_node.right is not None:
            tmp = self._recursive_search(current_node.right, key)
            if tmp is not None:
                return tmp
        return None
```

## Recursiva (Con OR)

```python
    def recursive_search(self, key):
        return self._recursive_search(self.root, key)

    def _recursive_search(self, node, key):
      if node is None or node.key == key:
          return node
      izq = self._recursive_search(node.left, key)
      return izq if izq is not None else self._recursive_search(node.right, key)
```
