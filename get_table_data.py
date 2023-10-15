import pandas as pd

table_data_string = "68.28	94.58	64.47	89.27	52.05	44.81	48.09	56.1	59.21	89.9	50.43	91.45	71.86	45.03	92.49	75.55	80.63	74.32	55.12	61.99"

string_length = len(table_data_string)

data_list = []
begin = end = 0
while(end != (string_length - 1)):
    while(table_data_string[end] != ' ' and table_data_string[end] != '\t'):
        if end != (string_length - 1):
            end += 1
        else:
            break
    if end == (string_length - 1):
        data = table_data_string[begin:]
        data_list.append(data)
        break
    else:
        data = table_data_string[begin:end]
        data_list.append(data)
        begin = end + 1
        
    while(table_data_string[begin] not in ['0','1','2','3','4','5','6','7','8','9']):
        if begin != (string_length - 1):
            begin += 1
        else:
            break
    end = begin + 1

file_name = 'outputs/table_data.csv'
data_dict = {}

for i in range(len(data_list)):
    if eval(data_list[i]) < 1:
        data_dict[i] = [eval(data_list[i]) * 100]
    else:
        data_dict[i] = [eval(data_list[i])]

data_dict = pd.DataFrame(data_dict)
data_dict.to_csv(file_name, index=False)

puls = False
if eval(data_list[0]) < 10:
    puls = True
for data in data_list:
    num = eval(data)
    if puls:
        num *= 100
    print('& %.1f'%num, ' ',end='')
    

