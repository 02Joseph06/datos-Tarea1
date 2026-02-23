class ArrayList:
    
    # size: initial capacity of the collection
    # initial_elements: allow the collection to start with some elements
    def __init__(self, size=100, initial_elements=[]):
        self._capacidad = size
        self._arreglo = [None] * self._capacidad
        self._longitud = 0
        
        for elemento in initial_elements:
            self.append(elemento)
    
    # return an str of the collection
    def __str__(self):
        elementos = [str(self._arreglo[i]) for i in range(self._longitud)]
        return "[" + ", ".join(elementos) + "]"
    
    # return the length of the elements in the collection
    def __len__(self):
        return self._longitud

    # return a boolean that implies if the collection is empty or not
    def isEmpty(self):
        return self._longitud == 0
    
    # return the element of the collection in the index possition
    # Error: the index dont exist
    def __getitem__(self, index):
        if index < 0 or index >= self._longitud:
            raise IndexError(f"Índice {index} fuera de rango. La colección tiene {self._longitud} elementos.")
        return self._arreglo[index]
    
    # allow the collection to be called in a for loop
    def __iter__(self):
        self._indice_iterador = 0
        return self
    
    def __next__(self):
        if self._indice_iterador >= self._longitud:
            raise StopIteration
        elemento = self._arreglo[self._indice_iterador]
        self._indice_iterador += 1
        return elemento
    
    # return a boolean value representing the existence of an element in the collection
    def __contains__(self, element):
        for i in range(self._longitud):
            if self._arreglo[i] == element:
                return True
        return False
    
    # add the element to the end of the collection
    def append(self, element):
        if self._longitud >= self._capacidad:
            raise OverflowError("La colección está llena. No se pueden agregar más elementos.")
        self._arreglo[self._longitud] = element
        self._longitud += 1
    
    # add the element to the collection at the requested index
    # Error: non existing index in the collection
    def insert(self, index, element):
        if index < 0 or index > self._longitud:
            raise IndexError(f"Índice {index} fuera de rango. No se puede insertar en esa posición.")
        if self._longitud >= self._capacidad:
            raise OverflowError("La colección está llena. No se pueden insertar más elementos.")
        
        for i in range(self._longitud, index, -1):
            self._arreglo[i] = self._arreglo[i - 1]
        
        self._arreglo[index] = element
        self._longitud += 1
    
    # remove an element in the collection by its value
    # Error: the element dont exist in the collection
    def remove(self, element):
        for i in range(self._longitud):
            if self._arreglo[i] == element:
                for j in range(i, self._longitud - 1):
                    self._arreglo[j] = self._arreglo[j + 1]
                self._arreglo[self._longitud - 1] = None
                self._longitud -= 1
                return
        raise ValueError(f"El elemento '{element}' no existe en la colección.")
    
    # remove and return the element in the collection by its index
    def pop(self, index):
        if index < 0 or index >= self._longitud:
            raise IndexError(f"Índice {index} fuera de rango. La colección tiene {self._longitud} elementos.")
        
        elemento = self._arreglo[index]
        
        for i in range(index, self._longitud - 1):
            self._arreglo[i] = self._arreglo[i + 1]
        
        self._arreglo[self._longitud - 1] = None
        self._longitud -= 1
        return elemento
    
    # remove all elements in the collection
    def clear(self):
        self._arreglo = [None] * self._capacidad
        self._longitud = 0