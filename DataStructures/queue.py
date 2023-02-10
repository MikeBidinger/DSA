class Queue:
    def __init__(self, cap):
        self.cap = cap
        self.front = 0
        self.size = 0
        self.rear = cap - 1
        self.Q = [0] * cap

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.cap

    def enQueue(self, item):
        if self.isFull():
            print("Queue is full!")
            return
        self.rear = (self.rear + 1) % (self.cap)
        self.Q[self.rear] = item
        self.size += 1
        print("Enqueued:", item)

    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty!")
            return
        print("Dequeued:", self.Q[self.front])
        self.front = (self.front + 1) % (self.cap)
        self.size -= 1

    def get_front(self):
        if self.isEmpty():
            return "Queue is empty!"
        return self.Q[self.front]

    def get_rear(self):
        if self.isEmpty():
            return "Queue is empty!"
        return self.Q[self.rear]

    def printQueue(self):
        if self.isEmpty():
            print("Queue is empty!")
            return
        for i in range(self.front, self.front + self.cap):
            if i >= self.cap:
                print(i - self.front, ":", self.Q[i - self.cap])
            else:
                print(i - self.front, ":", self.Q[i])


if __name__ == "__main__":

    # Create a queue
    q = Queue(5)

    # Enqueue items
    q.enQueue(10)
    q.enQueue("A")
    q.enQueue(20)
    q.enQueue(30)
    q.enQueue(40)
    q.enQueue(50)

    # Dequeue item
    q.deQueue()
    q.enQueue(50)

    # Get front of queue
    print("Front:", q.get_front())

    # Get rear of queue
    print("Rear:", q.get_rear())

    # Print queue
    q.printQueue()
