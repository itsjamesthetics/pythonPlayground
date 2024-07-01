import csv
import pandas as pd

# Function to fill missing values with forward fill
def fill_missing_with_forward_fill(df):
    return df.ffill()

# Define the input and output file names
input_file = 'input.csv'
output_file = 'output.csv'

try:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)
except FileNotFoundError:
    print(f"File '{input_file}' not found.")
    exit(1)

# Fill missing values using forward fill
df_filled = fill_missing_with_forward_fill(df)

# Save the modified data to a new CSV file
df_filled.to_csv(output_file, index=False)
print(f"Data with missing values filled using forward fill saved to '{output_file}'.")
