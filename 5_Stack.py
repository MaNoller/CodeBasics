from collections import deque

'''
reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
Using: Stack class from tutorial
'''


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def reverse_string(string):
    for el in string:
        stack.push(el)


stack = Stack()
string='We will conquere COVID-19'


if __name__ == '__main__':
    print(reverse_string("We will conquere COVI-19"))
    print(reverse_string("I am the king"))
