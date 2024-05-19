#!/usr/bin/env python3

import time
import random

# Generate a large list of items (simulating an online marketplace database)
num_items = 10**6
marketplace = [random.randint(1, num_items * 10) for _ in range(num_items)]
cache = {}

def cache_item_index(item, index):
    cache[item] = index
    
def cache_get_item(item):
    return cache[item]

# Linear search function
def linear_search(data, target):
    for index, item in enumerate(data):
        if item == target:
            return index
    return -1

# Simulate searching for an item in the marketplace
target_item = random.choice(marketplace)

# Measure the time taken for the first search (cold cache)
start_time = time.time()
result_index = linear_search(marketplace, target_item)
end_time = time.time()
print(f"First search (cold cache): Item found at index {result_index}, Time taken: {end_time - start_time:.6f} seconds")

# caching item
cache_item_index(target_item, result_index)

# Simulate caching by searching the same item again (warm cache)
start_time = time.time()
result_index = cache_get_item(target_item)
if result_index == None or result_index < 0:
    result_index = linear_search(marketplace, target_item)
end_time = time.time()
print(f"Second search (warm cache): Item found at index {result_index}, Time taken: {end_time - start_time:.6f} seconds")

# Perform a search for an item not in the list (worst case scenario)
non_existent_item = num_items * 10 + 1
start_time = time.time()
result_index = linear_search(marketplace, non_existent_item)
end_time = time.time()
print(f"Worst case search: Item found at index {result_index}, Time taken: {end_time - start_time:.6f} seconds")
