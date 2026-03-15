class _Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularList:
    
    # initial_elements: allow the collection to start with some elements
    def __init__(self, initial_elements=[]):
        self.head = None
        self.tail = None
        self._size = 0
        for element in initial_elements:
            self.append(element)
    
    # return an str of the collection
    def __str__(self):
        return str([element for element in self])
    
    # return the length of the elements in the collection
    def __len__(self):
        return self._size
    
    # return the element of the collection in the index possition
    # Error: the index dont exist
    def __getitem__(self, index):
        if index < 0:
            index += self._size
        if index < 0 or index >= self._size:
            raise IndexError("Error: the index dont exist")

        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    # return a boolean that implies if the collection is empty or not
    def isEmpty(self):
        return self._size == 0
    
    # allow the collection to be called in a for loop
    def __iter__(self):
        current = self.head
        steps = 0
        while steps < self._size:
            yield current.value
            current = current.next
            steps += 1
    
    # return a boolean value representing the existence of an element in the collection
    def __contains__(self, element):
        for current_element in self:
            if current_element == element:
                return True
        return False
    
    # add the element to the end of the collection
    def append(self, element):
        new_node = _Node(element)

        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    # insert the element to the desired index of the collection
    def add(self, index, element):
        if index < 0:
            index += self._size
        if index < 0 or index > self._size:
            raise IndexError("Error: the index dont exist")

        if index == self._size:
            self.append(element)
            return

        new_node = _Node(element)

        if index == 0:
            if self.isEmpty():
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = self.head
            self._size += 1
            return

        prev = self.head
        for _ in range(index - 1):
            prev = prev.next

        new_node.next = prev.next
        prev.next = new_node
        self._size += 1
    
    # remove an element in the collection by its value
    # Error: the element dont exist in the collection
    def remove(self, element):
        if self.isEmpty():
            raise ValueError("Error: the element dont exist in the collection")

        current = self.head
        prev = self.tail

        for _ in range(self._size):
            if current.value == element:
                if self._size == 1:
                    self.head = None
                    self.tail = None
                else:
                    prev.next = current.next
                    if current == self.head:
                        self.head = current.next
                    if current == self.tail:
                        self.tail = prev
                    self.tail.next = self.head
                self._size -= 1
                return

            prev = current
            current = current.next

        raise ValueError("Error: the element dont exist in the collection")
    
    # remove and return the element in the collection by its index
    def pop(self, index):
        if index < 0:
            index += self._size
        if index < 0 or index >= self._size:
            raise IndexError("Error: the index dont exist")

        if self._size == 1:
            value = self.head.value
            self.head = None
            self.tail = None
            self._size = 0
            return value

        if index == 0:
            value = self.head.value
            self.head = self.head.next
            self.tail.next = self.head
            self._size -= 1
            return value

        prev = self.head
        for _ in range(index - 1):
            prev = prev.next

        current = prev.next
        value = current.value
        prev.next = current.next

        if current == self.tail:
            self.tail = prev

        self.tail.next = self.head
        self._size -= 1
        return value
    
    # remove all elements in the collection
    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
