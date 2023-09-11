import os
import argparse
from tqdm import tqdm

def change_image_suffix(folder_path, original_suffix, new_suffix):
    for filename in tqdm(os.listdir(folder_path), desc="Processing images"):
        # if filename.endswith(original_suffix):
        original_file_path = os.path.join(folder_path, filename)
        new_filename = filename.replace(original_suffix, new_suffix)
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(original_file_path, new_file_path)

def main():
    parser = argparse.ArgumentParser(description="Change image file extensions in a folder.")
    parser.add_argument("--folder_path", type=str, help="Path to the folder containing images")
    parser.add_argument("--original_suffix", type=str, help="Original image file extension (e.g., .jpg)")
    parser.add_argument("--new_suffix", type=str, help="New image file extension (e.g., .png)")

    args = parser.parse_args()

    change_image_suffix(args.folder_path, args.original_suffix, args.new_suffix)

if __name__ == "__main__":
    main()
