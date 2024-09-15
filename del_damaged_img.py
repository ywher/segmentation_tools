import os
import argparse
import shutil
from tqdm import tqdm  # 导入tqdm

def delete_invalid_images(image_folder, label_folder, record_filename):
    # 获取图像文件夹中的所有文件
    image_files = os.listdir(image_folder)
    
    # 创建一个记录文件，以便记录删除的文件名
    with open(record_filename, 'w') as record_file:
        for image_file in tqdm(image_files, desc="Processing images"):
            image_path = os.path.join(image_folder, image_file)
            label_path = os.path.join(label_folder, image_file)  # 假设标签文件与图像文件具有相同的名称

            try:
                # 在尝试读取图像之前，检查文件是否存在或是否损坏
                with open(image_path, 'rb') as f:
                    f.read()
                
                # 如果文件有效，复制标签文件，删除无效的文件
                # shutil.copy(label_path, label_folder)  # 复制标签文件
            except Exception as e:
                # 记录损坏的文件名到记录文件中，并删除无效的图像文件
                record_file.write(image_file + '\n')
                os.remove(image_path)
                if os.path.exists(label_path):
                    os.remove(label_path)

def main():
    parser = argparse.ArgumentParser(description="Delete invalid images and corresponding labels.")
    parser.add_argument("--image_folder", type=str, help="Path to the image folder")
    parser.add_argument("--label_folder", type=str, help="Path to the label folder")
    parser.add_argument("--record_filename", type=str, help="Path to the record filename")

    args = parser.parse_args()

    delete_invalid_images(args.image_folder, args.label_folder, args.record_filename)

if __name__ == "__main__":
    main()
