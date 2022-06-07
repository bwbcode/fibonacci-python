# python iteration.py <SERIES_LENGTH>

import sys

def fibonacci_iteration(length):
    sequence = [0, 1]
    if length > 2:
        while length > 2: # Length is -2 as the sequence already contains 1st two Fibonacci numbers
            n = len(sequence)
            length = length - 1
            sequence.append(sequence[n-1] + sequence[n-2])

        print(sequence)
    else:
        print('The minimum length of a sequence is 2:','\n',sequence)

try:
    fibonacci_iteration(int(sys.argv[1]))
except:
    print('The series length submitted is not an integer')