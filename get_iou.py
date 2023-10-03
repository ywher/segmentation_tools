import pandas as pd
import numpy as np

def get_iou_data(file_name, synthia):

    data_list = []
    begin = end = 0

    with open(file_name, 'r') as f:
        contents = f.readlines()
    
    if synthia:
        num_of_data = 17
    else:
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
            
    file_name = file_name.replace('.txt', '.csv')
    data_dict = {}

    if (eval(data_list[10]) == 0 and eval(data_list[15]) == 0 and eval(data_list[17]) == 0):
        data_list = data_list[:10] + data_list[11:15] + data_list[16:17] + data_list[18:]
        data_list[0] = np.mean(np.array(data_list[1:], dtype=np.float32))

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
    # file_name = 'miou_dataset/daformer/acdc/new1/daformer_acdc_f1_result.txt'
    # file_name = 'miou_dataset/daformer/gta/new_4/daformer_gta_f3_result.txt'
    # file_name = 'miou_dataset/mic_gta_f3_result.txt'
    # file_name = 'miou_dataset/mic/gta/new1/mic_gta_f3_result.txt'
    # file_name = 'miou_dataset/mic/gta/mic_gta_base2_result.txt'
    # file_name = 'miou_dataset/mic/acdc/mic_acdc_f3_result.txt'
    # file_name = 'miou_dataset/tufl/tufl_gta_f5_new_result.txt'
    file_name = 'miou_dataset/daformer/syn/daformer_syn_new5_best/dafomer_syn_f2_result.txt'
    get_iou_data(file_name)