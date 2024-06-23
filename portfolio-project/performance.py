import time
import copy

from memory_profiler import memory_usage

from test_data import *
from algos import *

DATA_FIELD_ALGO_NAME = 'Algorithm'
DATA_FIELD_ARRAY_TYPE = 'Array Type'
DATA_FIELD_SIZE = 'Size'
DATA_FIELD_TIME = 'Time'
DATA_FIELD_MEMORY = 'Memory'

# INCLUDE MEM

def measure_performance_with_memory(sort_function, data):
    times = {}
    memories = {}
    for name, arr in data.items():
        copied_arr = arr[:]  # Make a shallow copy to preserve the original for in-place sorting
        start_time = time.time()
        # Capturing memory usage during the function execution
        memory_used = memory_usage((sort_function, (copied_arr,)), max_usage=True, interval=0.1, timeout=200, retval=True)
        elapsed_time = time.time() - start_time
        times[name] = elapsed_time
        memories[name] = memory_used[0] - memory_used[1]  # Subtract initial memory from peak memory
    return times, memories


def print_results_with_memory(results):
    for sort_method, details in results.items():
        print(f"Timings for {sort_method}:")
        for arr_type, metrics in details.items():
            time_taken = metrics[0]
            memory_used = metrics[1]
            try:
              print(f"{arr_type} array: Time: {time_taken:.6f} seconds, Memory: {memory_used:.2f} MiB")
            except Exception:
              print(f"{arr_type} array: {time_taken}")
        print()


def test_collect_results_with_memory(data):
    results = {}
    test_result = []
    for function in [bubble_sort, insertion_sort, merge_sort, quick_sort, heap_sort]:
        function_name = function.__name__
        try:
            times, memories = measure_performance_with_memory(function, data)
            for arr_type in data.keys():
                results[function_name] = (times[arr_type], memories[arr_type])
                test_result.append({
                    DATA_FIELD_ALGO_NAME: function_name,
                    DATA_FIELD_ARRAY_TYPE: arr_type,
                    DATA_FIELD_SIZE: len(data[arr_type]),
                    DATA_FIELD_TIME: times[arr_type],
                    DATA_FIELD_MEMORY: memories[arr_type]
                })
        except Exception as e:
            results[function_name] = {"ERROR": str(e)}
    print_results_with_memory(results)
    return test_result

# NO MEM

def measure_performance(sort_function, data):
    times = {}
    for name, arr in data.items():
        copied_arr = copy.deepcopy(arr)  # Make a deep copy to preserve the original
        start_time = time.time()
        if sort_function.__name__ == 'quick_sort':
            sort_function(copied_arr, 0, len(copied_arr) - 1)
        else:
            sort_function(copied_arr)
        elapsed_time = time.time() - start_time
        times[name] = elapsed_time
    return times


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
  test_result = []
  for function in [bubble_sort, insertion_sort, merge_sort, quick_sort, heap_sort]:
    function_name = function.__name__

    try:
      results[function_name] = measure_performance(function, data)
      for arr_type, time_taken in results[function_name].items():
            test_result.append({
                DATA_FIELD_ALGO_NAME: function.__name__,
                DATA_FIELD_ARRAY_TYPE: arr_type,
                DATA_FIELD_SIZE: len(data[arr_type]),
                DATA_FIELD_TIME: time_taken
            })
    except Exception as e:
      results[function_name] = {"ERROR": str(e)}
  print_results(results)
  return test_result


def do_performance_test(base_sample_size, num_test_sets):
    sample_size = base_sample_size
    test_t1 = time.time()
    test_results = []

    for test_iteration in range(1, num_test_sets+1):
        sample_size *= 2
        t1 = time.time()
        print(f"#### test {test_iteration}: sample size {sample_size} ###########################################################")
        print()
        test_results.extend(test_collect_results(generate_arrays(sample_size)))
        print(f"Iteration {test_iteration} run time: {time.time()-t1}")
        print()

    print(f"Total test duration for base sample size {base_sample_size} and doubling every iteration for {num_test_sets} times: {time.time()-test_t1}s")
    return test_results


def do_performance_test_with_memory(base_sample_size, num_test_sets):
    sample_size = base_sample_size
    test_t1 = time.time()
    test_results = []

    for test_iteration in range(1, num_test_sets+1):
        sample_size *= 2
        t1 = time.time()
        print(f"#### test {test_iteration}: sample size {sample_size} ###########################################################")
        print()
        test_results.extend(test_collect_results_with_memory(generate_arrays(sample_size)))
        print(f"Iteration {test_iteration} run time: {time.time()-t1}")
        print()

    print(f"Total test duration for base sample size {base_sample_size} and doubling every iteration for {num_test_sets} times: {time.time()-test_t1}s")
    return test_results

