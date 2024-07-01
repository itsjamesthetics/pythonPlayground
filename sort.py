import numpy as np

# Function for equal width binning
def equal_width_binning(data, num_bins):
    # Calculate bin width
    bin_width = (max(data) - min(data)) / num_bins
    # Create bins
    bins = [min(data) + i * bin_width for i in range(num_bins + 1)]
    # Digitize data into bins and round up to the nearest whole number
    binned_data = np.ceil(np.digitize(data, bins, right=True))
    return bins, binned_data

# Function for equal frequency binning
def equal_frequency_binning(data, num_bins):
    # Calculate indices to split data into equal frequency bins
    bin_indices = np.linspace(0, len(data), num_bins + 1).astype(int)
    # Sort data and assign bin boundaries
    sorted_data = np.sort(data)
    bins = [sorted_data[i] for i in bin_indices]
    # Digitize data into bins and round up to the nearest whole number
    binned_data = np.ceil(np.digitize(data, bins, right=True))
    return bins, binned_data

# Function for smoothing by means
def smoothing_by_means(data, bin_indices, num_bins):
    # Calculate the mean for each bin
    bin_means = [np.mean([data[i] for i in range(len(data)) if bin_indices[i] == bin_num]) for bin_num in range(1, num_bins + 1)]
    # Smooth the data using bin means
    smoothed_data = [bin_means[int(bin_indices[i]) - 1] for i in range(len(data))]
    return smoothed_data

# Function for smoothing by boundaries
def smoothing_by_boundaries(data):
    # Smooth the data using median
    smoothed_data = np.median(data)
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
    num_data = int(input("Enter the number of data points: "))
    data = [float(input(f"Enter data {i + 1}: ")) for i in range(num_data)]

    print("\nChoose binning method:")
    print("1. Equal Width Binning")
    print("2. Equal Frequency Binning")
    binning_method = int(input("Enter 1 or 2: "))

    if binning_method == 1:
        num_bins = int(input("Enter the number of bins for Equal Width Binning: "))
        bins, bin_indices = equal_width_binning(data, num_bins)
    elif binning_method == 2:
        num_bins = int(input("Enter the number of bins for Equal Frequency Binning: "))
        bins, bin_indices = equal_frequency_binning(data, num_bins)
    else:
        print("Invalid binning method selected.")
        exit(1)

    print("\nChoose smoothing method:")
    print("1. Smoothing by Means")
    print("2. Smoothing by Boundaries")
    print("3. Smoothing by Median")
    smoothing_method = int(input("Enter 1, 2, or 3: "))

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

    print(f"\nPartition into {num_bins} Equal Width Bins:")
    for i in range(num_bins):
        bin_start = bins[i]
        bin_end = bins[i + 1]
        bin_data = [data[j] for j in range(len(data)) if int(bin_indices[j]) == i + 1]
        print(f"Bin {i + 1}: {bin_start} - {bin_end} {bin_data}")

    print("\nBinned Data (Indices):", bin_indices.tolist())  # Convert bin_indices to a list
    print("Smoothed Data:", smoothed_data)
    print("Sorted Data:", sorted_data)

    # Adding feedback based on dataset size
    if num_data >= 2 and num_data <= 9:
        print("\nThis is a small dataset.")
    elif num_data >= 10 and num_data <= 50:
        print("\nThis is a medium-sized dataset.")
    else:
        print("\nThis is a large dataset.")
