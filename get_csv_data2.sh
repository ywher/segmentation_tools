#folder1, folder2, iou使用的是2-1，所以顺序不能错, iou为正时，选择f2的图，iou为负时，选择f1的图
#suffix是后缀，比如.png, 对csv文件里的文件名加上后缀

pred_root="/media/cyber-fx/ywh_disk/projects/SePiCo/work_dirs/local-exp1/syn/230709_0018_dlv2_proj_r101v1c_sepico_DistCL-reg-w1.0-start-iter3000-tau100.0-l3-w1.0_rcs0.01_cpl_self_adamw_6e-05_pmT_poly10warm_1x2_40k_syn2cs_seed76_e449d/pred_trainid"
fusion_root="/media/cyber-fx/ywh_disk/projects/SAM4UDASS/outputs/sepico_dlv2_synthia/"
python get_csv_data.py \
--folder1_path "${pred_root}" \
--folder2_path "${fusion_root}fusion1_trainid" \
--csv_file "${fusion_root}Differ_1_0_Differ_1_0.csv" \
--suffix_folder1 "_leftImg8bittrainID.png" \
--suffix_folder2 "_leftImg8bit.png" \
--output_path "${fusion_root}selected_trainid/"

