from collections import deque
import time
import threading
class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]

'''
Class implementation from Tutorial

...
Design a food ordering system where your python program will run two threads,

    Place Order: This thread will be placing an order and inserting that into a queue.
     This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
    Serve Order: This thread will server the order. All you need to do is pop the order out of the
     queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second 
     after place order thread is started.

Use this video to get yourself familiar with multithreading in python

Pass following list as an argument to place order thread,
orders = ['pizza','samosa','pasta','biryani','burger']
This problem is a producer,consumer problem where place_order thread is producing orders whereas 
server_order thread is consuming the food orders. Use Queue class implemented in a video tutorial.

'''
orderue= Queue()

def place_order(orders):
    for order in orders:
        print('Ordering: ', order)
        orderue.enqueue(order)
        time.sleep(0.5)

def serve_order(orders):
    time.sleep(1)
    for order in orders:
        print('Placing: ', order)
        orderue.dequeue()
        time.sleep(2.0)



'''
if __name__ == '__main__':
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    t1=threading.Thread(target=place_order,args=(orders,))
    t2=threading.Thread(target=serve_order,args=(orders,))

    t1.start()
    t2.start()

'''
'''
Write a program to print binary numbers from 1 to 10 using Queue.
Use Queue class implemented in main tutorial. Binary sequence should look like,

    1
    10
    11
    100
    101
    110
    111
    1000
    1001
    1010



Hint: Notice a pattern above. After 1 second and third number is 1+0 and 1+1. 4th and 5th number 
are second number (i.e. 10) + 0 and second number (i.e. 10) + 1.
You also need to add front() function in queue class that can return the front element in the queue.
'''

def binary_numbers(n):
    numb_queue = Queue()
    numb_queue.enqueue("1")

    for i in range(n):
        front = numb_queue.front()
        print("   ", front)
        #numb_queue.enqueue(front + "0")
        numb_queue.enqueue(front + "0")
        numb_queue.enqueue(front + "1")

        numb_queue.dequeue()
        #print('size=',numb_queue.size())

if __name__ == '__main__':
    binary_numbers(10)

'Anmekerung: Lösung aus Aufgabe übernommen'