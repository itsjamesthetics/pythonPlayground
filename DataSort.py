'''
    Developed by: James Ald Teves
    BS Computer Science
    Instructor: Dr. Chuchi S. Montenegro

    Description: A python program that asks the user to input Digits
    Asks the user what type of Binning and Smoothing method used and
    Lastly, sort the Data. 
'''

import numpy as np

def equal_width_binning(data, num_bins):
    bin_width = (max(data) - min(data)) / num_bins
    bins = [min(data) + i * bin_width for i in range(num_bins + 1)]
    binned_data = np.digitize(data, bins)
    return bins, binned_data  # Return both bins and binned data

def equal_frequency_binning(data, num_bins):
    bin_indices = np.linspace(0, len(data), num_bins + 1).astype(int)
    bins = np.sort(data)[bin_indices]
    bin_indices = np.digitize(data, bins)
    return bins, bin_indices

def smoothing_by_means(data, num_bins):
    #total_sum = np.sum(data)
    sum_sorted_data = np.sum(data)
    smoothed_data = sum_sorted_data/ num_data
    return smoothed_data

def smoothing_by_boundaries(data):
    smoothed_data = np.median(data)
    return smoothed_data

def smoothing_by_median(data):
    smoothed_data = [np.median([data[i - 1], data[i], data[i + 1]]) if 0 < i < len(data) - 1 else data[i] for i in range(len(data))]
    return smoothed_data

def sort_data(data):
    sorted_data = np.sort(data)
    return sorted_data

if __name__ == "__main__":
    num_data = int(input("Enter the number of datas: "))
    data = [float(input(f"Enter data {i + 1}: ")) for i in range(num_data)]

    print("\nChoose binning method:")
    print("1. Equal Width Binning")
    print("2. Equal Frequency Binning")
    binning_method = int(input("Enter 1 or 2: "))

    if binning_method == 1:
        num_bins = int(input("Enter the number of bins for Equal Width Binning: "))
        bins, binned_data = equal_width_binning(data, num_bins)
    elif binning_method == 2:
        num_bins = int(input("Enter the number of bins for Equal Frequency Binning: "))
        bins, binned_data = equal_frequency_binning(data, num_bins)
    else:
        print("Invalid binning method selected.")
        exit(1)

    print("\nChoose smoothing method:")
    print("1. Smoothing by Means")
    print("2. Smoothing by Boundaries")
    print("3. Smoothing by Median")
    smoothing_method = int(input("Enter 1, 2, or 3: "))

    if smoothing_method == 1:
        smoothed_data = smoothing_by_means(data, num_bins)
    elif smoothing_method == 2:
        smoothed_data = smoothing_by_boundaries(binned_data)
    elif smoothing_method == 3:
        smoothed_data = smoothing_by_median(binned_data)
    else:
        print("Invalid smoothing method selected.")
        exit(1)

    sorted_data = sort_data(data)  # Sort the original data

    print(f"\nPartition into {num_bins} Equal Width Bins:")
    for i in range(num_bins):
        bin_start = bins[i]
        bin_end = bins[i + 1]
        bin_data = [data[j] for j in range(len(data)) if binned_data[j] == i + 1]
        print(f"Bin {i + 1}: {bin_start} - {bin_end} {bin_data}")

    print("Binned Data (Indices):", binned_data.tolist())  # Convert binned_data to a list
    print("Smoothed Data:", smoothed_data)
    print("Sorted Data:", sorted_data)

    # Adding feedbacks
    if num_data >= 2 and num_data <= 9:
        print("This is a small dataset.")
    elif num_data >= 10 and num_data <= 50:
        print("This is a medium-sized dataset.")
    else:
        print("This is a large dataset.")
