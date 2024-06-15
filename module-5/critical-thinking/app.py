#!/usr/bin/env python3

import time
import math

from randomize import generate_random_users
from hashtable import UserHashTable
from binarysearch import BinarySearchArray

def benchmark(data_structure, users, structure_name):
    print()
    print(f"Benchmarking {structure_name}")

    insert_time = time.time()
    for user in users:
        data_structure.insert(user)
    insert_duration = time.time() - insert_time
    print(f"Time to insert users: {insert_duration:.5f} seconds")

    search_time = time.time()
    for user in users:
        found_user = data_structure.find(user.username, user.email)
    search_duration = time.time() - insert_time
    print(f"Time to search users: {search_duration:.5f} seconds")

    delete_time = time.time()
    for user in users:
        data_structure.delete(user.username, user.email)
    delete_duration = time.time() - insert_time
    print(f"Time to delete users: {delete_duration:.5f} seconds")

    additional_users = generate_random_users(100)
    additional_insert_time = time.time()
    for user in additional_users:
        data_structure.insert(user)
    additional_insert_duration = time.time() - additional_insert_time
    print(f"Time to insert additional users: {additional_insert_duration:.5f} seconds")

    return insert_duration, search_duration, delete_duration, additional_insert_duration

def main():
    # Generate random user profiles
    num_users = 100
    num_iterations = 10
    for i in range(num_iterations):
        print(f"Test Iteration {i}: sample size {num_users} #########################################")
        users = generate_random_users(num_users)

        # Create instances of HashTable and BinarySearchTree
        hash_table = UserHashTable(int(math.ceil(num_users / 0.75))) # maintain a load factor of 0.75
        user_array = BinarySearchArray()

        insert_time, search_time, delete_time, additional_insert_duration = benchmark(hash_table, users, "Hashtables")
        insert_time2, search_time2, delete_time2, additional_insert_duration2 =  benchmark(user_array, users, "Binary Search")

        print()
        print(f"BST time complexity over hashtables sample size ({num_users}):")
        print(f"insert {(insert_time2/insert_time)*100:.2f}%")
        print(f"search {(search_time2/search_time)*100:.2f}%")
        print(f"delete {(delete_time2/delete_time)*100:.2f}%")
        print(f"additional insert {(additional_insert_duration2/additional_insert_duration)*100:.2f}%")
        num_users *= 2

if __name__ == "__main__":
    main()
