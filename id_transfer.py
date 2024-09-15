import os
import cv2
import tqdm
import numpy as np
# from PIL import Image

def convert_labels(input_folder, output_folder, id_mapping):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 获取输入文件夹中的所有图片文件
    image_files = [f for f in os.listdir(input_folder) if f.endswith('.png')]
    bar = tqdm.tqdm(total=len(image_files))
    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, image_file)

        # 使用OpenCV读取图像
        image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

        # 使用NumPy进行类别级id转换，构建一个新的保存转换后图像的数组
        converted_image = np.ones_like(image) * 255
        for old_id, new_id in id_mapping.items():
            converted_image[image == old_id] = new_id
        converted_image = converted_image.astype(np.uint8)
        # 保存转换后的图像
        cv2.imwrite(output_path, converted_image)
        bar.update(1)
    bar.close()
    print("转换完成！")

if __name__ == '__main__':
    # 输入1为标签图文件夹路径，输入2为输出结果路径
    input_folder_path = '/media/ywh/1/yanweihao/projects/uda/BiSeNet-uda/outputs/Synthia_deeplab_BiSeNet_20kunsup_focal_0.8_0.05/pred/pred_trainid'
    output_folder_path = '/media/ywh/1/yanweihao/projects/uda/BiSeNet-uda/outputs/Synthia_deeplab_BiSeNet_20kunsup_focal_0.8_0.05/pred/pred_trainid_transfer'
    # 定义id映射关系
    id_mapping = {
        0: 0,   # 示例：synthia中的0对应cityscapes中的0
        1: 1,   # 示例：synthia中的1对应cityscapes中的1
        2: 2,   # 示例：synthia中的2对应cityscapes中的2
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 10,
        10: 11,
        11: 12,
        12: 13,
        13: 15,
        14: 17,
        15: 18,
    }
    
    # convert_labels(input_folder_path, output_folder_path, id_mapping)
    
    id_inverse_mapping = {k: v for v, k in id_mapping.items()}
    input_folder_path = '/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/tufl/tufl_synthia/fusion1_trainid'
    output_folder_path = '/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/tufl/tufl_synthia/fusion1_trainid_transfer'
    convert_labels(input_folder_path, output_folder_path, id_inverse_mapping)