L = int(input())  # Only take the integer input for length

sequence = [0]  # Start the sequence with 0

for k in range(1, L):  # Loop starting from 1 up to the length
    prev_value = sequence[k-1]  # Previous value in the sequence
    next_value = prev_value - k  # Try subtracting k

    # Check if next_value is positive and not in the sequence
    if next_value > 0 and next_value not in sequence:
        sequence.append(next_value)
    else:
        sequence.append(prev_value + k)  # Otherwise, add k to prev_value

# Print the sequence as a single line of space-separated integers
print(sequence)
