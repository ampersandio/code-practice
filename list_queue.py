class ListQueue():
    def __init__(self):
        self.queue = []

    def enqueue(self,value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)
    
    def print_queue(self):
        return self.queue
    
new_queue = ListQueue()

new_queue.enqueue(5)
new_queue.enqueue(10)
new_queue.enqueue(15)

new_queue.dequeue()
new_queue.dequeue()

print(new_queue.print_queue())
