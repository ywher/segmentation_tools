import os
import argparse
import cv2
from tqdm import tqdm

def change_folder_suffix(folder_root, original_suffix, new_suffix):
    for foldername in tqdm(os.listdir(folder_root), desc="Processing folders"):
        if foldername.endswith(original_suffix):
            original_folder_path = os.path.join(folder_root, foldername)
            new_foldername = foldername.replace(original_suffix, new_suffix)
            new_folder_path = os.path.join(folder_root, new_foldername)
            # rename the folder
            os.rename(original_folder_path, new_folder_path)

def main():
    parser = argparse.ArgumentParser(description="Change folder names in a folder root.")
    parser.add_argument("--folder_root", type=str, help="Path to the folder containing folders")
    parser.add_argument("--original_suffix", type=str, default='_', help="Original image file extension (e.g., .jpg)")
    parser.add_argument("--new_suffix", type=str, default='', help="New image file extension (e.g., .png)")

    args = parser.parse_args()

    change_folder_suffix(args.folder_root, args.original_suffix, args.new_suffix)

if __name__ == "__main__":
    main()
