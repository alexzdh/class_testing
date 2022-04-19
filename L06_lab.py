#fix the problems with each of these classes (1-3)

#1
class MyClass():
    def __init__(self, a, b):
        self.a = 10
        self.b = 20
        self.x = self.a + self.b
my_instance = MyClass()
my_instance.x

#2
class MyClass():
    def __init__(self):
        a = 10
        b = 20
        self.x = a + b
my_instance = MyClass()
my_instance.x

#3
class MyClass():
    def __init__(self, a, b):
        self.x = a + b
my_instance = MyClass(10, 20)
my_instance.x

#4 A Fibonacci sequence is a list of values where each is the sum of the previous
#  two, e.g. [0, 1, 1, 2, 3].
#      - First write a function that takes in a list of any two values, then
#        calculates the rest of the sequence starting from that point.  It
#        should have two arguments; the starting list, and the number to
#        calculate.
#      - Second, turn this into a class that takes the same list at start,
#        but has a method that takes N as an argument and then calculates
#        the sequence.
#  Note that technically the Fibonacci sequence starts at 0, but for our
#  coding practice we can calculate it from any two starting values.

def fib_func(start_list, a):
    if type(start_list) == list and len(start_list) == 2:
        current_index = 2
        while len(start_list) < a:
            start_list.append(start_list[current_index - 2] + start_list[current_index - 1])
            current_index += 1
    return start_list

print(fib_func([1, 2], 8))


class FibClass():
    def __init__(self, start_list):
        self.start_list = start_list

    def fib_calc(self, N):
        start_list = self.start_list
        if type(start_list) == list and len(start_list) == 2:
            current_index = 2
            while len(start_list) < N:
                start_list.append(start_list[current_index - 2] + start_list[current_index - 1])
                current_index += 1
        print(start_list)
        
        
print(FibClass([1, 2]).fib_calc(8))




