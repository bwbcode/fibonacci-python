n = 7
sequence = [0, 1]

while n > 2:
    length = len(sequence)
    n = n - 1
    sequence.append(sequence[length-1] + sequence[length-2])

print(sequence)