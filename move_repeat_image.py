import os
import shutil
import argparse
from tqdm import tqdm

def move_matching_images(src_folder1, src_folder2, dest_folder):
    # 获取路径1和路径2中的所有图片文件
    images1 = set(os.listdir(src_folder1))
    images2 = set(os.listdir(src_folder2))

    # 找到路径1和路径2中同名的图片
    matching_images = images1.intersection(images2)

    # 移动匹配的图片到目标文件夹
    for image in tqdm(matching_images, desc="Moving images"):
        src_path = os.path.join(src_folder2, image)
        dest_path = os.path.join(dest_folder, image)
        shutil.move(src_path, dest_path)

def main():
    parser = argparse.ArgumentParser(description="Move matching images from one folder to another.")
    parser.add_argument("--src_folder1", type=str, help="Path to the first image folder")
    parser.add_argument("--src_folder2", type=str, help="Path to the second image folder")
    parser.add_argument("--dest_folder", type=str, help="Path to the destination folder")

    args = parser.parse_args()

    move_matching_images(args.src_folder1, args.src_folder2, args.dest_folder)

if __name__ == "__main__":
    main()
