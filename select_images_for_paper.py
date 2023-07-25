import os
import shutil
from PIL import Image

def get_image_size(image_path):
    with Image.open(image_path) as img:
        return img.size

def resize_image(image_path, target_size):
    with Image.open(image_path) as img:
        resized_img = img.resize(target_size, Image.ANTIALIAS)
        return resized_img

def copy_and_rename_images(input_folders, output_folder, image_names, image_suffix, new_file_prefix, target_size, start_idx):


    for idx, image_name in enumerate(image_names, start=start_idx):
        sample_folder = os.path.join(output_folder, f"sample_{idx}")
        if not os.path.exists(sample_folder):
            os.makedirs(sample_folder)
        
        # Generate input and output file paths for each image name
        input_file_paths = [os.path.join(input_folder, image_name + image_suffix[i]) for i, input_folder in enumerate(input_folders)]
        output_file_paths = [os.path.join(output_folder, f"sample_{idx}", f"{new_file_prefix[i]}.png") for i in range(len(input_folders))]

        # Read the size of the first input image
        input_image_width, input_image_height = get_image_size(input_file_paths[0])

        # Copy and rename the image from input to output folder
        for i in range(len(input_file_paths)):
            shutil.copy(input_file_paths[i], output_file_paths[i])

        # Resize and save the merged image
        target_width, target_height = target_size
        merged_image = Image.new("RGB", (target_width * 2, target_height * 3))

        for i in range(len(input_file_paths)):
            img = resize_image(input_file_paths[i], target_size)
            x_offset = (i % 2) * target_width
            y_offset = (i // 2) * target_height
            merged_image.paste(img, (x_offset, y_offset))

        merged_image_path = os.path.join(output_folder, f"sample_{idx}", f"{image_name}.png")
        merged_image.save(merged_image_path)

if __name__ == "__main__":
    # 输入1：原图路径
    input_folder1 = "/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/leftImg8bit/val_all"
    # 输入2：真值路径
    input_folder2 = "/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/val_all_color"
    # 输入3：预测结果1路径
    input_folder3 = "/home/ywh/Documents/paper_writing/media/syn_comparison/da_base/preds_color"
    # 输入4：预测结果2路径
    input_folder4 = "/home/ywh/Documents/paper_writing/media/syn_comparison/da_best/preds_color"
    # 输入5：预测结果3路径
    input_folder5 = "/home/ywh/Documents/paper_writing/media/syn_comparison/mic_base/preds_color"
    # 输入6：预测结果4路径
    input_folder6 = "/home/ywh/Documents/paper_writing/media/syn_comparison/mic_best/preds_color"
    # 输入7：保存的输出路径
    output_folder = "/home/ywh/Documents/paper_writing/media/syn_comparison/selected_samples"
    # 输入8：图片名列表
    image_names = ["munster_000122_000019", "frankfurt_000001_070099", "munster_000173_000019",
                   "lindau_000021_000019", "lindau_000020_000019", "munster_000066_000019",
                   "frankfurt_000001_067092", "lindau_000004_000019", "lindau_000007_000019",
                   "lindau_000058_000019", "lindau_000022_000019", "lindau_000016_000019",
                   "munster_000128_000019", "munster_000117_000019", "lindau_000003_000019",
                   "munster_000121_000019", "lindau_000006_000019", "munster_000077_000019",
                   "munster_000171_000019", "munster_000090_000019", "munster_000130_000019"]  # Add all image names accordingly
    # 输入9：图片名后缀
    image_suffix = ["_leftImg8bit.png", "_gtFine_labelTrainIds.png", "_leftImg8bit.png",
                    "_leftImg8bit.png", "_leftImg8bit.png", "_leftImg8bit.png",]  # Add the image suffix accordingly (e.g., ".jpg", ".png", etc.)
    # 输入10：图片新文件名前缀
    new_file_prefix = ["img", "gt", "da_base", "da_best", "mic_base", "mic_best"]  # Add the desired prefix for new image file names
    # 输入11：拼接尺寸
    target_size = (512, 256)  # Set the desired dimensions for resizing the images

    # Combine the input folders into a list
    input_folders = [input_folder1, input_folder2, input_folder3, input_folder4, input_folder5, input_folder6]

    start_idx = len(os.listdir(output_folder)) + 1
    copy_and_rename_images(input_folders, output_folder, image_names, image_suffix, new_file_prefix, target_size, start_idx)
