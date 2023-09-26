root_folder="/media/ywh/1/yanweihao/projects/uda/MIC/seg/work_dirs/local-exp86/230723_2306_csHR2csHR_768x768_target-only_daformer_sepaspp_mitb5_poly10warm_s0_424b8"
folder_name="images_for_semantic1/pred_trainid_filter"
python change_img_suffix.py \
--folder_path "${root_folder}/${folder_name}" \
--original_suffix "_trainID.png" \
--new_suffix ".png" \