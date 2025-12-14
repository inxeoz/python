def pause_resume():

    yield 1
    yield 2


for v in pause_resume():

    print(v)

# 1
# 2


print(pause_resume()) #<generator object pause_resume at 0x7f7777958930>

it = pause_resume()

print(next(it)) # 1

print(next(it)) # 2

print(next(it)) # StopIteration

## yield turns a normal function into a generator.


