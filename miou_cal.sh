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
# dafromer
for i in 1 2 3 4 5
do
    python miou_cal.py \
    --gt_dir '/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_all' \
    --pred_dir '/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/daformer/daformer_gta_alpha0.1/fusion'$i'_trainid' \
    --devkit_dir '/media/ywh/1/yanweihao/projects/segmentation/tools/utils' \
    --save_path 'miou_dataset/daformer_gta_f'$i'_result_alpha0.1.txt'
done

# for i in 1 2 3
# do
#     python miou_cal.py \
#     --gt_dir '/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_all' \
#     --pred_dir '/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/train_fusion_gta_dino4/fusion'$i'_trainid' \
#     --devkit_dir '/media/ywh/1/yanweihao/projects/segmentation/tools/utils' \
#     --save_path 'miou_dataset/daformer_gta_f'$i'_dino_new5_result.txt'
# done

# python miou_cal.py \
# --gt_dir '/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_all' \
# --pred_dir '/media/ywh/1/yanweihao/projects/uda/DAFormer/work_dirs/local-exp7/gta/230522_2312_gta2cs_dacs_a999_fdthings_rcs001_cpl_daformer_sepaspp_mitb5_poly10warm_s0_ea659/trainid' \
# --devkit_dir '/media/ywh/1/yanweihao/projects/segmentation/tools/utils' \
# --save_path 'miou_dataset/daformer_gta_base_result.txt'

# mic
# python miou_cal.py \
# --gt_dir '/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_all' \
# --pred_dir '/media/ywh/1/yanweihao/projects/uda/MIC/seg/work_dirs/local-exp80/230716_1343_gtaHR2csHR_1024x1024_dacs_a999_fdthings_rcs001-20_cpl2_m64-07-spta_hrda1-512-01_daformer_sepaspp_sl_mitb5_poly10warm_s0_ea911/pred_trainid' \
# --devkit_dir '/media/ywh/1/yanweihao/projects/segmentation/tools/utils' \
# --save_path 'miou_dataset/mic_gta_base3_result.txt'

# for i in 1 2 3 4 5
# do
#     python miou_cal.py \
#     --gt_dir '/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_all' \
#     --pred_dir '/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/mic_gta_new3/fusion'$i'_trainid' \
#     --devkit_dir '/media/ywh/1/yanweihao/projects/segmentation/tools/utils' \
#     --save_path 'miou_dataset/mic_gta_f'$i'_new3_result.txt'
# done


# sepico
# python miou_cal.py \
# --gt_dir '/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_all' \
# --pred_dir '/media/ywh/1/yanweihao/projects/uda/SePiCo/work_dirs/local-exp1/230707_0324_dlv2_proj_r101v1c_sepico_DistCL-reg-w1.0-start-iter3000-tau100.0-l3-w1.0_rcs0.01_cpl_self_adamw_6e-05_pmT_poly10warm_1x2_40k_gta2cs_seed76_36629/pred_trainid' \
# --devkit_dir '/media/ywh/1/yanweihao/projects/segmentation/tools/utils' \
# --save_path 'miou_dataset/sepicov2_gta_base_result.txt'

# tufl
# for i in 1 2 3 4 5
# do
#     python miou_cal.py \
#     --gt_dir '/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_all' \
#     --pred_dir '/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/tufl_gta_new/fusion'$i'_trainid' \
#     --devkit_dir '/media/ywh/1/yanweihao/projects/segmentation/tools/utils' \
#     --save_path 'miou_dataset/tufl_gta_f'$i'_new2_result.txt'
# done

# synthia
# for i in 1 2 3 4 5
# do
#     python miou_cal.py \
#     --gt_dir '/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_all' \
#     --pred_dir '/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/debug_syn_tmp3/fusion'$i'_trainid' \
#     --devkit_dir '/media/ywh/1/yanweihao/projects/segmentation/tools/utils' \
#     --save_path 'miou_dataset/mic_syn_f'$i'_result.txt'
# done

# acdc
# for i in 1 2 3 4 5
# do
#     python miou_cal.py \
#     --gt_dir '/media/ywh/1/yanweihao/projects/uda/DAFormer/data/acdc/gt/train' \
#     --pred_dir '/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/debug_acdc/fusion'$i'_trainid' \
#     --devkit_dir '/media/ywh/1/yanweihao/projects/segmentation/tools/utils' \
#     --save_path 'miou_dataset/daformer_acdc_f'$i'_result.txt'
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
