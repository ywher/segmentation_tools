# image_root="/home/ywh/Documents/paper_writing/SAM4UDASS_paper/figure/experiment/gta_compare/sample_8"
image_root="/home/ywh/Documents/paper_writing/SAM4UDASS_paper/figure/experiment/syn_compare/sample_7"
image_root="/home/ywh/Documents/paper_writing/media/get_sam/selected_samples/sample_5"
python mix_image.py \
--image1_path "${image_root}/img.png" \
--image2_path "${image_root}/gt.png" \
--blending_coefficient 0.5 \
--output_path "${image_root}/mix.png" \

#alpha is the ratio of image2 in the mixed image