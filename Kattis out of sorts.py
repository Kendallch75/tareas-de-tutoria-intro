def generate_sequence(n, m, a, c, x):
    sequence = []
    current_value = (x * a + c) % m
    for _ in range(n):
        sequence.append(current_value)
        current_value = (current_value * a + c) % m
    return sequence

def binary_search(array, target):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False
  
n, m, a, c, x = map(int, input().split())
sequence = generate_sequence(n, m, a, c, x)
count_found = sum(1 for number in sequence if binary_search_unsorted(sequence, number))
print(count_found)
