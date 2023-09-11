trainid_path="/media/ywh/1/yanweihao/projects/uda/MIC/seg/work_dirs/local-exp86/230723_2306_csHR2csHR_768x768_target-only_daformer_sepaspp_mitb5_poly10warm_s0_424b8/pred_trainid"

python filter_polygon.py \
--input_folder ${trainid_path} \
--polygon_points 349 1199 349 990 366 990 517 942 699 924 707 1018 1267 975 1544 1011 1658 1059 1919 1067 1919 1199 343 1199 \
--label_id 0 \
--output_folder "${trainid_path}_filter"