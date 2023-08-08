#folder1, folder2, iou使用的是2-1，所以顺序不能错, iou为正时，选择f2的图，iou为负时，选择f1的图
#suffix是后缀，比如.png, 对csv文件里的文件名加上后缀

pred_root="/media/ywh/1/yanweihao/projects/uda/BiSeNet-uda/outputs/acdc/CityScapes_ACDC_BiSeNet_20kunsup_focal_0.8_0.05_paste_mode_Single_1/pred_train/"
fusion_root="/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/ACDC/tufl_acdc/"
python get_csv_data.py \
--folder1_path "${pred_root}pred_trainid" \
--folder2_path "${fusion_root}fusion5_trainid" \
--csv_file "${fusion_root}Differ_5_0_Differ_5_0.csv" \
--suffix_folder1 ".png" \
--suffix_folder2 ".png" \
--output_path "${fusion_root}selected_trainid/"

