# root_folder="/media/ywh/1/yanweihao/projects/uda/MIC/seg/work_dirs/local-exp86/230723_2306_csHR2csHR_768x768_target-only_daformer_sepaspp_mitb5_poly10warm_s0_424b8"
# folder_name="images_for_semantic1/pred_trainid_filter"
# python change_img_suffix.py \
# --folder_path "${root_folder}/${folder_name}" \
# --original_suffix "_trainID.png" \
# --new_suffix ".png" \

# densepass train
# data_root="/media/ywh/1/yanweihao/dataset/DensePASS/leftImg8bit/train"
# for folder in 'Canberra' 'Melbourne' 'Nottingham' 'Amsterdam' 'Manila' 'Capetown' 'Edinburgh' 'Jakarta' 'Zagreb' 'Auckland' 'Bangkok' 'Osaka' 'Saopaulo' 'Florence' 'Yokohama' 'Chicago' 'Glasgow' 'Helsinki' 'Turin' 'Singapore' 'Toronto' 'Oslo' 'Seoul' 'Barcelona' 'Lisbon' 'Sandiego' 'Buenosaires' 'Dublin' 'Moscow' 'Athens' 'Copenhagen' 'Montreal' 'Istanbul' 'Mexicocity' 'Stockholm' 'Marseille' 'Brussel' 'Bremen' 'Zurich' 'Hochiminhcity'
# do
#     python change_file_suffix.py \
#     echo "Processing ${folder}..." \
#     --folder_path "${data_root}/${folder}" \
#     --original_suffix ".jpg" \
#     --new_suffix ".png"
# done

# densepass val
# data_root="/media/ywh/1/yanweihao/projects/segmentation/segment-anything/tools/outputs/DensePASS_val_vith/gray"
# python change_file_suffix.py \
# --folder_path "${data_root}" \
# --original_suffix "_.png" \
# --new_suffix ".png"

# 
# data_root="/media/ywh/1/yanweihao/projects/uda/Trans4PASS/adaptations/pseudo_DensePASS_Trans4PASS_v2_mpa_val_ms_full/pred_label"
# python change_file_suffix.py \
# --folder_path "${data_root}" \
# --original_suffix ".png" \
# --new_suffix "_labelTrainIds.png"

# acdc
data_root="/media/ywh/1/yanweihao/projects/uda/HRDA_new/data/acdc/gt/train_pseudo_hrda_acdc_get_sam_mode0"
python change_file_suffix.py \
--folder_path "${data_root}" \
--original_suffix ".png" \
--new_suffix "_gt_labelTrainIds.png"