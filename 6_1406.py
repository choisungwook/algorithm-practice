from os import link
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.before = None

class LinkedList:
    def __init__(self):
        self.dummy = Node(None)
        self.head = self.dummy
        self.tail = self.dummy

        self.head.next = self.tail
        self.tail.before = self.head

        self.cursor = self.dummy
        self.size = 0

    def append(self, data):
        '''tail에 노드 추가'''
        new_node = Node(data)

        # 링크 연결
        new_node.before = self.tail
        self.tail.next = new_node

        # 노드 변경
        self.tail = new_node
        self.cursor = new_node

        self.size += 1

    def insert(self, data):
        '''중간에 노드 삽입'''
        new_node = Node(data)
        node_cursornext = self.cursor.next

        # 링크 연결
        self.cursor.next = new_node
        node_cursornext.before = new_node
        new_node.before = self.cursor
        new_node.next = node_cursornext

        # 노드 변경
        self.cursor = new_node

        self.size += 1

    def rpop(self):
        '''tail 노드제거'''
        node_cursorbefore = self.cursor.before

        # 링크변경
        node_cursorbefore.next = None

        # 노드 변경
        self.cursor = node_cursorbefore
        self.tail = node_cursorbefore

        self.size -= 1

    def delete(self):
        '''중간 노드 삭제'''
        # 링크 변경
        node_cursorbefore = self.cursor.before
        node_cursorafter = self.cursor.next

        node_cursorbefore.next = node_cursorafter
        node_cursorafter.before = node_cursorbefore

        # 노드 변경
        self.cursor = node_cursorbefore
        self.size -= 1

    def move_cursor_left(self):
        self.cursor = self.cursor.before

    def move_cursor_right(self):
        self.cursor = self.cursor.next

    def print_all(self):
        if self.size != 0:
            travel_node = self.head.next
            while travel_node:
                print(travel_node.data, end="")
                travel_node = travel_node.next

            print("")

    #
    # command
    #

    def p_command(self, data):
        if self.cursor == self.tail:
            self.append(data)
        else:
            self.insert(data)

    def l_command(self):
        if self.cursor != self.dummy:
            self.move_cursor_left()

    def d_command(self):
        if self.cursor != self.tail:
            self.move_cursor_right()

    def b_command(self):
        if self.cursor == self.head:
            return
        if self.cursor == self.tail:
            self.rpop()
        else:
            self.delete()

if __name__=="__main__":
    linkedlist = LinkedList()

    for data in list(sys.stdin.readline().rstrip()):
        linkedlist.append(data)

    testcase = int(sys.stdin.readline())
    for _ in range(testcase):
        command = sys.stdin.readline().rstrip()

        if command == "L":
            linkedlist.l_command()
        elif command == "D":
            linkedlist.d_command()
        elif command == "B":
            linkedlist.b_command()
        else:
            opcode, operand = command.split(" ")
            linkedlist.p_command(operand)

    linkedlist.print_all()
