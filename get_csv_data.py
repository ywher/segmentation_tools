import os
import pandas as pd
from tqdm import tqdm
import shutil

def process_images(folder1_path, folder2_path, csv_file, suffix_folder1, suffix_folder2, output_path):
    # Read the CSV file using pandas
    df = pd.read_csv(csv_file, sep='\t')

    # Iterate over each row in the CSV file
    for _, row in tqdm(df.iterrows(), total=len(df), desc="Processing images"):
        filename = row['Filename']
        value = row['Value']

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
        input_image_path = os.path.join(folder_path, f"{image_name}.{image_suffix}")
        output_image_path = os.path.join(output_path, f"{image_name}.{image_suffix}")

        # Move the image to the output folder
        shutil.move(input_image_path, output_image_path)

if __name__ == "__main__":
    folder1_path = "path/to/folder1"
    folder2_path = "path/to/folder2"
    csv_file = "path/to/csv_file.csv"
    suffix_folder1 = "jpg"  # Change this to the actual image extension in folder1
    suffix_folder2 = "jpg"  # Change this to the actual image extension in folder2
    output_path = "path/to/output_folder"

    process_images(folder1_path, folder2_path, csv_file, suffix_folder1, suffix_folder2, output_path)
