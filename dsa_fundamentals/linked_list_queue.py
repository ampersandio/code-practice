class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue():
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self,value):
        new_node = Node(value)
        temp = self.last
        temp.next = new_node
        self.last = new_node

    def dequeue(self):
        temp = self.first.next
        self.first = temp

    def print_queue(self):
        temp = self.first

        while temp is not None:
            print(temp.value)
            temp = temp.next



new_queue = Queue(5)
new_queue.enqueue(10)
new_queue.enqueue(15)
new_queue.enqueue(20)

# new_queue.dequeue()
# new_queue.dequeue()

new_queue.print_queue() 