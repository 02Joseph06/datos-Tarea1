class Queue:
    
    # initial_elements: allow the collection to start with some elements
    def __init__(self, initial_elements=[]):
        self._elements = list(initial_elements)
    
    # return an str of the collection
    def __str__(self):
        return str(self._elements)
    
    # return the length of the elements in the collection
    def __len__(self):
        return len(self._elements)
    
    # return a boolean that implies if the collection is empty or not
    def isEmpty(self):
        return len(self._elements) == 0
    
    # return the next element in the collection
    def peek(self):
        if self.isEmpty():
            raise IndexError("Error: the queue is empty")
        return self._elements[0]
    
    # allow the collection to be called in a for loop
    def __iter__(self):
        return iter(self._elements)
    
    # return a boolean value representing the existence of an element in the collection
    def __contains__(self, element):
        return element in self._elements
    
    # add the element to the collection
    def push(self, element):
        self._elements.append(element)
    
    # remove and return the next element in the collection
    def pop(self, index=0):
        if self.isEmpty():
            raise IndexError("Error: the queue is empty")

        first_index = 0
        if index != first_index and index != -len(self._elements):
            raise IndexError("Error: the index dont exist")

        return self._elements.pop(0)
