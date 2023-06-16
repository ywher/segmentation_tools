python iou_perimg.py \
--pred_folder '/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/train_fusion_gta_daformer_base2/trainID_bg' \
--gt_folder '/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_all' \
--num_classes 19 \
--pred_suffix '_leftImg8bit.png' \
--gt_suffix '_gtFine_labelTrainIds.png' \
--output_file 'iou_per_image/daformer_gta_basef1_newrefine.csv' \

#/media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/train_fusion_gta_0/trainID_bg
# /media/ywh/1/yanweihao/projects/segmentation/segment-anything/outputs/cityscapes/train_fusion_gta_1/trainID_bg