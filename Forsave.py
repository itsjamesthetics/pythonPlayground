'''
    Developed by: James Ald Teves
    BS Computer Science
    Instructor: Dr. Chuchi S. Montenegro

    A Python Program that simulates Binning which performs Equal Width Binning and Equal Frequency Binning.
    Also Partitions into any Bins the user wants demonstrates Smoothing by Means, Boundaries, and Median.
'''
import numpy as np

# Modify the equal_width_binning function to use numpy.floor for binning
def equal_width_binning(data, num_bins):
    # Calculate bin width
    bin_width = (max(data) - min(data)) / num_bins
    # Create bins, rounding up to the nearest whole number
    bins = [int(np.floor(min(data))) + i * int(np.ceil(bin_width)) for i in range(num_bins + 1)]
    # Digitize data into bins and round down to the nearest whole number
    binned_data = np.ceil(np.digitize(data, bins, right=False))
    return bins, binned_data

# Function for equal frequency binning
def equal_frequency_binning(data, num_bins):
    # Calculate indices to split data into equal frequency bins
    bin_indices = np.linspace(0, len(data), num_bins + 1).astype(int)
    # Sort data
    sorted_data = np.sort(data)
    bins = []  # Initialize an empty list for bin boundaries
    prev_idx = 0  # Initialize the previous index
    for idx in bin_indices[1:]:  # Iterate over bin indices
        if prev_idx >= len(sorted_data):
            break
        bin_boundary = sorted_data[min(idx, len(sorted_data) - 1)]  # Ensure the index is within bounds
        bins.append(int(np.ceil(bin_boundary)))  # Round up to the nearest whole number
        prev_idx = idx
    # Digitize data into bins and round up to the nearest whole number
    binned_data = np.ceil(np.digitize(data, bins, right=True))
    return bins, binned_data

''' 
# Function for smoothing by means
def smoothing_by_means(data, bin_indices, num_bins):
    # Calculate the mean for all the data
    #bin_means = [np.mean([data[i] for i in range(len(data)) if bin_indices[i] == bin_num]) for bin_num in range(1, num_bins + 1)]
    #smoothed_data = [bin_means[int(bin_indices[i]) - 1] for i in range(len(data))]
    #smoothed_data = [np.sum([data[i - 1], data[i], data[i + 1]]) if 0 < i < len(data) - 1 else data[i] for i in range(len(data))/num_data]
    #smoothed_data = [np.sum([data[i - 1], data[i], data[i + 1]]) if 0 < i < len(data) - 1 else data[i] for i in range(len(data))/num_data]
    smoothed_data = [np.sum((data)/num_data[i] for i in range (len(data)) if bin_indices[i] == bin_num) for bin_num in range(1, numb_bins + 1)]
    return smoothed_data

    # Function for smoothing by means
def smoothing_by_means(data, bin_indices, num_bins):
    smoothed_data = [np.sum([data[i] for i in range(len(data))]) / len([data[i] for i in range(len(data))]) for num_data in range(1, num_bins + 1)]
    return smoothed_data
'''
'''
# Function for smoothing by boundaries
def smoothing_by_boundaries(data):
    # Smooth the data using median
    smoothed_data = [np.median([data[i - 1], data[i], data[i + 1]]) if 0 < i < len(data) - 1 else data[i] for i in range(len(data))]
    return smoothed_data
'''

def smoothing_by_means(data, bin_indices, num_bins):
    smoothed_data = np.sum(data) / len(data)
    return [smoothed_data] * len(data)

def smoothing_by_boundaries(data, window_size=3):
    smoothed_data = []
    for i in range(len(data)):
        start_idx = max(0, i - (window_size - 1) // 2)
        end_idx = min(len(data), i + (window_size - 1) // 2 + 1)
        window_data = data[start_idx:end_idx]
        median_value = np.median(window_data)
        smoothed_data.append(median_value)
    return smoothed_data

def smoothing_by_means(data, bin_indices, num_bins):
    smoothed_data = []
    for bin_num in range(1, num_bins + 1):
        bin_data = [data[i] for i in range(len(data)) if bin_indices[i] == bin_num]
        if bin_data:
            bin_mean = np.mean(bin_data)
            smoothed_data.extend([bin_mean] * len(bin_data))
        else:
            smoothed_data.extend([0] * len(bin_data))  # Handle empty bins
    return smoothed_data

# Function for smoothing by median
def smoothing_by_median(data):
    smoothed_data = [np.median([data[i - 1], data[i], data[i + 1]]) if 0 < i < len(data) - 1 else data[i] for i in range(len(data))]
    return smoothed_data

# Function to sort data
def sort_data(data):
    sorted_data = np.sort(data)
    return sorted_data

if __name__ == "__main__":
    num_data = int(input("\n\t\t Enter the number of data points: "))
    data = [float(input(f"\t Input Data {i + 1}: ")) for i in range(num_data)]

    print("\n\t Choose binning method:")
    print("\t 1. Equal Width Binning")
    print("\t 2. Equal Frequency Binning")
    binning_method = int(input("\n\t Enter 1 or 2: "))

    if binning_method == 1:
        num_bins = int(input("\n\t Enter the number of bins for Equal Width Binning: "))
        bins, bin_indices = equal_width_binning(data, num_bins)
    elif binning_method == 2:
        num_bins = int(input("\n\t Enter the number of bins for Equal Frequency Binning: "))
        bins, bin_indices = equal_frequency_binning(data, num_bins)
    else:
        print("Invalid binning method selected.")
        exit(1)

    print("\n\t Choose smoothing method:")
    print("\t 1. Smoothing by Means")
    print("\t 2. Smoothing by Boundaries")
    print("\t 3. Smoothing by Median")
    smoothing_method = int(input("\t Enter 1, 2, or 3: "))

    if smoothing_method == 1:
        smoothed_data = smoothing_by_means(data, bin_indices, num_bins)
    elif smoothing_method == 2:
        smoothed_data = smoothing_by_boundaries(data)
    elif smoothing_method == 3:
        smoothed_data = smoothing_by_median(data)
    else:
        print("Invalid smoothing method selected.")
        exit(1)

    sorted_data = sort_data(data)  # Sort the original data

    print(f"\n\t Partition into {num_bins} Equal Width Bins:")
    for i in range(num_bins):
        bin_start = bins[i]
        bin_end = bins[i + 1] if i < num_bins - 1 else max(data)  # Adjust for the last bin
        bin_data = [data[j] for j in range(len(data)) if int(bin_indices[j]) == i + 1]
        print(f"\t Bin {i + 1}:  {bin_start} - {bin_end}  {bin_data}")

    print("\n\t Binned Data (Indices):", bin_indices.tolist())  # Convert bin_indices to a list
    print("\t Smoothed Data:", smoothed_data)
    print("\t Sorted Data:", sorted_data)

    # Adding feedback based on dataset size
    if num_data >= 2 and num_data <= 9:
        print("\n\t This is a small dataset.")
    elif num_data >= 10 and num_data <= 50:
        print("\n\t This is a medium-sized dataset.")
    else:
        print("\n\t This is a large dataset.")