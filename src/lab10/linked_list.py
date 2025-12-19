class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def prepend(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

        self._size += 1

    def insert(self, idx, value):
        if idx < 0 or idx > self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size}]")

        if idx == 0:
            self.prepend(value)
            return

        if idx == self._size:
            self.append(value)
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        new_node = Node(value, current.next)
        current.next = new_node
        self._size += 1

    def remove_at(self, idx):
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size})")

        if idx == 0:
            value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return value

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        value = current.next.value
        if current.next == self.tail:
            self.tail = current
        current.next = current.next.next

        self._size -= 1
        return value

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size

    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"


def main():
    print("SinglyLinkedList (односвязный список)")
    lst = SinglyLinkedList()

    # append
    lst.append(10)
    lst.append(20)
    lst.append(30)
    print(f"добавили 10, 20, 30: {lst}")

    # prepend
    lst.prepend(5)
    print(f"добавили 5 в начало: {lst}")

    # insert
    lst.insert(2, 15)  # Между 10 и 20
    print(f"вставили 15 на позицию 2: {lst}")

    # remove_at
    removed = lst.remove_at(1)
    print(f"удалили элемент на позиции 1: {removed}")
    print(f"теперь список: {lst}")

    # __len__
    print(f"длина списка: {len(lst)}")

    # __iter__
    print("элементы списка:", end=" ")
    for item in lst:
        print(item, end=" ")


if __name__ == "__main__":
    main()
