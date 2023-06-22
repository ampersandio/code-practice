class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack():
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node 

    def push(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


    def pop(self):
        temp = self.head
        self.head = temp.next

        return temp.value


    def print_stack(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        

new_stack = Stack(5)
new_stack.push(10)
new_stack.push(20)
new_stack.push(30)

print("popped",new_stack.pop())
print("popped",new_stack.pop())

new_stack.print_stack()