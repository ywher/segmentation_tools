#cityscapes
# python miou_cal.py \
# --gt_dir '/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_all' \
# --pred_dir '/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/train_fusion_gta_daformer_f1_refine/trainID_bg' \
# --devkit_dir '/media/ywh/1/yanweihao/projects/segmentation/tools/utils' \
# --save_path 'miou_dataset/daformer_gta_f1_refine.txt'

# seg: daformer gta base; fusion mode: 2 ; sam mask: refine
# python miou_cal.py \
# --gt_dir '/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_all' \
# --pred_dir '/media/ywh/1/yanweihao/projects/uda/DAFormer/work_dirs/local-exp7/230522_2312_gta2cs_dacs_a999_fdthings_rcs001_cpl_daformer_sepaspp_mitb5_poly10warm_s0_ea659/trainid' \
# --devkit_dir '/media/ywh/1/yanweihao/projects/segmentation/tools/utils' \
# --save_path 'miou_dataset/daformer_gta_base.txt'


# python miou_cal.py \
# --gt_dir '/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_all' \
# --pred_dir '/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/train_fusion_gta_mic_base2/trainID_bg' \
# --devkit_dir '/media/ywh/1/yanweihao/projects/segmentation/tools/utils' \
# --save_path './mic_gta_f1_result2.txt'

# gta
for i in 1 2 3 4 5
do
    python miou_cal.py \
    --gt_dir '/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_all' \
    --pred_dir '/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/debug_gta/fusion'$i'_trainid' \
    --devkit_dir '/media/ywh/1/yanweihao/projects/segmentation/tools/utils' \
    --save_path 'miou_dataset/daformer_gta_f'$i'_result.txt'
done

# synthia
# for i in 1 2 3 4 5
# do
#     python miou_cal.py \
#     --gt_dir '/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_all' \
#     --pred_dir '/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/debug_syn_tmp2/fusion'$i'_trainid' \
#     --devkit_dir '/media/ywh/1/yanweihao/projects/segmentation/tools/utils' \
#     --save_path 'miou_dataset/dafomer_syn_f'$i'_result.txt'
# done

# python miou_cal.py \
# --gt_dir '/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_darmstadt' \
# --pred_dir '/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/train_fusion_darmstadt_1/trainID_bg' \
# --devkit_dir '/media/ywh/1/yanweihao/projects/segmentation/tools/utils' \
# --save_path './daformer_gtaf1_darmstadt1_result.txt'

#acdc
# python miou_cal.py \
# --gt_dir '/media/ywh/1/yanweihao/dataset/acdc/gt/train' \
# --pred_dir '/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/ACDC/train_fusion2/trainID_bg' \
# --devkit_dir '/media/ywh/1/yanweihao/projects/segmentation/tools/utils' \
# --save_path './daformer_acdc_f1_ssam_result.txt'

# --pred_dir '/media/ywh/1/yanweihao/projects/uda/DAFormer/work_dirs/local-exp8/230527_0645_cs2acdc_dacs_a999_fdthings_rcs001_cpl_daformer_sepaspp_mitb5_poly10warm_s0_f753f/pred_trainid' \

#pred mic new: '/media/ywh/1/yanweihao/projects/uda/MIC/seg/work_dirs/local-basic/230505_2311_gtaHR2csHR_mic_hrda_s2_38493/pred_trainid'
#pred '/media/yons/pool1/ywh/projects/UDA/MIC/seg/work_dirs/local-exp80/230422_0820_gtaHR2csHR_1024x1024_dacs_a999_fdthings_rcs001-20_cpl2_m64-07-spta_hrda1-512-01_daformer_sepaspp_sl_mitb5_poly10warm_3e-05_s0_21197/pred_trainid' \
#pred_dir2 /media/yons/pool1/ywh/projects/Segmentation/segment-anything/outputs/cityscapes/train_fusion/trainID_bg
