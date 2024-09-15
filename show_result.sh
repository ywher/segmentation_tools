python show_result.py \
--gt_folder '/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_gt_color' \
--pred_folder1 '/media/ywh/1/yanweihao/projects/uda/DAFormer/work_dirs/local-exp7/230522_2312_gta2cs_dacs_a999_fdthings_rcs001_cpl_daformer_sepaspp_mitb5_poly10warm_s0_ea659/pred_train_all' \
--pred_folder2 '/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/train_fusion_gta_daformer_f1_refine/mixed_bg' \
--gt_suffix '_gtFine_color.png' \
--pred_suffix1 '_leftImg8bit.png' \
--pred_suffix2 '_leftImg8bit.png' \
--iou_info_file '/media/ywh/1/yanweihao/projects/segmentation/tools/iou_per_image/compare4_f1refine.xlsx' \
--record_file 'iou_per_image/record4_refine.csv' \
--resolution 256 512 \

#  _pred1.png _pred2.png iou_info.xlsx
