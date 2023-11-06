class FibIter:
    def __init__(self, steps):
        self.steps = steps

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        if self.steps == 0:
            raise StopIteration
        self.steps -= 1

        fib = self.a
        self.a, self.b = self.b, self.a + self.b

        return fib


myclass = FibIter(10)
myiter = iter(myclass)


for x in myiter:
    print(x)
