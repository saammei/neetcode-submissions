
class DoubleListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}  # key -> DoubleListNode
        # Sentinel nodes
        self.head = DoubleListNode() # MRU side
        self.tail = DoubleListNode() # LRU side
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: "DoubleListNode"):
        """Removes a node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node: "DoubleListNode"):
        """Adds a node to the front of the linked list (right after head)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        node = self.map[key]
        # Move the accessed node to the front
        self._remove(node)
        self._add_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        # If key exists, update value and move to front
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._remove(node)
            self._add_to_front(node)
            return

        # If at capacity, evict the least recently used item
        if len(self.map) >= self.capacity:
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.map[lru_node.key]

        # Add the new node to the front
        new_node = DoubleListNode(key, value)
        self.map[key] = new_node
        self._add_to_front(new_node)
