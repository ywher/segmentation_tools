
root_path="/media/ywh/1/yanweihao/projects/uda/MIC/seg/work_dirs/local-exp86/230723_2306_csHR2csHR_768x768_target-only_daformer_sepaspp_mitb5_poly10warm_s0_424b8"
folder_path="images_for_semantic2/pred_trainid"
trainid_path="${root_path}/${folder_path}"
# --polygon_points 349 1199 349 990 366 990 517 942 699 924 707 1018 1267 975 1544 1011 1658 1059 1919 1067 1919 1199 343 1199 \

python filter_polygon.py \
--input_folder ${trainid_path} \
--polygon_points 231 1199 459 1163 571 1094 648 1067 767 1041 927 1016 1150 1002 1333 1007 1531 1036 1681 1097 1919 1097 1919 1199 231 1199 \
--label_id 0 \
--output_folder "${trainid_path}_filter"