import random

# Generating test data
def generate_arrays(size=1000):
    random_arr = [random.randint(0, size) for _ in range(size)]
    sorted_arr = sorted(random_arr)
    reverse_arr = sorted_arr[::-1]
    nearly_sorted_arr = sorted_arr[:]
    few_swaps = int(0.1 * size)
    for _ in range(few_swaps):
        i, j = random.randint(0, size-1), random.randint(0, size-1)
        nearly_sorted_arr[i], nearly_sorted_arr[j] = nearly_sorted_arr[j], nearly_sorted_arr[i]
    few_unique_arr = [random.choice([0, 1, 2, 3, 4]) for _ in range(size)]
    return {
        "random": random_arr,
        "sorted": sorted_arr,
        "reverse": reverse_arr,
        "nearly sorted": nearly_sorted_arr,
        "few unique": few_unique_arr
    }
