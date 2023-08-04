'''
输入:
    input_folders: 一个包含5个输入文件夹路径的列表, 分别是原图路径、真值路径和3个预测结果路径。
    output_folder: 保存拼接图像的输出路径。
    image_names: 一个包含要处理的图像名称的列表。
    image_suffix: 一个包含每个输入文件夹中图像文件的后缀的列表。
    new_file_prefix: 包含新图像文件名前缀的列表。
    target_size: 目标图像的大小，用于将图像进行缩放和拼接。
    start_idx: 保存拼接图像时的起始索引, 用于给每个图像样本创建一个独立的文件夹。
功能:
    对给定的图片文件名, 在输入的多个文件夹中查找对应的图像文件, 
    并将它们拼接成一张图像, 然后将拼接后的图像保存到输出文件夹中。
    同时, 将对应的图像复制并重命名到输出文件夹中。
    主要用于论文图像的筛选

输出:

'''
import os
import shutil
import tqdm
from PIL import Image

# Function to get the size of an image
def get_image_size(image_path):
    with Image.open(image_path) as img:
        return img.size

# Function to resize an image
def resize_image(image_path, target_size):
    with Image.open(image_path) as img:
        resized_img = img.resize(target_size, Image.ANTIALIAS)
        return resized_img

# Function to copy and rename images from input folders to the output folder
def copy_and_rename_images(input_folders, output_folder, image_names, image_suffix, new_file_prefix, target_size, start_idx):
    '''
    input_folders: 一个包含5个输入文件夹路径的列表, 分别是原图路径、真值路径和3个预测结果路径。
    output_folder: 保存拼接图像的输出路径。
    image_names: 一个包含要处理的图像名称的列表。
    image_suffix: 一个包含每个输入文件夹中图像文件的后缀的列表。
    new_file_prefix: 包含新图像文件名前缀的列表。
    target_size: 目标图像的大小，用于将图像进行缩放和拼接。
    start_idx: 保存拼接图像时的起始索引, 用于给每个图像样本创建一个独立的文件夹。
    '''
    # Loop through the selected image names and perform the following operations for each image
    bar = tqdm.tqdm(total=len(image_names))
    for idx, image_name in enumerate(image_names, start=start_idx):
        # Create a new sample folder in the output folder for each image
        sample_folder = os.path.join(output_folder, f"sample_{idx}")
        if not os.path.exists(sample_folder):
            os.makedirs(sample_folder)

        # Generate input and output file paths for each image name
        input_file_paths = [os.path.join(input_folder, image_name + image_suffix[i]) for i, input_folder in enumerate(input_folders)]
        output_file_paths = [os.path.join(output_folder, f"sample_{idx}", f"{new_file_prefix[i]}.png") for i in range(len(input_folders))]

        # Read the size of the first input image (assuming all input images have the same size)
        input_image_width, input_image_height = get_image_size(input_file_paths[0])

        # Copy and rename the image from input to output folder
        for i in range(len(input_file_paths)):
            shutil.copy(input_file_paths[i], output_file_paths[i])

        # Resize and save the merged image by concatenating two images side by side
        target_width, target_height = target_size
        col = 2
        row = (len(input_folders) + 1) // col
        merged_image = Image.new("RGB", (target_width * col, target_height * row))

        for i in range(len(input_file_paths)):
            img = resize_image(input_file_paths[i], target_size)
            x_offset = (i % 2) * target_width
            y_offset = (i // 2) * target_height
            merged_image.paste(img, (x_offset, y_offset))

        # Save the merged image with the specified naming convention
        merged_image_path = os.path.join(output_folder, f"sample_{idx}", f"{image_name}.png")
        merged_image.save(merged_image_path)
        bar.update(1)
    bar.close()

# The main entry point of the script
if __name__ == "__main__":
    # # Input 1: Original image path
    # input_folder1 = "/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/leftImg8bit/val_all"
    # # Input 2: Ground truth path
    # input_folder2 = "/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/val_all_color"
    # # Input 3: Path for prediction result 1
    # input_folder3 = "/home/ywh/Documents/paper_writing/media/syn_comparison/da_base/preds_color"
    # # Input 4: Path for prediction result 2
    # input_folder4 = "/home/ywh/Documents/paper_writing/media/syn_comparison/da_best/preds_color"
    # # Input 5: Path for prediction result 3
    # input_folder5 = "/home/ywh/Documents/paper_writing/media/syn_comparison/mic_base/preds_color"
    # # Input 6: Path for prediction result 4
    # input_folder6 = "/home/ywh/Documents/paper_writing/media/syn_comparison/mic_best/preds_color"
    # # Output: Path for saving the concatenated images
    # output_folder = "/home/ywh/Documents/paper_writing/media/syn_comparison/selected_samples"
    # # Image names to be processed and concatenated
    # image_names = ["munster_000122_000019", "frankfurt_000001_070099", "munster_000173_000019",
    #                "lindau_000021_000019", "lindau_000020_000019", "munster_000066_000019",
    #                "frankfurt_000001_067092", "lindau_000004_000019", "lindau_000007_000019",
    #                "lindau_000058_000019", "lindau_000022_000019", "lindau_000016_000019",
    #                "munster_000128_000019", "munster_000117_000019", "lindau_000003_000019",
    #                "munster_000121_000019", "lindau_000006_000019", "munster_000077_000019",
    #                "munster_000171_000019", "munster_000090_000019", "munster_000130_000019"]  # Add all image names accordingly
    # # Suffix for each type of image in the input folders
    # image_suffix = ["_leftImg8bit.png", "_gtFine_labelTrainIds.png", "_leftImg8bit.png",
    #                 "_leftImg8bit.png", "_leftImg8bit.png", "_leftImg8bit.png",]  # Add the image suffix accordingly (e.g., ".jpg", ".png", etc.)
    # # Desired prefix for new image file names
    # new_file_prefix = ["img", "gt", "da_base", "da_best", "mic_base", "mic_best"]  # Add the desired prefix for new image file names
    # # Desired dimensions for resizing the images
    # target_size = (512, 256)  # Set the desired dimensions for resizing the images

    # # Combine the input folders into a list
    # input_folders = [input_folder1, input_folder2, input_folder3, input_folder4, input_folder5, input_folder6]

    # # Calculate the starting index for numbering the output sample folders
    # start_idx = len(os.listdir(output_folder)) + 1

    # # Call the main function to process the images and save the concatenated images with the selected file names
    # copy_and_rename_images(input_folders, output_folder, image_names, image_suffix, new_file_prefix, target_size, start_idx)


    # Input 1: Original image path
    input_folder1 = "/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/leftImg8bit/train_all"
    # Input 2: Ground truth path
    input_folder2 = "/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_all_color"
    # Input 3: SAM masks
    input_folder3 = "/media/ywh/1/yanweihao/projects/segmentation/segment-anything/tools/outputs/cityscapes_mix2/rgb"
    # Input 4: UDA prediction
    input_folder4 = "/media/ywh/1/yanweihao/projects/uda/DAFormer/work_dirs/local-exp7/gta/230522_2312_gta2cs_dacs_a999_fdthings_rcs001_cpl_daformer_sepaspp_mitb5_poly10warm_s0_ea659/pred_trainid_color"
    # Input 5: DINO prediction
    input_folder5 = "/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/dino/train_all_color"
    # Input 6: majority voting
    input_folder6 = "/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/daformer/daformer_gta_sam/sam_majority_color"
    # Input 7: SGML prediction
    input_folder7 = "/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/daformer/daformer_gta_sam/sam_refine_color"
    # Input 8: fusion 3 color on SGML
    input_folder8 = "/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/daformer/daformer_gta_sam/fusion3_color"
    # Output: Path for saving the concatenated images
    output_folder = "/home/ywh/Documents/paper_writing/media/get_sam/selected_samples"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # Image names to be processed and concatenated
    image_names = ["aachen_000000_000019", "aachen_000004_000019", "aachen_000009_000019",
                   "aachen_000021_000019", "aachen_000024_000019", "aachen_000027_000019",
                   "aachen_000035_000019", "aachen_000064_000019", "aachen_000075_000019",
                   "aachen_000077_000019", "aachen_000080_000019", "aachen_000086_000019",
                   "aachen_000100_000019", "aachen_000111_000019", "aachen_000133_000019",
                   "aachen_000134_000019", "aachen_000139_000019", "aachen_000153_000019",
                   "bochum_000000_002293"]  # Add all image names accordingly
    # Suffix for each type of image in the input folders
    image_suffix = ["_leftImg8bit.png", "_gtFine_labelTrainIds.png", "_leftImg8bit.png", "_leftImg8bittrainID.png",
                    "_leftImg8bit_labelTrainIds.png", "_leftImg8bit.png", "_leftImg8bit.png", "_leftImg8bit.png"]  # Add the image suffix accordingly (e.g., ".jpg", ".png", etc.)
    # Desired prefix for new image file names
    new_file_prefix = ["img", "gt", "sam_mask", "uda_pred", "dino", "majority", "sgml", "fusion3"]  # Add the desired prefix for new image file names
    # Desired dimensions for resizing the images
    target_size = (512, 256)  # Set the desired dimensions for resizing the images

    # Combine the input folders into a list
    input_folders = [input_folder1, input_folder2, input_folder3, input_folder4, 
                     input_folder5, input_folder6, input_folder7, input_folder8]

    # Calculate the starting index for numbering the output sample folders
    start_idx = len(os.listdir(output_folder)) + 1

    # Call the main function to process the images and save the concatenated images with the selected file names
    copy_and_rename_images(input_folders, output_folder, image_names, image_suffix, 
                           new_file_prefix, target_size, start_idx)
    
    # select for paper first image
    # # Input 1: Original image path
    # input_folder1 = "/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/leftImg8bit/train_all"
    # # Input 2: Ground truth path
    # input_folder2 = "/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_all_color"
    # # Input 3: SAM masks
    # input_folder3 = "/media/ywh/1/yanweihao/projects/segmentation/segment-anything/tools/outputs/cityscapes_mix2/rgb"
    # # Input 4: UDA prediction
    # input_folder4 = "/media/ywh/1/yanweihao/projects/uda/DAFormer/work_dirs/local-exp7/gta/230522_2312_gta2cs_dacs_a999_fdthings_rcs001_cpl_daformer_sepaspp_mitb5_poly10warm_s0_ea659/pred_trainid_color"
    # # Input 5: Fusion 3
    # input_folder5 = "/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/daformer/beta_ablation/daformer_gta_beta0.9/fusion3_trainid_color"
    # # # Input 6: mixed image
    # input_folder6 = "/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_gt_mix_color"
    # # # Input 7: SGML prediction
    # # input_folder7 = "/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/daformer/daformer_gta_sam/sam_refine_color"
    # # Output: Path for saving the concatenated images
    # output_folder = "/home/ywh/Documents/paper_writing/media/first_img/selected_samples"
    # if not os.path.exists(output_folder):
    #     os.makedirs(output_folder)
    # # Image names to be processed and concatenated
    # image_names = ["strasbourg_000001_043748", "bochum_000000_002293", "zurich_000116_000019",
    #                "zurich_000050_000019", "strasbourg_000001_013914", "darmstadt_000041_000019",
    #                "hamburg_000000_018878", "weimar_000104_000019", "strasbourg_000000_010816",
    #                "hamburg_000000_103075", "strasbourg_000000_023854", "stuttgart_000016_000019",
    #                "ulm_000055_000019", "strasbourg_000001_061472", "ulm_000036_000019",
    #                "zurich_000080_000019", "strasbourg_000001_051134", "tubingen_000060_000019",
    #                "strasbourg_000001_054639", "jena_000077_000019", "darmstadt_000048_000019",
    #                "monchengladbach_000000_018575", "krefeld_000000_005503", "zurich_000119_000019",
    #                "bremen_000035_000019", "aachen_000139_000019", "darmstadt_000083_000019",
    #                "zurich_000044_000019", "bremen_000140_000019", "bochum_000000_030913",
    #                "aachen_000130_000019", "strasbourg_000001_058373", "jena_000091_000019",
    #                "zurich_000061_000019", "bremen_000135_000019", "bremen_000119_000019",
    #                "strasbourg_000001_028379", "bochum_000000_037223", "monchengladbach_000000_018445",
    #                "jena_000030_000019", "strasbourg_000000_025491", "weimar_000066_000019",
    #                "bochum_000000_033531", "erfurt_000033_000019", "hanover_000000_001620",
    #                "bremen_000310_000019", "tubingen_000054_000019", "hamburg_000000_074267",
    #                "tubingen_000001_000019", "bremen_000292_000019", "erfurt_000040_000019",
    #                "jena_000104_000019", "zurich_000089_000019", "weimar_000075_000019"
    #                 ]  # Add all image names accordingly
    # # Suffix for each type of image in the input folders
    # image_suffix = ["_leftImg8bit.png", "_gtFine_labelTrainIds.png", "_leftImg8bit.png",
    #                 "_leftImg8bittrainID.png", "_leftImg8bit.png", "_leftImg8bit.png"]  # Add the image suffix accordingly (e.g., ".jpg", ".png", etc.)
    # # Desired prefix for new image file names
    # new_file_prefix = ["img", "gt", "sam", "uda", "fusion3", "mix"]  # Add the desired prefix for new image file names
    # # Desired dimensions for resizing the images
    # target_size = (512, 256)  # Set the desired dimensions for resizing the images

    # # Combine the input folders into a list
    # input_folders = [input_folder1, input_folder2, input_folder3, input_folder4, input_folder5, input_folder6]

    # # Calculate the starting index for numbering the output sample folders
    # start_idx = len(os.listdir(output_folder)) + 1

    # # Call the main function to process the images and save the concatenated images with the selected file names
    # copy_and_rename_images(input_folders, output_folder, image_names, image_suffix, new_file_prefix, target_size, start_idx)
