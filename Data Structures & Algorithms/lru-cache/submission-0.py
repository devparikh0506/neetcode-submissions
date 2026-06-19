class ListNode:
    def __init__ (self, val, key, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.head = ListNode(0, key="head")
        self.tail = ListNode(0, key="tail")
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        value = self.cache.get(key).val
        self._touch(key)
        return value    

    def _remove(self, key):
        if key not in self.cache:
            return None
        val_node = self.cache.pop(key)
        val_node.next.prev = val_node.prev 
        val_node.prev.next = val_node.next
        self.size -= 1
        return val_node.val


    def _add(self, key, val):
        new_node = ListNode(val, key=key)
        new_node.prev = self.head
        new_node.next = self.head.next
        self.head.next = new_node
        new_node.next.prev = new_node
        self.cache[key] = new_node
        self.size += 1

    def _touch(self, key):
        val = self._remove(key)
        if val is not None:
            self._add(key, val)

    def _trim(self):
        last_node= self.tail.prev
        if last_node != self.head:
            self._remove(last_node.key)
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(key)
        self._add(key, value)
        if self.size > self.capacity:
            self._trim()
