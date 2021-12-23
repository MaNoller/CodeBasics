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

    rev=''
    while not stack.is_empty():
        rev+=stack.pop()
    return rev

stack = Stack()
string='We will conquere COVID-19'


if __name__ == '__main__':
    print(reverse_string("We will conquere COVI-19"))
    print(reverse_string("I am the king"))

'''
Write a function in python that checks if paranthesis in the string are balanced or not. 
Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial. 
'''


def is_balanced(string):
    klammern = {')': '(', ']': '[', '}': '{'}
    stack=Stack()
    for el in string:
        if el in ['[','(','{']:
            stack.push(el)
        if el in [']',')','}']:
            if stack.size()==0:
                return False
            if not stack.pop()==klammern[el]:
                return False

    if stack.size()==0:
        return True
    else:
        return False




def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced_2(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0


if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
    print('AB HIER LSG:')
    print(is_balanced_2("({a+b})"))
    print(is_balanced_2("))((a+b}{"))
    print(is_balanced_2("((a+b))"))
    print(is_balanced_2("((a+g))"))
    print(is_balanced_2("))"))
    print(is_balanced_2("[a+b]*(x+2y)*{gg+kk}"))

