def find_min_max(arr):
    if not arr:
        return None, None 
    minimum = maximum = arr[0]

    for num in arr[1:]:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num
    return minimum, maximum

numbers = [12, 3, 7, 9, 1, 25, 6]
min_val, max_val = find_min_max(numbers)
print(f"Minimum: {min_val}, Maximum: {max_val}")
