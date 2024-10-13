import queue

"""
A queue is a linear data structure that follows
the First In, First Out (FIFO) principle.
This means that the first element added to the queue
will be the first one to be removed. A queue operates
similarly to a real-life queue, such as a line of people
waiting for a service — the person who arrives first
is served first.
"""

# creates a queue
people = queue.Queue()

# adds items to the end of the queue
people.put('Michael')    
people.put('Charlotte')  
people.put('Olivia')     

## prints number of elements of the queue
print('Number of queue elements:', people.qsize())

# gets and prints items from the queue
while not people.empty():
    person = people.get()
    print(person)
