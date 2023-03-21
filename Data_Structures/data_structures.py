class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList():
    #
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append(" ")
        return " -> ".join(nodes)

    def read(self,index):
        current_node = self.head
        current_index = 0

        while current_index < index:
            current_node = current_node.next
            current_index += 1
            if current_node is None:
                return None
        
        return current_node

    def index_of(self,searched_value):
        current_node = self.head
        current_index = 0

        while current_node is not None:
            if current_node.data == searched_value:
                return current_index
            current_node = current_node.next
            current_index += 1

        return None    

    def insert_at_index(self, index, inserted_value):
        new_node = Node(inserted_value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            current_index = 0

            while current_index < (index - 1):
                current_node = current_node.next
                if current_node is None:
                    return
                current_index += 1
                

            new_node.next = current_node.next
            current_node.next = new_node

    def delete_at_index(self,index):
        current_node = self.head
        current_index = 0

        if index == 0:
            self.head = current_node.next
        else:
            while current_index < (index - 1):
                current_node = current_node.next
                if current_node is None:
                    return None
                current_index += 1
                
            next_node = current_node.next
            current_node.next = next_node.next

    # add first
    def push(self, added_value):
        new_node = Node(added_value)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, added_value):
        new_node = Node(added_value)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def reverse(self):
        prev_node = None
        current_node = self.head
        
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" -> ")
            temp = temp.next
        print(end="\n")
 
##         


class Stack():
    # like linked list
    def __init__(self):
        self.head = Node("head")
        self.size = 0
        
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur is not None:
            out = str(cur.data) + "->"
            cur = cur.next
        return out[:-2]
    
    def getsize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def push(self, data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        poped = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return poped.data
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" -> ")
            temp = temp.next
        print(end="\n")    
##    

class Stack2():
    
    def __init__(self):
        self.stack = []

    def push(self, data):
           if data not in self.stack:
                self.stack.append(data)
                return True     

    def top(self):
        return self.stack[-1]
    
    def pop(self):
        if len(self.stack) <= 0:
            return ("Stack empty")
        else:
            return self.stack.pop()
        

##

class Queue():
    # implemented like linked list
    def __init__(self):
        self.head = Node("head")
        self.size = 0
    pass

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out = str(cur.data) + "->"
            cur = cur.next
        return out[:]
    
    def getsize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        tempsize = self.size
        cur = self.head
        while tempsize > 1:
            cur = cur.next
            tempsize -= 1
        dequeued = cur.next
        cur.next = None
        self.size -= 1
        return dequeued.data
    
    def add(self,data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" -> ")
            temp = temp.next
        print(end="\n")    
##

class Queue2():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def print(self):
        print(self.items)
##

class HashTable():
    def __init__(self):
        self.MAX = 127
        self.table = [None for i in range(self.MAX)]

    # Hash Fuction
    def Hash_func(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, value):
        hash = self.Hash_func(key)
        if self.table[hash] is None:
            self.table[hash] = value

    def __getitem__(self, key):
        hash = self.Hash_func(key)
        return self.table[hash]
        
    def __delitem__(self, key):
        hash = self.Hash_func(key)
        if self.table[hash] is None:
            print("No element found with key:", key)
        else:
            print("Deleted element with key:", key)
            self.table[hash] = None
##


# BinaryTree
class NodeBT():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def search(root, data):
    pass

def insert(root, node):
    pass

##

class Heap():
    # halda
    pass

##

class Graph():
    # 
    pass

##


#----------------------------------------------------------------------------------

# linked_list = LinkedList()
# print(linked_list)
# first_node = Node("a")
# second_node = Node("b")
# linked_list.head = first_node
# first_node.next = second_node
# print(linked_list)
# print(linked_list.read(1))
# print(linked_list.index_of("b"))
# linked_list.insert_at_index(2,'c')
# linked_list.insert_at_index(3,'d')
# print(linked_list)
# linked_list.delete_at_index(1)
# print(linked_list)
# linked_list.push("1")
# print(linked_list, "\n")
# linked_list.insert_at_index(4,'e')
# linked_list.add_last("5")
# print("Linked list1:")
# linked_list.printList()
# linked_list.reverse()
# print("Linked list1 reversed:")
# linked_list.printList()


# list2 = LinkedList()
# list2.push("1")
# list2.push("2")
# list2.push("3")
# list2.push("4")
# print("Linked list2:")
# list2.printList()
# list2.reverse()
# print("Linked list2 reversed:")
# list2.printList()

# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.printList()
# print(stack.pop())
# stack.printList()
# stack.pop()
# stack.printList()

# Q = Queue()
# Q.add(1)
# Q.add(2)
# Q.add(3)
# Q.printList()
# print(Q.dequeue())
# Q.printList()
# print(Q.dequeue())
# Q.printList()
# print(Q.dequeue())
# Q.printList()

# ht = HashTable()
# ht['a'] = 1
# ht['b'] = 2
# del ht['a']
# print(ht.table)
# print(ht['a'])
# print(ht['b'])

# q = Queue2()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(1)
# q.enqueue(1)
# q.print()
# q.dequeue()
# q.dequeue()
# q.print()

root = NodeBT(1)
root.left = NodeBT(2)
root.right = NodeBT(3)
root.left.left = NodeBT(4)
root.left.right = NodeBT(5)
root.right.left = NodeBT(6)
root.right.right = NodeBT(7)

print(root.left.left.data)