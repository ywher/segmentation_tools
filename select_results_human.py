'''
输入: 5个文件夹, 显示的图片大小, 输出的csv文件名字, 以及图片之间的间隔, 
            
功能: 每个文件夹下有一系列图片, 每个文件夹下的图片按照名字排序后是一一对应的, 
然后将这5个文件夹下的图片按照顺序水平拼接在一起, 然后显示出来, 
然后可以选择图片, 按键a和d分别表示上一张和下一张图片, enter键表示选择当前图片, esc键表示退出,
选择的图片名字保存在csv文件中
            
输出: 选择的图片名字保存在csv文件中
'''
import cv2
import os
import numpy as np
import pandas as pd

def resize_and_concat_images(img_list, target_size, gap=10, image_name='tmp', num_columns=1):
    """
    Resize and concatenate images horizontally with gaps between them.

    Parameters:
        img_list (list): List of image file paths to be resized and concatenated.
        target_size (tuple): Target size (width, height) for resizing the images.
        gap (int, optional): Gap size between concatenated images. Default is 10 pixels.
        image_name (str, optional): Name to be displayed on the concatenated image. Default is 'tmp'.
        num_columns (int, optional): Number of columns to concatenate the images. Default is 1.

    Returns:
        np.ndarray: Concatenated and resized image.
    """
    resized_images = []
    num_rows = int(np.ceil(len(img_list) / num_columns))

    for img_path in img_list:
        img = cv2.imread(img_path)
        resized_img = cv2.resize(img, target_size)
        resized_images.append(resized_img)

    # Create a blank gap image
    gap_img = 255 * np.ones((target_size[1], gap, 3), dtype=np.uint8) #[h, gap]

    # Create a blank row image
    row_blank = 255 * np.ones((gap, target_size[0] + (target_size[0] + gap) * (num_columns - 1), 3), dtype=np.uint8)
    print(row_blank.shape)
    
    # Concatenate images horizontally with gaps and arrange them in rows
    rows = []
    for i in range(0, len(resized_images), num_columns):
        row_imgs = resized_images[i:i + num_columns]
        row_concatenated_img = row_imgs[0]
        for resize_image in row_imgs[1:]:
            row_concatenated_img = np.hstack([row_concatenated_img, gap_img, resize_image])
        rows.append(row_concatenated_img)

    # Concatenate the rows vertically
    gap_concatenated_img = rows[0]
    for row_img in rows[1:]:
        gap_concatenated_img = np.vstack([gap_concatenated_img, row_blank, row_img])

    cv2.putText(gap_concatenated_img, image_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    return gap_concatenated_img

def save_to_csv(file_names, output_path):
    """
    Save a list of file names to a CSV file.

    Parameters:
        file_names (list): List of file names to be saved.
        output_path (str): Path of the CSV file to save the file names.
    """
    df = pd.DataFrame({'Selected File Names': file_names})
    df.to_csv(output_path, index=False)

def main(folders, resize_size, output_csv_path, gap_size, cols):
    """
    Main function to display and select images from multiple folders, concatenate and resize them,
    and save the selected file names to a CSV file.

    Parameters:
        folders (list): List of folder paths containing images to be displayed and selected.
        resize_size (tuple): Target size (width, height) for resizing the images.
        output_csv_path (str): Path of the CSV file to save the selected file names.
        gap_size (int): Gap size between concatenated images.
        cols (int): Number of columns to concatenate the images.
    """
    # Load lists of file names from each folder
    img_lists = [sorted(os.listdir(folder)) for folder in folders]

    # Initialize the current index of displayed image and list for selected file names
    current_idx = 0
    selected_file_names = []

    while True:
        # Concatenate and resize images horizontally, then display the concatenated image
        image_name = img_lists[1][current_idx].split('.')[0]
        img = resize_and_concat_images([os.path.join(folder, img_list[current_idx])
            for folder, img_list in zip(folders, img_lists)], resize_size, gap_size, image_name, cols)
        cv2.imshow('Concatenated Image', img)

        key = cv2.waitKey(0) & 0xFF

        # Press 'a' key to display the previous image
        if key == ord('a'):
            current_idx = max(0, current_idx - 1)

        # Press 'd' key to display the next image
        elif key == ord('d'):
            current_idx = min(len(img_lists[1]) - 1, current_idx + 1)

        # Press 'enter' key to save the current displayed file name
        elif key == 13:  # ASCII code 13 corresponds to the 'enter' key
            selected_file_names.append(img_lists[1][current_idx])

        # Press 'esc' key to exit the loop and save selected file names to the CSV file
        elif key == 27:  # ASCII code 27 corresponds to the 'esc' key
            break

    # Save selected file names to a CSV file
    save_to_csv(selected_file_names, output_csv_path)

    # Close the image window
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Input 1: List of 5 folder paths, each containing images sorted by file name.
    # folder1_path = "/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/val_all_color"
    # folder2_path = "/home/ywh/Documents/paper_writing/media/syn_comparison/da_base/preds_color"
    # folder3_path = "/home/ywh/Documents/paper_writing/media/syn_comparison/da_best/preds_color"
    # folder4_path = "/home/ywh/Documents/paper_writing/media/syn_comparison/mic_base/preds_color"
    # folder5_path = "/home/ywh/Documents/paper_writing/media/syn_comparison/mic_best/preds_color"
    # folders = [folder1_path, folder2_path, folder3_path, folder4_path, folder5_path]
    folder1_path = '/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_gt_color'
    folder2_path = '/media/ywh/1/yanweihao/projects/uda/DAFormer/work_dirs/local-exp7/gta/230522_2312_gta2cs_dacs_a999_fdthings_rcs001_cpl_daformer_sepaspp_mitb5_poly10warm_s0_ea659/pred_trainid_color'
    folder3_path = '/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/daformer/daformer_gta_sam/sam_majority_color'
    folder4_path = '/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/daformer/daformer_gta_sam/fusion3_majority_color'
    folder5_path = '/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/daformer/daformer_gta_sam/sam_refine_color'
    folder6_path = '/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/daformer/daformer_gta_sam/fusion3_color'
    
    folders = [folder1_path, folder2_path, folder3_path, folder4_path, folder5_path, folder6_path]
    # Input 2: Image resize size
    resize_size = (360, 180)  # (width, height)

    # Input 3: Output path for saving the CSV file
    output_csv_path = "output_sam.csv"
    
    # Input 4: Gap size between concatenated images
    gap_size = 10
    
    # Input 5: Number of columns to concatenate the images
    cols = 2

    # Run the main function
    main(folders, resize_size, output_csv_path, gap_size=gap_size, cols=cols)
