class Heap:
    def __init__(self, max_heap=True):
        self.heap = []
        self.max_heap = max_heap

    def is_empty(self):
        if len(self.heap)==0:
            return True
        return False
    def size(self):
	    return len(self.heap)

    def insert(self, value):
	    self.heap.append(value)

    def extract(self):
        if self.max_heap:
            a=max(self.heap)
            self.heap.remove(a)
            return a
        else:
            a=min(self.heap)
            self.heap.remove(a)
            return a

    def peek(self):
        if self.max_heap:
            a=max(self.heap)
            return a
        else:
            a=min(self.heap)
            return a

    def _heapify_up(self, index):
	    pass

    def _heapify_down(self, index):
	    pass

# Пример использования
h = Heap(max_heap=True)  # Создаем максимальную кучу

# Вставка элементов
h.insert(10)
h.insert(4)
h.insert(15)
h.insert(20)
h.insert(3)

print("Корень кучи:", h.peek())  # Ожидаемый вывод: 20

# Извлечение корней
while not h.is_empty():
	print("Извлеченный элемент:", h.extract())
