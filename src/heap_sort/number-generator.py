import random

numbers = list(range(1000000))

random.shuffle(numbers)

[print(str(x)) for x in numbers]
