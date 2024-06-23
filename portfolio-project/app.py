#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

from performance import *


def plot_results(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    for name, group in df.groupby(DATA_FIELD_ALGO_NAME):
        group.groupby(DATA_FIELD_ARRAY_TYPE).plot(x=DATA_FIELD_SIZE, y=DATA_FIELD_TIME, ax=ax, label=f'{name} Time', marker='o')
    plt.title('Performance of Sorting Algorithms')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.legend(title='Algorithm')
    plt.grid(True)
    plt.show()


def main():
  test_results = do_performance_test(50, 10)
  # test_results = do_performance_test_with_memory(50, 4)

  df = pd.DataFrame(test_results)
  df.to_csv('sort_performance.csv', index=False)
  plot_results(df)


if __name__ == "__main__":
  main()
