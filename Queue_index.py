# Mahan Kiyani first Data Structures Project
class Queue:
    def __init__(self, max_size):
        self.max_size = max_size 
        self.Q = [None] * max_size 
        self.num = 0
        self.first = 0
    
    def __str__(self): # in baraye khoshgelish 🤓
        return f'list is {self.Q}'

    def enqueue(self, item):
        if self.num >= self.max_size:
            raise IndexError("Queue overflow")
        
        self.Q[(self.num + self.first) % self.max_size] = item 
        self.num += 1

    def dequeue(self):
        if self.num == 0:
            raise Exception("Queue empty")
        
        item = self.Q[self.first]
        self.Q[self.first] = None
        
        self.first = (self.first + 1) % self.max_size 
        self.num -= 1

        return item
    
    def dequeue_data(self, item):
        if item in self.Q:
            self.Q.remove(item)
            self.num -= 1
            return item
        else:
            return None
    
    def front(self):
        if self.is_empty():
            raise Exception("Queue empty") 
        return self.Q[self.first]

    def is_empty(self): 
        return self.num == 0

    def size(self): 

        return self.num
        

    def is_full(self):
        return self.num >= self.max_size
    
    def index(self, ind):
        
        if 0 <= ind <= self.size():
            return self.Q[ind]
        else:
            print('index is out of the range')
def main():
        
    q = Queue(int(input('please enter your queue Length: '))) 
    q.enqueue("ra'na") 
    q.enqueue("vez") 
    q.enqueue("Arya") 
    print("queue size is: ",q.size())
    print(q.dequeue(), "left the queue") 
    print("front of queue is:",q.front()) 
    q.enqueue("milda") 
    print(f"It was your queue: {q}")

    ind = int(input('enter your item you want: '))
    print(q.index(ind))
    print(f"It was your queue: {q}")
    print(f"you remove {q.dequeue_data('milda')}")
    print(f"It was your queue: {q}")

if __name__ == '__main__':
    main()