
class CountUp:

    def __init__(self, max : int , start_from : int | None = 0):

        if max is None:
            raise ValueError

        self.max = max
        self.current = start_from

    def __iter__(self):

        return self
    def __next__(self):

        if self.current <=  self.max:
            value = self.current
            self.current += 1

            return value

        else:
            raise StopIteration

it = list(CountUp(7))

print(it) # [0, 1, 2, 3, 4, 5, 6, 7]

for v in CountUp(5):
    print(v)

# 0
# 1
# 2
# 3
# 4
# 5

