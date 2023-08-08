import os
import pandas as pd
import csv
from tqdm import tqdm
import shutil
import argparse
'''
输入:
    图片1文件夹路径, 图片2文件夹路径, csv文件路径, 图片1后缀, 图片2后缀, 输出路径
功能:
    根据csv文件中的数据, 将图片1文件夹和图片2文件夹中的表现更好的伪标签移动到输出路径
    如果csv文件中的数据为正(>=0), 则将图片2移动到输出路径
    如果csv文件中的数据为负(<0), 则将图片1移动到输出路径
    
    主要用于伪标签的筛选
'''

def process_images(folder1_path, folder2_path, csv_file, suffix_folder1, suffix_folder2, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)
    # Read the CSV file using pandas
    df = pd.read_csv(csv_file, header=0, sep='\t')
    print(df.columns)

    # Iterate over each row in the CSV file
    for _, row in tqdm(df.iterrows(), total=len(df), desc="Processing images"):
        filename = row.values[0].split(',')[0]
        value = eval(row.values[0].split(',')[1])

        # Get the image name without the .csv extension
        image_name = os.path.splitext(filename)[0]

        # Choose the appropriate folder based on the value
        if value >= 0:
            folder_path = folder2_path
            image_suffix = suffix_folder2
        else:
            folder_path = folder1_path
            image_suffix = suffix_folder1

        # Build the full paths of the input and output images
        input_image_path = os.path.join(folder_path, image_name+image_suffix)
        output_image_path = os.path.join(output_path, image_name+'.png')

        # copy the image to the output folder
        shutil.copy(input_image_path, output_image_path)
        # shutil.move(input_image_path, output_image_path)
        # move back
        # shutil.move(output_image_path, input_image_path)
        

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder1_path', type=str, default='/media/ywh/1/yanweihao/projects/uda/MIC/seg/work_dirs/local-exp80/230713_0405_csHR2acdcHR_1024x1024_dacs_a999_fdthings_rcs001-20_m64-07-sep_hrda1-512-01_daformer_sepaspp_sl_mitb5_poly10warm_s0_0b9fc/pred_trainid')
    parser.add_argument('--folder2_path', type=str, default='/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/mic/mic_acdc/fusion3_trainid')
    parser.add_argument('--csv_file', type=str, default='/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/mic/mic_acdc/Differ_3_0_result.csv')
    parser.add_argument('--suffix_folder1', type=str, default='trainID.png')
    parser.add_argument('--suffix_folder2', type=str, default='.png')
    parser.add_argument('--output_path', type=str, default='/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/mic/mic_acdc/select_trainid')
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    folder1_path = args.folder1_path
    folder2_path = args.folder2_path
    csv_file = args.csv_file
    suffix_folder1 = args.suffix_folder1
    suffix_folder2 = args.suffix_folder2
    output_path = args.output_path
    # folder1_path = "/media/ywh/1/yanweihao/projects/uda/MIC/seg/work_dirs/local-exp80/230713_0405_csHR2acdcHR_1024x1024_dacs_a999_fdthings_rcs001-20_m64-07-sep_hrda1-512-01_daformer_sepaspp_sl_mitb5_poly10warm_s0_0b9fc/pred_trainid"
    # folder2_path = "/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/mic/mic_acdc/fusion3_trainid"
    # csv_file = "/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/mic/mic_acdc/Differ_3_0_result.csv"
    # suffix_folder1 = "trainID.png"  # Change this to the actual image extension in folder1
    # suffix_folder2 = ".png"  # Change this to the actual image extension in folder2
    # output_path = "/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/mic/mic_acdc/select_trainid"

    process_images(folder1_path, folder2_path, csv_file, suffix_folder1, suffix_folder2, output_path)
