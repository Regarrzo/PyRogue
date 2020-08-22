"""
This module implements a shared link list. 

It makes it possible to have a master list and sublists that reference 
parts of the master list. It has the following properties:

- Removing items from the master list will recursively remove them from all
  sublists

- Inserting items into the master list will allow them to be inserted into
  any of the sublists

- Sublists cannot contain elements which are not present in the master list

- Removing items from sublists will not remove them from the master list

- Insertion and removal at any position have O(1) time complexity
"""


class _Node:
    def __init__(self, data):
        self.data = data

        self.next = None
        self.prev = None


class _SharedListIterator:
    def __init__(self, node):

        begin_iterator = _Node(None)
        begin_iterator.next = node

        self.node = begin_iterator
    
    def __iter__(self):
        return self

    def __next__(self):
        self.node = self.node.next

        if not self.node:
            raise StopIteration

        return self.node


class SharedList:
    def __init__(self, master=None, sublists=None):
        self.master = master
        self.sublists = sublists

        if not sublists:
            self.sublists = []
        
        self._head = None
        self._tail = None
        self._len = 0
    
    def __str__(self):
        return "[" + ", ".join([str(node.data) for node in self]) + "]"

    def __len__(self):
        return self._len
    
    def __delitem__(self, node):
        self.remove(node)
    
    def __iter__(self):
        return _SharedListIterator(self._head)

    def _create_inital_node(self, data):
        self._head = _Node(data)
        self._tail = self._head
    
    def _validate_index(self, index):
        if index < 0:
            index = self._len + index

        if self._len > 0 and index >= self._len:
            raise IndexError("Index out of bounds.")
            
        return index

    def _traverse_forward(self, node, n):
        for _ in range(n):
            node = node.next
        
        return node
    
    def _traverse_backward(self, node, n):
        for _ in range(n):
            node = node.prev

        return node
    
    def _traverse_to(self, index):
        index = self._validate_index(index)

        if index > self._len // 2:
            node = self._traverse_backward(self._tail, self._len - index - 1)
        else:
            node = self._traverse_forward(self._head, index)
        
        return node
    
    def push_back(self, data):
        self.insert_after(self._tail, data)

    def push_front(self, data):
        self.insert_before(self._head, data)

    def insert_at(self, index, data):
        node = self._traverse_to(index)
        self.insert_after(node, data)


    def insert_after(self, node, data):
        """
        Insert data into the list after the specified node
        """

        self._len += 1

        if not self._head:
            self._create_inital_node(data)
            return 
        
        new_node = _Node(data)

        if node.next:
            node.next.prev = new_node
            new_node.next = node.next
        else:
            self._tail = new_node
        
        node.next = new_node
        new_node.prev = node
    

    def insert_before(self, node, data):
        """
        Insert data into the list before the specified node
        """

        self._len += 1

        if not self._head:
            self._create_inital_node(data)
            return 
        
        new_node = _Node(data)

        if node.prev:
            node.prev.next = new_node
            new_node.prev = node.prev
        
        node.prev = new_node
        new_node.next = node

    def remove(self, node):

        if node.next and node.prev:
            # Node is in the middle of the list
            node.prev.next = node.next
            node.next.prev = node.prev

        elif node.next and not node.prev:
            # Node is at the tail of the list
            node.next.prev = None
            self._tail = node.next
        
        elif node.prev and not node.next:
            # Node is at the head of the list
            node.prev.next = None
            self._head = node.prev

        else:
            # Node is the head and the tail, list is only 1 long
            if not self._len == 1:
                raise ValueError(f"Tail or head incompatible with \
                    list of length {self._len}")

            self._tail = None
            self._head = None

        self._len -= 1
        del node
    
    def remove_at(self, index):
        node = self._traverse_to(index)
        self.remove(node)
