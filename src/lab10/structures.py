from collections import deque


class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __repr__(self):
        return f"Stack({self._data})"


class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self):
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __repr__(self):
        return f"Queue({list(self._data)})"


def main():
    print("Stack")
    s = Stack()

    # Показываем push и peek
    s.push(1)
    s.push(2)
    s.push(3)
    print(f"добавили 1, 2, 3: {s}")
    print(f"верхний элемент: {s.peek()}")

    # Показываем pop
    print(f"удаляем: {s.pop()}")
    print(f"теперь стек: {s}")

    # Показываем is_empty
    print(f"стек пуст? {s.is_empty()}")

    print("\nQueue (Очередь)")
    q = Queue()

    # Показываем enqueue и peek
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    print(f"добавили A, B, C: {q}")
    print(f"первый в очереди: {q.peek()}")

    # Показываем dequeue
    print(f"обслуживаем: {q.dequeue()}")
    print(f"теперь очередь: {q}")

    # Показываем is_empty
    print(f"очередь пуста? {q.is_empty()}")


if __name__ == "__main__":
    main()
