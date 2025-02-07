import random


def generate_array(size: int) -> list:
    arr = []

    for _i in range(size):
        arr.append(random.randrange(0, 6))
    
    return arr


def sort_array(array_to_sort: list) -> list:
    # Sorting by choice

    for i in range(len(array_to_sort)):
        smallest = array_to_sort[i]
        smallest_idx = i

        for j in range(i+1, len(array_to_sort)):
            if array_to_sort[j] < smallest:
                smallest = array_to_sort[j]
                smallest_idx = j
        
        temp = array_to_sort[i]
        array_to_sort[i] = array_to_sort[smallest_idx]
        array_to_sort[smallest_idx] = temp


def count_elements(number: int, list: list[int]) -> int:
    counter = 0

    for el in list:
        if el == number:
            counter += 1
    
    return counter


arr = generate_array(20)
print("Original array:")
print(arr)

print("\nAfter sort:")
sort_array(arr)
print(arr)

print("\nElements count:")
for i in range(6):
    print(f"\"{i}\" - {count_elements(i, arr)}")
