import pandas as pd


def get_iou_data(file_name):

    data_list = []
    begin = end = 0

    with open(file_name, 'r') as f:
        contents = f.readlines()
        
    num_of_data = 20

    for i in range(num_of_data):
        content = contents[i]
        begin = content.find(':')
        end = content.find('\n')
        if end >= len(content):
            number = content[begin+2:]
        else:
            number = content[begin+2:end]
        data_list.append(number)
            
    file_name = 'data.csv'
    data_dict = {}

    if (eval(data_list[10]) == 0 and eval(data_list[15]) == 0 and eval(data_list[17]) == 0):
        data_list = data_list[:10] + data_list[11:15] + data_list[16:17] + data_list[18:]

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
        

if __name__ == '__main__':
    file_name = 'mic_syn_mybase_result.txt'
    get_iou_data(file_name)