class Coffeecup:
    def __init__(self, capacity, amount):
        self.capacity = capacity
        self.amount = amount

    def fill(self):
        self.amount = self.capacity
        print(f"Amount is: {self.amount}")
        return self

    def empty(self):
        self.amount = 0
        print(f"Amount is: {self.amount}")
        return self

    def drink(self, drunk):
        if self.amount > 0:
            self.amount = self.amount - drunk
            print(f"Amount is: {self.amount}")
        else:
            print('The cup is empty!')
        return self
    