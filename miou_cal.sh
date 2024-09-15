### cityscapes
city_gt="/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_all"
acdc_gt="/media/ywh/1/yanweihao/dataset/acdc/gt/train"
pass_val_gt="/media/ywh/1/yanweihao/dataset/DensePASS/gtFine/val"
dev_dir="/media/ywh/1/yanweihao/projects/segmentation/segmentation_tools/utils"
output_root="/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs"

################
### daformer ###
################
### gta->cityscapes
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

### gta UDA pseudo
# pred_path="/media/ywh/1/yanweihao/projects/uda/DAFormer/work_dirs/local-exp7/gta/4090_baseline/pred_trainid"
# output_folder="miou_dataset/daformer/gta/baseline"
# python miou_cal.py \
# --gt_dir ${city_gt} \
# --pred_dir "${pred_path}" \
# --devkit_dir "${dev_dir}" \
# --save_path "${output_folder}/4090_daformer_gta_uda_pseudo.txt"

# pred_path="/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/daformer/gta/daformer_gta_sam/fusion1_majority_trainid"
# output_folder="miou_dataset/daformer/gta/sgml"
# python miou_cal.py \
# --gt_dir ${city_gt} \
# --pred_dir "${pred_path}" \
# --devkit_dir "${dev_dir}" \
# --save_path "${output_folder}/da_majority_f1.txt"

# for folder in "fusion1_majority_trainid" "fusion1_trainid"
# do
#     pred_path="/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/daformer/gta/da_gta_baseline_majority_vs_sgml_get_sam_mode2/${folder}"
#     output_folder="miou_dataset/daformer/gta/sgml"
#     python miou_cal.py \
#     --gt_dir ${city_gt} \
#     --pred_dir "${pred_path}" \
#     --devkit_dir "${dev_dir}" \
#     --save_path "${output_folder}/da_gta_sam2_${folder}.txt"
# done

### syn->cityscapes
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

### cityscapes->acdc
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

############
### hrda ###
############
model="hrda"
### gta->cityscapes
dataset="gta"

# baseline
# output_folder="miou_dataset/${model}/${dataset}"
# python miou_cal.py \
# --gt_dir ${city_gt} \
# --pred_dir "/media/ywh/1/yanweihao/projects/uda/HRDA_new/work_dirs/local-exp40/231122_2129_gtaHR2csHR_1024x1024_dacs_a999_fdthings_rcs001-20_cpl2_hrda1-512-01_daformer_sepaspp_sl_mitb5_poly10warm_s0_0221d/pred_trainid" \
# --devkit_dir "${dev_dir}" \
# --save_path "${output_folder}/hrda_gta_base.txt"

# folder="hrda_gta_get_sam_mode0_confidence0.9"
# pred_folder="cityscapes/${model}/${dataset}/${folder}"
# output_folder="miou_dataset/${model}/${dataset}/${folder}"
# for i in 1 2 3
# do
#     python miou_cal.py \
#     --gt_dir ${city_gt} \
#     --pred_dir "${output_root}/${pred_folder}/fusion${i}_trainid" \
#     --devkit_dir "${dev_dir}" \
#     --save_path "${output_folder}/${model}_${dataset}_f${i}.txt"
# done

### cityscapes->acdc
# dataset="acdc"

# baseline
# output_folder="miou_dataset/${model}/${dataset}"
# python miou_cal.py \
# --gt_dir ${acdc_gt} \
# --pred_dir "/media/ywh/1/yanweihao/projects/uda/HRDA_new/work_dirs/local-exp49/231122_2220_csHR2acdcHR_1024x1024_dacs_a999_fdthings_rcs001-20_hrda1-512-01_daformer_sepaspp_sl_mitb5_poly10warm_s0_57b03/pred_trainid" \
# --devkit_dir "${dev_dir}" \
# --save_path "${output_folder}/hrda_acdc_base.txt"

# folder="hrda_acdc_get_sam_mode0"
# pred_folder="${dataset}/${model}/${folder}"
# output_folder="miou_dataset/${model}/${dataset}/${folder}"
# for i in 1 2 3
# do
#     python miou_cal.py \
#     --gt_dir ${acdc_gt} \
#     --pred_dir "${output_root}/${pred_folder}/fusion${i}_trainid" \
#     --devkit_dir "${dev_dir}" \
#     --save_path "${output_folder}/${model}_${dataset}_f${i}.txt"
# done

### syn->cityscapes
dataset="synthia"

# output_folder="miou_dataset/${model}/${dataset}"
# python miou_cal.py \
# --gt_dir ${city_gt} \
# --pred_dir "/media/ywh/1/yanweihao/projects/uda/HRDA_new/work_dirs/local-exp40/231123_2008_synHR2csHR_1024x1024_dacs_a999_fdthings_rcs001-20_cpl2_hrda1-512-01_daformer_sepaspp_sl_mitb5_poly10warm_s0_245a1/pred_trainid" \
# --devkit_dir "${dev_dir}" \
# --save_path "${output_folder}/hrda_synthia_base.txt" \
# --synthia

folder="hrda_syn_base"
pred_folder="cityscapes/${model}/${dataset}/${folder}"
output_folder="miou_dataset/${model}/${dataset}/${folder}"
for i in 1 2 3
do
    python miou_cal.py \
    --gt_dir ${city_gt} \
    --pred_dir "${output_root}/${pred_folder}/fusion${i}_trainid" \
    --devkit_dir "${dev_dir}" \
    --save_path "${output_folder}/${model}_${dataset}_f${i}.txt" \
    --synthia
done

###########
### mic ###
###########
###  gta
# pred_folder="cityscapes/mic/train_vith_32_86_92"
# output_folder="miou_dataset/mic/gta/train_vith_32_86_9b2"
# for i in 1 2 3
# do
#     python miou_cal.py \
#     --gt_dir ${city_gt} \
#     --pred_dir "${output_root}/${pred_folder}/fusion${i}_trainid" \
#     --devkit_dir "${dev_dir}" \
#     --save_path "${output_folder}/mic_gta_f${i}.txt"
# done

### gta UDA pseudo
# pred_path="/media/ywh/1/yanweihao/projects/uda/MIC/seg/work_dirs/local-exp80/230711_0741_gtaHR2csHR_1024x1024_dacs_a999_fdthings_rcs001-20_cpl2_m64-07-spta_hrda1-512-01_daformer_sepaspp_sl_mitb5_poly10warm_s0_139ce/pred_trainid"
# output_folder="miou_dataset/mic/gta/mic_base"
# python miou_cal.py \
# --gt_dir ${city_gt} \
# --pred_dir "${pred_path}" \
# --devkit_dir "${dev_dir}" \
# --save_path "${output_folder}/mic_gta_uda_pseudo.txt"

# for folder in "mic_gta_vith_default_base_8w_get_sam_mode0" #"mic_gta_vith_default_base_get_sam_mode1"
# do
#     for i in 1 2 3
#     do
#         python miou_cal.py \
#         --gt_dir "${city_gt}" \
#         --pred_dir "/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/mic/gta/${folder}/fusion${i}_trainid" \
#         --devkit_dir "${dev_dir}" \
#         --save_path "miou_dataset/mic/gta/${folder}/mic_gta_f${i}_result.txt"
#     done
# done

# python miou_cal.py \
# --gt_dir "${city_gt}" \
# --pred_dir "/media/ywh/1/yanweihao/projects/uda/MIC/seg/work_dirs/local-exp80/231105_0258_gtaHR2csHR_1024x1024_dacs_a999_fdthings_rcs001-20_cpl2_m64-07-spta_hrda1-512-01_daformer_sepaspp_sl_mitb5_poly10warm_s0_b9405/pred_trainid" \
# --devkit_dir "${dev_dir}" \
# --save_path "miou_dataset/mic/gta/mic_gta_vith_default_base_8w.txt"
# --save_path "miou_dataset/daformer/gta/da_gta_prev_best_new.txt"
# --save_path "miou_dataset/daformer/gta/da_gta_prev_best.txt"

##############
### sepico ###
##############
# python miou_cal.py \
# --gt_dir '/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_all' \
# --pred_dir '/media/ywh/1/yanweihao/projects/uda/SePiCo/work_dirs/local-exp1/230707_0324_dlv2_proj_r101v1c_sepico_DistCL-reg-w1.0-start-iter3000-tau100.0-l3-w1.0_rcs0.01_cpl_self_adamw_6e-05_pmT_poly10warm_1x2_40k_gta2cs_seed76_36629/pred_trainid' \
# --devkit_dir '/media/ywh/1/yanweihao/projects/segmentation/tools/utils' \
# --save_path 'miou_dataset/sepicov2_gta_base_result.txt'

############
### tufl ###
############
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

#####################
### transpass val ###
#####################
# passv2 baseline
# python miou_cal.py \
# --gt_dir "${pass_val_gt}" \
# --pred_dir "/media/ywh/1/yanweihao/projects/uda/Trans4PASS/adaptations/pseudo_DensePASS_val_Trans4PASS_v2_ms_full/pred_label" \
# --devkit_dir "${dev_dir}" \
# --save_path "miou_dataset/pass/pass_v2/pass_v2_base_val_new.txt"

# python miou_cal.py \
# --gt_dir "${pass_val_gt}" \
# --pred_dir "/media/ywh/1/yanweihao/projects/uda/Trans4PASS/adaptations/pseudo_DensePASS_Trans4PASS_v2_mpa_val_ms_full/pred_label" \
# --devkit_dir "${dev_dir}" \
# --save_path "miou_dataset/pass/pass_v2/vith_default_get_sam_mode_0_new/pass_v2_ssl_mpa.txt"

# for i in 1 2 3 4
# do
#     python miou_cal.py \
#     --gt_dir "${pass_val_gt}" \
#     --pred_dir "/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/DensePASS_val/passv2/vith_default_get_sam_mode_1/fusion${i}_trainid" \
#     --devkit_dir "${dev_dir}" \
#     --save_path "miou_dataset/pass/pass_v2/vith_default_get_sam_mode_1/pass_f${i}_result.txt"
# done




