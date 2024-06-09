import time
import copy

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