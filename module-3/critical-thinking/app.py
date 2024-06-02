#!/usr/bin/env python3

import time
import random
import string

class PatientRecord:
    """
    Class representing a patient record.
    """
    def __init__(self, patient_id, name, age):
        """
        Initializes a new patient record.
        
        Args:
            patient_id (int): Unique identifier for the patient.
            name (str): Name of the patient.
            age (int): Age of the patient.
        """
        self.patient_id = patient_id
        self.name = name
        self.age = age

    def __lt__(self, other):
        """
        Compares this patient record to another based on name and age.
        
        Args:
            other (PatientRecord): Another patient record.
        
        Returns:
            bool: True if this patient's name is less than the other patient's name, 
                  or if names are equal and this patient's age is less than the other patient's age.
        """
        if self.name == other.name:
            return self.age < other.age
        return self.name < other.name

    def __repr__(self):
        """
        Returns a string representation of the patient record.
        
        Returns:
            str: String representation of the patient record.
        """
        return f"PatientRecord({self.patient_id}, {self.name}, {self.age})"

def bubble_sort(records):
    """
    Sorts a list of patient records using Bubble Sort algorithm.
    
    Args:
        records (list of PatientRecord): List of patient records to sort.
    """
    n = len(records)
    for i in range(n):
        for j in range(0, n-i-1):
            if records[j] > records[j+1]:
                records[j], records[j+1] = records[j+1], records[j]

def merge_sort(records):
    """
    Sorts a list of patient records using Merge Sort algorithm.
    
    Args:
        records (list of PatientRecord): List of patient records to sort.
    """
    if len(records) > 1:
        mid = len(records) // 2
        left_half = records[:mid]
        right_half = records[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                records[k] = left_half[i]
                i += 1
            else:
                records[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            records[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            records[k] = right_half[j]
            j += 1
            k += 1

def generate_random_name():
    """
    Generates a random name.
    
    Returns:
        str: Randomly generated name.
    """
    first_name = ''.join(random.choices(string.ascii_uppercase, k=1)) + ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 7)))
    last_name = ''.join(random.choices(string.ascii_uppercase, k=1)) + ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))
    return f"{first_name} {last_name}"

def generate_patient_records(num_records):
    """
    Generates a list of random patient records.
    
    Args:
        num_records (int): Number of patient records to generate.
    
    Returns:
        list of PatientRecord: List of randomly generated patient records.
    """
    records = []
    for i in range(num_records):
        patient_id = random.randint(1, 10000)
        name = generate_random_name()
        age = random.randint(1, 100)
        records.append(PatientRecord(patient_id, name, age))
    return records

def compare_sorting_algorithms(num_records):
    """
    Compares the performance of Bubble Sort and Merge Sort algorithms.
    
    Args:
        num_records (int): Number of patient records to sort.
    """
    records = generate_patient_records(num_records)

    # Bubble Sort
    bubble_sort_records = records.copy()
    start_time = time.time()
    bubble_sort(bubble_sort_records)
    bubble_sort_time = time.time() - start_time

    # Merge Sort
    merge_sort_records = records.copy()
    start_time = time.time()
    merge_sort(merge_sort_records)
    merge_sort_time = time.time() - start_time

    print(f"Sorting {num_records} patient records:")
    print(f"Bubble Sort took {bubble_sort_time:.6f} seconds")
    print(f"Merge Sort took {merge_sort_time:.6f} seconds")

if __name__ == "__main__":
    compare_sorting_algorithms(50)
    compare_sorting_algorithms(100)
    compare_sorting_algorithms(200)
    compare_sorting_algorithms(400)
    compare_sorting_algorithms(800)
    compare_sorting_algorithms(1600)
    compare_sorting_algorithms(3200)
    compare_sorting_algorithms(6400)
