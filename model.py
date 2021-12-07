class Model:

    def __init__(self):
        self.count = 0

    def incr(self):
        self.count += 1

    def decr(self):
        self.count -= 1

    def get_count(self):
        return self.count
