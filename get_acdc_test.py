import csv

filename = 'acdc.txt'
output_filename = 'outputs/acdc.csv'

categories = []
values = []

with open(filename, 'r') as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    if line:
        category, value = line.split('\t')
        categories.append(category)
        values.append(float(value))

with open(output_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(categories)
    writer.writerow(values)

print("Data has been successfully saved to", output_filename)
