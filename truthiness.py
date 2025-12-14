
def myfunc(value: int | None  = None):

    if value:

        return value
    return "no value"

print(myfunc(12)) ## 12


print(myfunc(0)) ## None # even though it has value 0


def robost(value:int | None = None):

    if value is not None:
        return value
    return "no value"


print(robost(12)) ## 12

print(robost(0)) ## 0
