class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node

    def remove_by_value(self, data):
        itr = self.head
        if itr.data == data:
            self.head = itr.next
        while itr:
            if itr.data == data:
                if itr.next:
                    itr = itr.next
                break
            itr = itr.next

    # Remove first node that contains data


ll = LinkedList()
ll.insert_values(["banana", "mango", "grapes", "orange"])
ll.print()
ll.insert_after_value("mango", "apple")  # insert apple after mango
ll.print()
ll.remove_by_value("orange")  # remove orange from linked list
ll.print()
ll.remove_by_value("figs")
ll.print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print()

###2.aufgabe
'''


Add following new methods,

def print_forward(self):
    # This method prints list in forward direction. Use node.next

def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.

Implement all other methods in regular linked list class and make necessary changes for doubly linked list (you need to populate node.prev in all those methods)
'''

class Node:

    def __init__(self, data=None, next=None, prev=None):
        self.data = data

        self.next = next

        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def print_forward(self):
        if self.head is None:
            print('List is empty')
            return
        itr=self.head
        llstr=''
        while itr:
            llstr+= str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr=itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print('List is empty')
            return
        itr = self.get_last_node()
        llstr=''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.prev else str(itr.data)
            itr = itr.prev
        print('reversed: ', llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def insert_at_begining(self, data):
        if self.head==None:
            self.head=Node(data, self.head)
        else:
            node = Node(data, self.head)
            self.head.prev=node
            self.head=node



    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, self.head)
            return

        itr = self.head

        while itr.next:
            itr = itr.next
        itr.next = Node(data, None,itr)


    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr.prev)
                if itr.next:
                    itr.next.prev=node
                itr.next = node
                break

            itr = itr.next
            count += 1


    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.head.prev=None
            return

        count = 0
        itr = self.head
        while itr:
            '''
            if count == index -1:
                itr.next = itr.next.next
                if itr.next.next:
                    itr.next.next.prev=itr
                break
            '''
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count+=1
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()