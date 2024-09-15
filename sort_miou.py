import os
import numpy as np
from PIL import Image
import pandas as pd
from tqdm import tqdm

def calculate_iou(gt_path, pred_path, num_classes=19):
    gt_img = np.array(Image.open(gt_path))
    pred_img = np.array(Image.open(pred_path))
    
    iou_per_class = []
    
    for class_id in range(1, num_classes + 1):
        gt_class_mask = (gt_img == class_id)
        pred_class_mask = (pred_img == class_id)

        intersection = np.logical_and(gt_class_mask, pred_class_mask).sum()
        union = np.logical_or(gt_class_mask, pred_class_mask).sum()

        if union == 0:  # Avoid division by zero
            iou_per_class.append(0.0)
        else:
            iou_per_class.append(intersection / union)

    return iou_per_class

def calculate_miou(gt_path, pred_path, num_classes=19):
    iou_per_class = calculate_iou(gt_path, pred_path, num_classes)
    
    # Filter out the class where the ground truth has value 255
    valid_iou_per_class = [iou for iou in iou_per_class if iou != 255]
    
    miou = np.mean(valid_iou_per_class)
    miou_percent = miou * 100.0
    
    return miou_percent


def main(gt_folder, pred1_folder, pred2_folder, pred3_folder, pred4_folder):
    # 获取文件名列表，按文件名排序
    file_names = sorted(os.listdir(gt_folder))
    file_names_pred1 = sorted(os.listdir(pred1_folder))
    file_names_pred2 = sorted(os.listdir(pred2_folder))
    file_names_pred3 = sorted(os.listdir(pred3_folder))
    file_names_pred4 = sorted(os.listdir(pred4_folder))

    # 初始化结果列表
    results = []

    for file_name, file_name_pred1, file_name_pred2, file_name_pred3, file_name_pred4 \
        in tqdm(zip(file_names, file_names_pred1, file_names_pred2,
                 file_names_pred3, file_names_pred4), desc="Calculating MIoU"):
        gt_path = os.path.join(gt_folder, file_name)
        pred1_path = os.path.join(pred1_folder, file_name_pred1)
        pred2_path = os.path.join(pred2_folder, file_name_pred2)
        pred3_path = os.path.join(pred3_folder, file_name_pred3)
        pred4_path = os.path.join(pred4_folder, file_name_pred4)

        miou_pred1 = calculate_miou(gt_path, pred1_path)
        miou_pred2 = calculate_miou(gt_path, pred2_path)
        miou_pred3 = calculate_miou(gt_path, pred3_path)
        miou_pred4 = calculate_miou(gt_path, pred4_path)
        delta_miou = miou_pred2 - miou_pred1
        delta_miou2 = miou_pred4 - miou_pred3

        results.append([file_name, miou_pred1, miou_pred2, delta_miou,
                        miou_pred3, miou_pred4, delta_miou2])

    # 将结果保存为CSV文件，并保留两位小数
    df = pd.DataFrame(results, columns=["File Name", "MIoU Prediction 1",
                                        "MIoU Prediction 2", "Delta MIoU",
                                        "MIoU Prediction 3", "MIoU Prediction 4",
                                        "Delta MIoU2"])
    df["MIoU Prediction 1"] = df["MIoU Prediction 1"].round(2)
    df["MIoU Prediction 2"] = df["MIoU Prediction 2"].round(2)
    df["Delta MIoU"] = df["Delta MIoU"].round(2)
    df["MIoU Prediction 3"] = df["MIoU Prediction 3"].round(2)
    df["MIoU Prediction 4"] = df["MIoU Prediction 4"].round(2)
    df["Delta MIoU2"] = df["Delta MIoU2"].round(2)
    df.to_csv("miou_results.csv", index=False)

def main2(gt_folder, pred1_folder, pred2_folder):
    # 获取文件名列表，按文件名排序
    file_names = sorted(os.listdir(gt_folder))
    file_names_pred1 = sorted(os.listdir(pred1_folder))
    file_names_pred2 = sorted(os.listdir(pred2_folder))
    # file_names_pred3 = sorted(os.listdir(pred3_folder))
    # file_names_pred4 = sorted(os.listdir(pred4_folder))

    # 初始化结果列表
    results = []
    bar = tqdm(total=len(file_names))
    for file_name, file_name_pred1, file_name_pred2 \
        in zip(file_names, file_names_pred1, file_names_pred2):
        gt_path = os.path.join(gt_folder, file_name)
        pred1_path = os.path.join(pred1_folder, file_name_pred1)
        pred2_path = os.path.join(pred2_folder, file_name_pred2)
        # pred3_path = os.path.join(pred3_folder, file_name_pred3)
        # pred4_path = os.path.join(pred4_folder, file_name_pred4)

        miou_pred1 = calculate_miou(gt_path, pred1_path)
        miou_pred2 = calculate_miou(gt_path, pred2_path)
        # miou_pred3 = calculate_miou(gt_path, pred3_path)
        # miou_pred4 = calculate_miou(gt_path, pred4_path)
        delta_miou = miou_pred2 - miou_pred1
        print('delta_miou', delta_miou)
        # delta_miou2 = miou_pred4 - miou_pred3

        results.append([file_name, miou_pred1, miou_pred2, delta_miou])
        bar.update(1)
    bar.close()

    # 将结果保存为CSV文件，并保留两位小数
    df = pd.DataFrame(results, columns=["File Name", "MIoU Prediction 1",
                                        "MIoU Prediction 2", "Delta MIoU"])
    df["MIoU Prediction 1"] = df["MIoU Prediction 1"].round(2)
    df["MIoU Prediction 2"] = df["MIoU Prediction 2"].round(2)
    df["Delta MIoU"] = df["Delta MIoU"].round(2)
    # df["MIoU Prediction 3"] = df["MIoU Prediction 3"].round(2)
    # df["MIoU Prediction 4"] = df["MIoU Prediction 4"].round(2)
    # df["Delta MIoU2"] = df["Delta MIoU2"].round(2)
    df.to_csv("miou_results_new.csv", index=False)

if __name__ == "__main__":
    # 输入1：语义分割真值的路径
    # gt_folder = "/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/val_all"
    # # 输入2：预测结果1的路径
    # pred1_folder = "/home/ywh/Documents/paper_writing/media/syn_comparison/da_base/preds_trainid"
    # # 输入3：预测结果2的路径
    # pred2_folder = "/home/ywh/Documents/paper_writing/media/syn_comparison/da_best/preds_trainid"
    # # 输入2：预测结果3的路径
    # pred3_folder = "/home/ywh/Documents/paper_writing/media/syn_comparison/mic_base/preds_trainid"
    # # 输入3：预测结果4的路径
    # pred4_folder = "/home/ywh/Documents/paper_writing/media/syn_comparison/mic_best/preds_trainid"
    # main(gt_folder, pred1_folder, pred2_folder, pred3_folder, pred4_folder)

    gt_folder = "/media/cyber-fx/ywh_disk/datasets/cityscapes/gtFine/train_all"
    pred_da_base = "/media/cyber-fx/ywh_disk/projects/SePiCo/work_dirs/local-exp1/acdc/230723_1056_dlv2_proj_r101v1c_sepico_DistCL-reg-w1.0-start-iter3000-tau100.0-l3-w1.0_rcs0.01_cpl_self_adamw_6e-05_pmT_poly10warm_1x2_40k_cs2acdc_seed76_fef76/pred_trainid"
    pred_fusion3 = "/media/cyber-fx/ywh_disk/projects/SAM4UDASS/outputs/sepico_acdc/fusion1_trainid"
    main2(gt_folder, pred_da_base, pred_fusion3)