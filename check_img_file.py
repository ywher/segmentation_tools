import os
import cv2
import shutil
import csv
import tqdm
import argparse

def check_images(folder1, folder2, output_csv):
    # 获取文件夹1中的所有文件名
    folder1_files = os.listdir(folder1)
    
    # 创建CSV文件以记录有问题的文件名
    with open(output_csv, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['File Name', 'Status'])
        
        bar = tqdm.tqdm(total=len(folder1_files))
        for filename in folder1_files:
            # 构建文件的完整路径
            file1_path = os.path.join(folder1, filename)
            file2_path = os.path.join(folder2, filename)
            
            # 检查文件1是否存在
            if not os.path.exists(file1_path):
                print(f"File '{filename}' does not exist in folder1.")
                csv_writer.writerow([filename, 'Missing'])
                continue
            
            # 读取文件1，如果失败，则使用文件2进行覆盖
            try:
                img = cv2.imread(file1_path)
                if img is None:
                    print(f"Failed to read '{filename}' in folder1. Replacing with file from folder2.")
                    shutil.copy(file2_path, file1_path)
                    csv_writer.writerow([filename, 'Replaced'])
            except Exception as e:
                print(f"Error processing '{filename}': {str(e)}")
                csv_writer.writerow([filename, 'Error'])
                
            bar.update(1)
        bar.close()
    csv_file.close()

def main():
    # 创建解析器
    parser = argparse.ArgumentParser(description="Check and replace images in folder1 with corresponding images from folder2 if needed.")
    
    # 添加命令行参数
    parser.add_argument("--folder1", help="Path to the first folder containing images")
    parser.add_argument("--folder2", help="Path to the second folder containing replacement images")
    parser.add_argument("--output_csv", help="Path to the output CSV file")
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 调用函数进行检查和替换
    check_images(args.folder1, args.folder2, args.output_csv)

if __name__ == "__main__":
    main()

