'''
    Developed by: James Ald Teves
    BS Computer Science
    
    Instructor: Dr. Chuchi Montenegro
    Description: Python Program that can read and manipulate CSV Data
'''

import csv
import pandas as pd

# Function to fill missing values with column average
def fill_missing_with_average(df):
    return df.fillna(df.mean())

# Function to fill missing values using linear interpolation
def fill_missing_with_interpolation(df):
    return df.interpolate()

# Function to fill missing values with a global constant (0)
def fill_missing_with_constant(df, constant=0):
    return df.fillna(constant)

# Define the input and output file names
input_file = 'Datasamp.csv'
output_file = 'NewDataSet.csv'

try:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)
except FileNotFoundError:
    print(f"File '{input_file}' not found.")
    exit(1)

# Ask the user for filling method
print("Choose a method to fill in missing data:")
print("(1) Remove rows with missing data")
print("(2) Fill by column average")
print("(3) Fill by linear interpolation")
print("(4) Fill by global constant (0)")

fill_method = input("Enter the number corresponding to your choice: ")

# Check if the chosen method is valid
if fill_method in ['1', '2', '3', '4']:
    if fill_method == '1':
        # Remove rows with missing data
        df_filled = df.dropna()
    elif fill_method == '2':
        # Fill missing values with column averages
        df_filled = fill_missing_with_average(df)
    elif fill_method == '3':
        # Fill missing values using linear interpolation
        df_filled = fill_missing_with_interpolation(df)
    else:
        # Fill missing values with a global constant (0)
        constant = float(input("Enter the global constant value: "))
        df_filled = fill_missing_with_constant(df, constant)

    # Save the modified data to a new CSV file
    df_filled.to_csv(output_file, index = False)
    print(f"Data with missing values filled using method {fill_method} saved to '{output_file}'.")
else:
    print("Invalid choice. Please enter 1, 2, 3, or 4 for the fill method.")