import csv
import re

input_filename = 'FinalData.csv'
output_filename = 'NewFinalData.csv'

pattern = r'\|(\d+)/(\d+)\|'

with open(input_filename, 'r') as input_file, open(output_filename, 'w', newline = '') as output_file:
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)

    for row in csv_reader:
        new_row = []
        for item in row:
            matches = re.search(pattern, item)
            if matches:
                number1 = int(matches.group(1))
                number2 = int(matches.group(2))
                new_row.append(number1)
                new_row.append(number2)
            else:
                new_row.append(item)  # Append the item as-is if it doesn't match the pattern
        csv_writer.writerow(new_row)