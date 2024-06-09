#!/usr/bin/env python3

import time
from algos import *
from performance import *
from test_data import *

def print_results(results):
  for sort_method, timings in results.items():
    print(f"Timings for {sort_method}:")
    for arr_type, time_taken in timings.items():
        try:
          print(f"{arr_type} array: {time_taken:.6f} seconds")
        except Exception:
          print(f"{arr_type} array: {time_taken}")
    print()

def test_collect_results(data):
  results = {}
  for function in [bubble_sort, insertion_sort, merge_sort, quick_sort, heap_sort]:
      try:
        results[function.__name__] = measure_performance(function, data)
      except Exception as e:
        results[function.__name__] = {"ERROR": str(e)}
  return results

if __name__ == "__main__":
  base_sample_size = 50
  sample_size = base_sample_size
  num_test_sets = 10
  test_t1 = time.time()
  for test_iteration in range(1, num_test_sets+1):
    sample_size *= 2
    t1 = time.time()
    print(f"#### test {test_iteration}: sample size {sample_size} ###########################################################")
    print()
    print_results(test_collect_results(generate_arrays(sample_size)))
    print(f"Iteration {test_iteration} run time: {time.time()-t1}")
    print()
  print(f"Total Test Duration: {time.time()-test_t1}s")
