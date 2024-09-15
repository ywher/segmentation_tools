import csv
'''
输入:
    filename: txt文件路径, acdc test上的结果
    output_filename: 保存结果的csv文件路径
功能
    将txt文件中的数据保存到csv文件中
    主要用于保存acdc test evaluation server上的评估结果
'''

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
