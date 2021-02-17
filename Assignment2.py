class Stack:
    data=[]

    def is_empty(self):
        return self.data==[]

    def push(self, node):
        self.data.append(node)

    def pop(self):
        if not self.is_empty():
            value=self.data[-1]
            del self.data[-1]
            return value
        else:
            print("Nothing to pop")

    def print_stack(self):
        for i in range(len(self.data)-1,-1,-1):
            print(self.data[i])
        print()



fruit = Stack()
fruit.pop()
fruit.push("Apple")
fruit.push("Banana")
fruit.pop()
fruit.push("Canned Yams")
fruit.push("Durian")
fruit.print_stack()
fruit.pop()
fruit.pop()
fruit.print_stack()

"""
Finish the Stack Class so that the print_stack method prints the stack vertically so that for instance ['a','b','c'] is printed 
a
b
c
"""

class Queue:
    data=[]

    """
    Write Queue functions for enqueue, dequeue, is_empty and print_queue
    """

    def is_empty(self):
        return self.data==[]

    def enqueue(self, node):
        self.data.append(node)

    def dequeue(self):
        if not self.is_empty():
            value=self.data[0]
            del self.data[0]
            return value
        else:
            print("Nothing to pop")

    def print_queue(self):
        for i in range(len(self.data)):
            print(self.data[i])
        print()




q=Queue()

q.enqueue('Job 1')
q.enqueue('Job 2')
q.enqueue('Job 3')
q.print_queue()
q.dequeue()
q.dequeue()
q.print_queue()



def is_palindrome(word):
    length = len(word)
    mid=length//2
    stack = Stack()
    for i in range(mid):
        stack.push(word[i])
    if 2*mid!=length:
        mid=mid+1
    for i in range(mid,length):
        x=stack.pop()
        if x!=word[i]:
            return False
    return True

if is_palindrome('racecar'):
    print('pass')
else:
    print('fail')

if is_palindrome('mom'):
    print('pass')
else:
    print('fail')

if is_palindrome('noon'):
    print('pass')
else:
    print('fail')

if is_palindrome('test'):
    print('pass')
else:
    print('fail')