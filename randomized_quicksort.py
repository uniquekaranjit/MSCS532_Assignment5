# ----------------------------------------------------------------------------------------------------------------------
# Driver Code to analyze and compare randomized quicksort with deterministic quick sort (first element as pivot) 
# Author: Unique Karanjit
# Feb 2, 2025 
# This code is pulled from Assignment3 @Unique Karanjit
# ----------------------------------------------------------------------------------------------------------------------

#Increase necessary dependencies. 
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import sys

# Increase recursion limit to handle larger inputs
sys.setrecursionlimit(10**6)

# ----------------------------------------------------------------------------------------------------------------------
# Funtion Declarations 
# ----------------------------------------------------------------------------------------------------------------------


# Deterministic Quicksort (pivot is the first element)
def deterministic_quicksort(arr):
    if len(arr) <= 1: # is the array size is 1, the array is already sorted, so return. 
        return arr
    pivot = arr[0] # choose pivot as first element. 
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quicksort(left) + middle + deterministic_quicksort(right) # recursive call until sorted. 

# Randomized Quicksort (pivot chosen randomly)
def randomized_quicksort(arr):
    if len(arr) <= 1: # is the array size is 1, the array is already sorted, so return. 
        return arr
    pivot_idx = np.random.randint(len(arr))
    pivot = arr[pivot_idx] # choose random pivot element. 
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + middle + randomized_quicksort(right) # recursive call until sorted. 

# Helper function to generate test cases
def generate_test_cases(size):
    random_array = [random.randint(0, 5000) for _ in range(size)] # generate random array
    sorted_array = sorted(random_array) # generate sorted array
    reverse_sorted_array = sorted_array[::-1] # generate reverse sorted array
    repeated_elements = [random.randint(0, 100) for _ in range(size)] # generate array with repeated elements. 
    return [random_array, sorted_array, reverse_sorted_array, repeated_elements]

# Measure runtime of a sorting algorithm
def measure_runtime(sort_function, arr):
    start_time = time.time()
    sort_function(arr.copy())  # Use a copy to avoid modifying the original array
    end_time = time.time()
    return end_time - start_time


# ----------------------------------------------------------------------------------------------------------------------
# Driver Code 
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    # Define input sizes for testing
    sizes = [500, 1000, 2500, 5000, 20000, 50000, 100000, 250000]

    # Define case labels
    case_labels = [
        "Randomly generated arrays",
        "Already sorted arrays",
        "Reverse-sorted arrays",
        "Arrays with repeated elements"
    ]

    # Collect runtime data
    results_deterministic = {case: [] for case in case_labels}
    results_randomized = {case: [] for case in case_labels}

    # Run experiments
    for size in sizes:
        test_cases = generate_test_cases(size) # generate test case for each size. 
        for i, case_label in enumerate(case_labels):
            array = test_cases[i]
            results_deterministic[case_label].append(measure_runtime(deterministic_quicksort, array))
            results_randomized[case_label].append(measure_runtime(randomized_quicksort, array))

    print("Runtime Results for Sorted Arrays:")
    for size in sizes:
        print(f"\nSize: {size}")
        print(f"Deterministic Quicksort (Sorted):         {results_deterministic['Already sorted arrays'][sizes.index(size)]:.6f} seconds")
        print(f"Randomized Quicksort (Sorted):            {results_randomized['Already sorted arrays'][sizes.index(size)]:.6f} seconds")

        print(f"Deterministic Quicksort (Random):         {results_deterministic['Randomly generated arrays'][sizes.index(size)]:.6f} seconds")
        print(f"Randomized Quicksort (Random):            {results_randomized['Randomly generated arrays'][sizes.index(size)]:.6f} seconds")

        print(f"Deterministic Quicksort (Reverse-Sorted): {results_deterministic['Reverse-sorted arrays'][sizes.index(size)]:.6f} seconds")
        print(f"Randomized Quicksort (Reverse-Sorted):    {results_randomized['Reverse-sorted arrays'][sizes.index(size)]:.6f} seconds")

        print(f"Deterministic Quicksort (Repeated):       {results_deterministic['Arrays with repeated elements'][sizes.index(size)]:.6f} seconds")
        print(f"Randomized Quicksort (Repeated):          {results_randomized['Arrays with repeated elements'][sizes.index(size)]:.6f} seconds")

        print("---------------------------------------------")


    # Plot results
    plt.figure(figsize=(12, 8))
    for case_label in case_labels:
        plt.plot(sizes, results_deterministic[case_label], label=f"Deterministic ({case_label})", marker='o')
        plt.plot(sizes, results_randomized[case_label], label=f"Randomized ({case_label})", marker='x')

    plt.title("Running Time: Randomized Quicksort vs Deterministic Quicksort", fontsize=16)
    plt.xlabel("Input Size", fontsize=14)
    plt.ylabel("Time (seconds)", fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.show()

