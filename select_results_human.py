import cv2
import os
import numpy as np
import pandas as pd

def resize_and_concat_images(img_list, target_size, gap=10, image_name='tmp'):
    resized_images = []
    for img_path in img_list:
        img = cv2.imread(img_path)
        resized_img = cv2.resize(img, target_size)
        resized_images.append(resized_img)

    # Create a blank gap image
    gap_img = 255 * np.ones((target_size[1], gap, 3), dtype=np.uint8)

    # Concatenate images horizontally with gaps
    gap_concatenated_img = resized_images[0]
    for resize_image in resized_images[1:]:
        gap_concatenated_img = np.hstack([gap_concatenated_img, gap_img, resize_image])
    cv2.putText(gap_concatenated_img, image_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    # gap_concatenated_img = np.hstack([resized_images[0], gap_img, resized_images[1], gap_img, resized_images[2], gap_img, resized_images[3], gap_img, resized_images[4]])

    return gap_concatenated_img


def save_to_csv(file_names, output_path):
    df = pd.DataFrame({'Selected File Names': file_names})
    df.to_csv(output_path, index=False)

def main(folders, resize_size, output_csv_path, gap_size):
    # 加载文件名列表
    img_lists = [sorted(os.listdir(folder)) for folder in folders]
    # img_list = sorted(os.listdir(folders[0]))

    # 初始化显示的图像序号和选中的文件名列表
    current_idx = 0
    selected_file_names = []

    while True:
        # 水平拼接图像并显示
        image_name = img_lists[1][current_idx].split('.')[0]
        img = resize_and_concat_images([os.path.join(folder, img_list[current_idx]) 
            for folder, img_list in zip(folders, img_lists)], resize_size, gap_size, image_name)
        cv2.imshow('concate image', img)

        key = cv2.waitKey(0) & 0xFF

        # 按下'a'键，显示前一张图像
        if key == ord('a'):
            current_idx = max(0, current_idx - 1)

        # 按下'd'键，显示后一张图像
        elif key == ord('d'):
            current_idx = min(len(img_lists[1]) - 1, current_idx + 1)

        # 按下'enter'键，保存当前显示的文件名
        elif key == 13:  # ASCII码13对应enter键
            selected_file_names.append(img_lists[1][current_idx])

        # 按下'esc'键，退出循环并保存选中的文件名到csv文件
        elif key == 27:  # ASCII码27对应esc键
            break

    # 保存选中的文件名到csv文件
    save_to_csv(selected_file_names, output_csv_path)

    # 关闭窗口
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # 输入1：5个文件夹路径，按文件名排序后对应的图片
    # ground truth
    folder1_path = "/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/val_all_color"
    # folder2_path = "/home/ywh/Documents/paper_writing/media/gta_comparison/da_base_predval/preds_color"
    # folder3_path = "/home/ywh/Documents/paper_writing/media/gta_comparison/da_best_predval/preds_color"
    # folder4_path = "/home/ywh/Documents/paper_writing/media/gta_comparison/mic_base_predval/preds_color"
    # folder5_path = "/home/ywh/Documents/paper_writing/media/gta_comparison/mic_best_predval/preds_color"
    folder2_path = "/home/ywh/Documents/paper_writing/media/syn_comparison/da_base/preds_color"
    folder3_path = "/home/ywh/Documents/paper_writing/media/syn_comparison/da_best/preds_color"
    folder4_path = "/home/ywh/Documents/paper_writing/media/syn_comparison/mic_base/preds_color"
    folder5_path = "/home/ywh/Documents/paper_writing/media/syn_comparison/mic_best/preds_color"
    folders = [folder1_path, folder2_path, folder3_path, folder4_path, folder5_path]

    # 输入2：图像resize的尺寸
    resize_size = (360, 180)  # (w, h)
    gap_size = 10

    # 输入3：保存csv文件的路径，即输出路径
    output_csv_path = "output_syn.csv"
    main(folders, resize_size, output_csv_path, gap_size)
