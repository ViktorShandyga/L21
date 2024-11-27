'''class Iterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        word = self.words[self.index]
        self.index += 1
        return len(word)

words = ["apple", "banana", "cat", "automobile"]
iterator = Iterator(words)

for length in iterator:
    print(length)'''

'''class Iterator:
    def __init__(self, max_power):
        self.current = 0
        self.max_power = max_power

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_power:
            raise StopIteration
        result = 2 ** self.current
        self.current += 1
        return result

iterator = Iterator(10)
for value in iterator:
    print(value)'''

'''class Iterator:
    def __init__(self, max_power):
        self.current = 0
        self.max_power = max_power

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_power:
            raise StopIteration
        result = 3 ** self.current
        self.current += 1
        return result

iterator = Iterator(10)
for value in iterator:
    print(value)'''

'''import random
import string

def random_letter_generator():
    while True:
        yield random.choice(string.ascii_letters)

generator = random_letter_generator()

for _ in range(10):
    print(next(generator))'''

'''def sum_closure():
    total = 0

    def adder(value):
        nonlocal total
        total += value
        return total

    return adder

sum_closure = sum_closure()

print(sum_closure(15))
print(sum_closure(5))
print(sum_closure(20))'''

'''def create_adder(additional_value):
    def adder(value):
        return value + additional_value
    return adder

add_ten = create_adder(10)
add_twenty = create_adder(20)

print(add_ten(3))
print(add_ten(7))

print(add_twenty(3))
print(add_twenty(7))'''

