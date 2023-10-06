dataset_root="/media/ywh/Elements/dataset"
data1_folder="synthia_deeplab/RGB"
data2_folder="synthia/RGB"
output_file="synthia_deeplab/synthia_deeplab.csv"

python check_img_file.py \
--folder1 "${dataset_root}/${data1_folder}" \
--folder2 "${dataset_root}/${data2_folder}" \
--output_csv "${dataset_root}/${output_file}" \