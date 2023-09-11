
# for scene in "stuttgart_00" "stuttgart_01" "stuttgart_02"
# do
#     for mode in "da_source" "da_base" "da_best"
#     do
#         python color_trainid.py \
#         --source_folder "/home/ywh/Documents/paper_writing/media/video_demo/${scene}/daformer/${mode}" \
#         --gt_suffix ".png" \
#         --save_folder "/home/ywh/Documents/paper_writing/media/video_demo/${scene}/daformer/${mode}_color"
#     done
# done

root_folder="/media/ywh/1/yanweihao/projects/uda/MIC/seg/work_dirs/local-exp86/230723_2306_csHR2csHR_768x768_target-only_daformer_sepaspp_mitb5_poly10warm_s0_424b8"
python color_trainid.py \
--source_folder "${root_folder}/pred_trainid_filter" \
--gt_suffix ".png" \
--save_folder "${root_folder}/pred_color_filter"