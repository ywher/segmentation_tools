### cityscapes
city_gt="/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_all"
acdc_gt="/media/ywh/1/yanweihao/dataset/acdc/gt/train"
pass_gt="/media/ywh/1/yanweihao/dataset/DensePASS/leftImg8bit/val"
dev_dir="/media/ywh/1/yanweihao/projects/segmentation/segmentation_tools/utils"
output_root="/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs"

### daformer gta->cityscapes
# for folder in "train_vitb_default" "train_vitl_default"
# do
#     pred_folder="cityscapes/daformer/${folder}"
#     output_folder="miou_dataset/daformer/gta/${folder}"
#     for i in 1 2 3
#     do
#         python miou_cal.py \
#         --gt_dir ${city_gt} \
#         --pred_dir "${output_root}/${pred_folder}/fusion${i}_trainid" \
#         --devkit_dir "${dev_dir}" \
#         --save_path "${output_folder}/daformer_gta_f${i}.txt"
#     done
# done

### daformer syn->cityscapes
# for folder in "da_syn_vith_32_86_92_mode_0" # "da_syn_vith_32_86_92_mode_2" # "da_syn_vith_32_86_92_mode_2"
# do 
#     pred_folder="cityscapes/daformer/${folder}"
#     output_folder="miou_dataset/daformer/syn/${folder}"
#     for i in 1 2 3
#     do
#         python miou_cal.py \
#         --gt_dir ${city_gt} \
#         --pred_dir "${output_root}/${pred_folder}/fusion${i}_trainid" \
#         --devkit_dir "${dev_dir}" \
#         --save_path "${output_folder}/daformer_syn_f${i}.txt" \
#         --synthia
#     done
# done

### daformer gta UDA pseudo
# pred_path="/media/ywh/1/yanweihao/projects/uda/DAFormer/work_dirs/local-exp7/gta/230522_2312_gta2cs_dacs_a999_fdthings_rcs001_cpl_daformer_sepaspp_mitb5_poly10warm_s0_ea659/pred_trainid"
# output_folder="miou_dataset/daformer/gta"
# python miou_cal.py \
# --gt_dir ${city_gt} \
# --pred_dir "${pred_path}" \
# --devkit_dir "${dev_dir}" \
# --save_path "${output_folder}/daformer_gta_uda_pseudo.txt"

### mic gta
# pred_folder="cityscapes/mic/train_vith_32_86_92"
# output_folder="miou_dataset/mic/gta/train_vith_32_86_92"
# for i in 1 2 3
# do
#     python miou_cal.py \
#     --gt_dir ${city_gt} \
#     --pred_dir "${output_root}/${pred_folder}/fusion${i}_trainid" \
#     --devkit_dir "${dev_dir}" \
#     --save_path "${output_folder}/mic_gta_f${i}.txt"
# done

# pred_folder="cityscapes/mic/train_vith_32_86_92_new_get_sam"
# output_folder="miou_dataset/mic/gta/train_vith_32_86_92_new_get_sam"
# for i in 1 2 3
# do
#     python miou_cal.py \
#     --gt_dir ${city_gt} \
#     --pred_dir "${output_root}/${pred_folder}/fusion${i}_trainid" \
#     --devkit_dir "${dev_dir}" \
#     --save_path "${output_folder}/mic_gta_f${i}.txt"
# done

### mic gta UDA pseudo
# pred_path="/media/ywh/1/yanweihao/projects/uda/MIC/seg/work_dirs/local-exp80/230711_0741_gtaHR2csHR_1024x1024_dacs_a999_fdthings_rcs001-20_cpl2_m64-07-spta_hrda1-512-01_daformer_sepaspp_sl_mitb5_poly10warm_s0_139ce/pred_trainid"
# output_folder="miou_dataset/mic/gta/mic_base"
# python miou_cal.py \
# --gt_dir ${city_gt} \
# --pred_dir "${pred_path}" \
# --devkit_dir "${dev_dir}" \
# --save_path "${output_folder}/mic_gta_uda_pseudo.txt"

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
# for alpha in 0.01 0.01_mode3 0.05 0.05_mode3 0.1 0.15 0.2 0.25 0.3 0.35 0.4
# do
#     for i in 1 2 3
#     do
#         python miou_cal.py \
#         --gt_dir "${city_gt}" \
#         --pred_dir "/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/daformer/alpha_ablation/daformer_gta_alpha${alpha}/fusion${i}_trainid" \
#         --devkit_dir "${dev_dir}" \
#         --save_path "miou_dataset/daformer/gta/alpha_ablation/${alpha}/daformer_gta_f${i}_result_alpha${alpha}.txt"
#     done
# done

sam_name="fast_sam_default_get_sam_mode2"
for i in 1 2 3
do
    python miou_cal.py \
    --gt_dir "${city_gt}" \
    --pred_dir "/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/daformer/gta/${sam_name}/fusion${i}_trainid" \
    --devkit_dir "${dev_dir}" \
    --save_path "miou_dataset/daformer/gta/sam_params/${sam_name}/daformer_gta_f${i}_result.txt"
done

# for ratio in 1 # 0.9999
# do
#     for i in 1 2 3
#     do
#         python miou_cal.py \
#         --gt_dir "${city_gt}" \
#         --pred_dir "/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/daformer/adaptive_ratio/da_gta_vith_32_86_92_adaptive_4_${ratio}/fusion${i}_trainid" \
#         --devkit_dir "${dev_dir}" \
#         --save_path "miou_dataset/daformer/gta/adaptive_ratio/adaptive_4_${ratio}/daformer_gta_f${i}_result.txt"
#     done
# done

# for i in 1 2 3
# do
#     python miou_cal.py \
#     --gt_dir '/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_all' \
#     --pred_dir '/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/daformer/daformer_gta_sam/fusion'$i'_majority_trainid' \
#     --devkit_dir '/media/ywh/1/yanweihao/projects/segmentation/tools/utils' \
#     --save_path 'miou_dataset/daformer_gta_f'$i'_result_majority.txt'
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
# for i in 1 2 3
# do
#     python miou_cal.py \
#     --gt_dir '/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_all' \
#     --pred_dir '/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/tufl/tufl_synthia/fusion'$i'_trainid' \
#     --devkit_dir '/media/ywh/1/yanweihao/projects/segmentation/tools/utils' \
#     --save_path 'miou_dataset/tufl_syn_f'$i'_result.txt'
# done
# python miou_cal.py \
# --gt_dir '/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_all' \
# --pred_dir '/media/ywh/1/yanweihao/projects/uda/BiSeNet-uda/outputs/Synthia_deeplab_BiSeNet_20kunsup_focal_0.8_0.05/pred/pred_trainid_transfer' \
# --devkit_dir '/media/ywh/1/yanweihao/projects/segmentation/tools/utils' \
# --save_path 'miou_dataset/tufl_syn_base_result.txt'

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
# model="daformer"
# for folder in "vith_32_86_92_mode_0" "vith_32_86_92_mode_1" "vith_32_86_92_mode_2"
# do
#     pred_folder="ACDC/${model}/${folder}"
#     output_folder="miou_dataset/${model}/acdc/${folder}"
#     for i in 1 2 3
#     do
#         python miou_cal.py \
#         --gt_dir ${acdc_gt} \
#         --pred_dir "${output_root}/${pred_folder}/fusion${i}_trainid" \
#         --devkit_dir "${dev_dir}" \
#         --save_path "${output_folder}/${model}_acdc_f${i}.txt"
#     done
# done

# python miou_cal.py \
# --gt_dir '/media/ywh/1/yanweihao/projects/uda/DAFormer/data/acdc/gt/train' \
# --pred_dir '/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/ACDC/tufl_acdc/selected_trainid' \
# --devkit_dir '/media/ywh/1/yanweihao/projects/segmentation/tools/utils' \
# --save_path 'miou_dataset/tufl_acdc_selected.txt'

# python miou_cal.py \
# --gt_dir '/media/ywh/1/yanweihao/projects/uda/DAFormer/data/acdc/gt/train' \
# --pred_dir '/media/ywh/1/yanweihao/projects/uda/BiSeNet-uda/outputs/acdc/CityScapes_ACDC_BiSeNet_20kunsup_focal_0.8_0.05_paste_mode_Single_1/pred_train/pred_trainid' \
# --devkit_dir '/media/ywh/1/yanweihao/projects/segmentation/tools/utils' \
# --save_path './tufl_acdc_base_result.txt'

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
