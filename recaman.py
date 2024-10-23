L = int(input("Length of sequence: ")) # this should be your only input
sequence = [0]

for k in range(1, L):
    prev_value = sequence[k-1]

    next_value = prev_value - k
    if next_value > 0 and next_value not in sequence: 
        sequence.append(next_value)
    else:
        sequence.append(prev_value + k)

for item in sequence:
    print(item, end=" ")