
data_root="/media/ywh/Elements/dataset/GTA5_deeplab"
python del_damaged_img.py \
--image_folder "${data_root}/images" \
--label_folder "${data_root}/labels" \
--record_filename "${data_root}/del.txt"
