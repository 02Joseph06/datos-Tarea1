class LinkedList:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    # initial_elements: allow the collection to start with some elements
    def __init__(self, initial_elements=[]):
        self._head = None
        self._longitud = 0
        for elemento in initial_elements:
            self.append(elemento)

    # return an str of the collection
    def __str__(self):
        elementos = []
        actual = self._head
        while actual is not None:
            elementos.append(str(actual.data))
            actual = actual.next
        return "[" + ", ".join(elementos) + "]"

    # return the length of the elements in the collection
    def __len__(self):
        return self._longitud

    # return the element of the collection in the index possition
    # Error: the index dont exist
    def __getitem__(self, index):
        if index < 0 or index >= self._longitud:
            raise IndexError(f"Índice {index} fuera de rango. La colección tiene {self._longitud} elementos.")
        actual = self._head
        for _ in range(index):
            actual = actual.next
        return actual.data

    # return a boolean that implies if the collection is empty or not
    def isEmpty(self):
        return self._longitud == 0

    # allow the collection to be called in a for loop
    def __iter__(self):
        actual = self._head
        while actual is not None:
            yield actual.data
            actual = actual.next

    # return a boolean value representing the existence of an element in the collection
    def __contains__(self, element):
        actual = self._head
        while actual is not None:
            if actual.data == element:
                return True
            actual = actual.next
        return False

    # add the element to the end of the collection
    def append(self, element):
        nuevo = self.Node(element)
        if self._head is None:
            self._head = nuevo
        else:
            actual = self._head
            while actual.next is not None:
                actual = actual.next
            actual.next = nuevo
        self._longitud += 1

    # add the element to the collection at the requested index
    # Error: non existing index in the collection
    def insert(self, index, element):
        if index < 0 or index > self._longitud:
            raise IndexError(f"Índice {index} fuera de rango. No se puede insertar en esa posición.")
        nuevo = self.Node(element)
        if index == 0:
            nuevo.next = self._head
            self._head = nuevo
        else:
            actual = self._head
            for _ in range(index - 1):
                actual = actual.next
            nuevo.next = actual.next
            actual.next = nuevo
        self._longitud += 1

    # remove an element in the collection by its value
    # Error: the element dont exist in the collection
    def remove(self, element):
        if self._head is None:
            raise ValueError(f"El elemento '{element}' no existe en la colección.")
        if self._head.data == element:
            self._head = self._head.next
            self._longitud -= 1
            return
        actual = self._head
        while actual.next is not None:
            if actual.next.data == element:
                actual.next = actual.next.next
                self._longitud -= 1
                return
            actual = actual.next
        raise ValueError(f"El elemento '{element}' no existe en la colección.")

    # remove and return the element in the collection by its index
    def pop(self, index):
        if index < 0 or index >= self._longitud:
            raise IndexError(f"Índice {index} fuera de rango. La colección tiene {self._longitud} elementos.")
        if index == 0:
            dato = self._head.data
            self._head = self._head.next
        else:
            actual = self._head
            for _ in range(index - 1):
                actual = actual.next
            dato = actual.next.data
            actual.next = actual.next.next
        self._longitud -= 1
        return dato

    # remove all elements in the collection
    def clear(self):
        self._head = None
        self._longitud = 0