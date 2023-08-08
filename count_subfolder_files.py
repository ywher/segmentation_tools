import os
import argparse
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


def count_files_in_folder(path):
    file_count = sum(1 for _ in os.listdir(path) if os.path.isfile(os.path.join(path, _)))
    return file_count


def main():
    parser = argparse.ArgumentParser(description="统计子文件夹中的文件数量并进行可视化")
    parser.add_argument("--folder_path", type=str, help="文件夹路径")
    parser.add_argument("--num_subfolders", type=int, default=0, help="要统计的子文件夹数量")
    parser.add_argument("--subtract_one", action="store_true", help="是否在统计子文件夹的文件数量时减去1")

    args = parser.parse_args()

    subfolders = sorted([subdir for subdir in os.listdir(args.folder_path) if os.path.isdir(os.path.join(args.folder_path, subdir))])
    subfolders_to_count = subfolders[:args.num_subfolders]
    file_counts = [count_files_in_folder(os.path.join(args.folder_path, subdir)) for subdir in tqdm(subfolders_to_count)]
    if args.subtract_one:
        file_counts = [count - 1 for count in file_counts]

    average_file_count = np.mean(file_counts)

    # 绘制直方图
    plt.figure(figsize=(6, 2))
    plt.hist(file_counts, bins=10, alpha=0.7, color='blue')
    plt.xlabel('Number of masks')
    plt.ylabel('Number of images')
    # plt.title('Distribution of number of masks per image')
    plt.savefig("histogram.pdf", bbox_inches='tight')
    plt.show()

    print("平均文件数量:", average_file_count)


if __name__ == "__main__":
    main()
