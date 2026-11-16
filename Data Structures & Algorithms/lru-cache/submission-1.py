
class LRUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.hashmap = {}
        self.head = LLNode(-1,0)
        self.tail = LLNode(-1,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        
        if key in self.hashmap:
            node = self.hashmap[key]
            value = node.val
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            node.prev = self.head

            return value
            
        else:
            return -1


    def put(self, key: int, value: int) -> None:

        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            node.prev = self.head

        else:
            new_node = LLNode(key,value)
            new_node.next = self.head.next
            self.head.next.prev = new_node
            self.head.next = new_node
            new_node.prev = self.head
            self.hashmap[key] = new_node

        if len(self.hashmap) > self.capacity:
            last_node = self.tail.prev
            last_node.prev.next = self.tail
            self.tail.prev = last_node.prev
            del self.hashmap[last_node.key]
            
class LLNode:

    def __init__(self,key,val):

        self.key = key
        self.val = val
        self.next = None
        self.prev = None
