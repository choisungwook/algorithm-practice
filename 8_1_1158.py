import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cursor = None
        self.cursor_before = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.head.next = self.head
            self.cursor = self.head
            self.cursor_before = self.head
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def move_cursor(self, times):
        for _ in range(times):
            self.cursor_before = self.cursor
            self.cursor = self.cursor.next

    def pop(self):
        data = self.cursor.data

        self.cursor_before.next = self.cursor.next
        self.cursor = self.cursor.next
        self.size -= 1

        return str(data)

    def get_current_data(self):
        return str(self.cursor.data)

    def get_size(self):
        return self.size

    def print_all(self):
        node = self.head
        size = 0

        while size != self.size:
            print(node.data)
            node = node.next
            size += 1


if __name__=="__main__":
    k, n = map(int, sys.stdin.readline().split())
    linked_list = LinkedList()

    for idx in range(1, k+1):
        linked_list.append(idx)

    answer = []
    while linked_list.get_size() != 1:
        linked_list.move_cursor(n-1)
        answer.append(linked_list.pop())

    answer.append(linked_list.get_current_data())

    print("<", end="")
    print(", ".join(answer), end="")
    print(">", end="")