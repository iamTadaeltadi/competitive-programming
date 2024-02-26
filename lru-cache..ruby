class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.hash_map = {}
        self.capacity = capacity

    def prepend(self, new_node: Node):
        if self.head: 
            self.head.prev = new_node
            new_node.next = self.head
        
        if not self.tail:
            self.tail = new_node
            
        self.head = new_node

    def unlink_node(self, node: Node) -> None:
        # Unlink the node from cache
        if not node: return None
        
        prev_node = node.prev
        next_node = node.next

        if prev_node: prev_node.next = next_node
        if next_node: next_node.prev = prev_node

        if self.head == node:
            self.head = next_node
        
        if self.tail == node:
            self.tail = prev_node
        
        node.prev = None
        node.next = None

    def delete_node(self, node: Node):
        self.unlink_node(node)
        del self.hash_map[node.key]
        del node

    def evict_lru_node(self) -> Node or None:
        if not self.tail: return None

        lru_node = self.tail
        self.delete_node(lru_node)
    
    def get(self, key: int) -> int:
        if key not in self.hash_map: return -1
        node = self.hash_map[key]

        if self.head != node:
            self.unlink_node(node)
            self.prepend(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        new_node = Node(key, value)
        if key in self.hash_map:
            self.delete_node(self.hash_map[key])
        
        if len(self.hash_map) >= self.capacity:
            self.evict_lru_node()

        self.prepend(new_node)
        self.hash_map[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)