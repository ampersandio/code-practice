class Node():
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_ll(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


    def append(self,value):
        '''
        time complexity O(1) - constant - no traversing, just switching pointers
        '''
        new_node = Node(value)
        temp = self.tail
        temp.next = new_node
        self.tail = new_node
        self.length += 1


    def prepend(self,value):
        '''
        time complexity O(1) - constant - no traversing, just switching pointers
        '''

        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        temp = self.head
        self.head = new_node
        new_node.next = temp
        self.length += 1
    

    def pop(self):
        '''
        time complexity O(n) - linear - traversing the list to get to the last item
        '''
        temp = self.tail
        last_node = self.head

        while last_node.next is not self.tail:
            last_node = last_node.next

        self.tail = last_node
        self.tail.next = None
        self.length -= 1
        return temp

    def get_at_index(self,index):
        '''
        time complexity O(n) - linear - traversing the list to get to the last item
        '''

        idx = 0
        temp = self.head
        
        if index == 0:
            return self.head

        while idx < index-1:
            temp = temp.next
            idx += 1 

        return temp
    

    def add_at_index(self,value,index):
        '''
        time complexity O(n) - linear - traversing the list to get to the last item
        '''
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)

        new_node = Node(value)
        prev_node = self.get_at_index(index)
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.next = next_node

    def reverse(self):
        previous = None
        current = self.head
        self.tail = self.head

        while current is not None:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt

        self.head = previous


    def reverse(self):
        previous = None
        current = self.head
        self.tail = self.head

        while current is not None:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt

        self.head = previous






















    # def reverse(self):
    #     temp = self.head
    #     self.head = self.tail
    #     self.tail = temp
    #     before = None

    #     for _ in range(self.length):
    #         after = temp.next
    #         temp.next = before
    #         before = temp
    #         temp = after


new_ll = LinkedList(5)

new_ll.append(10)
new_ll.append(25)
new_ll.append(50)
# new_ll.print_ll()

new_ll.prepend(1)

new_ll.prepend(-1204)


new_ll.add_at_index("value",2)


new_ll.reverse()

new_ll.print_ll()
