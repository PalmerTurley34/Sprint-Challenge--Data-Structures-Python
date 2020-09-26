class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.size = len(self.storage)
        self.times_appended = 0       

    def append(self, item):
        if self.times_appended == 0:
            self.storage[0] = item
        else:
            self.storage[self.times_appended % self.capacity] = item
        self.times_appended += 1

    def get(self):
        return [x for x in self.storage if x]

