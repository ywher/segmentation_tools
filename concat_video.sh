# for scene in scene2 scene3
# do
#     python concat_video.py \
#     --inputs "/media/ywh/1/yanweihao/projects/segmentation/segment-anything-old/tools/outputs/kyxz_mix/${scene}/${scene}_original.mp4" \
#     "/media/ywh/1/yanweihao/projects/segmentation/segment-anything-old/tools/outputs/kyxz_mix/${scene}/${scene}.mp4" \
#     --interval 5 \
#     --output "/media/ywh/1/yanweihao/projects/segmentation/segment-anything-old/tools/outputs/kyxz_mix/${scene}/${scene}_concat.mp4"
# done

# video_root1='/media/ywh/1/yanweihao/dataset/sjtu/image/train/'
# video_root2='/media/ywh/1/yanweihao/projects/uda/BiSeNet-uda/outputs/CityScapes_SJTU_BiSeNet_20kunsup_focal_0.8_0.05/pred_train_10k/pred_color/'
# video_root3='/media/ywh/1/yanweihao/projects/uda/BiSeNet-uda/outputs/CityScapes_SJTU_BiSeNet_20kunsup_focal_0.8_0.05/pred_train_20k/pred_color/'
# # video_root3='/media/ywh/1/yanweihao/projects/uda/BiSeNet-uda/outputs/CityScapes_SJTU_BiSeNet_20kunsup_focal_0.8_0.05_paste_mode_Single_1/pred_train_20k/pred_color/'

# for target_scene in 'sjtu1.mp4' 'sjtu2.mp4' 'sjtu7.mp4' 'sjtu9.mp4'
# do 
#     echo $target_scene 'begin'
#     python concat_video.py \
#     --inputs "${video_root1}${target_scene}" "${video_root2}${target_scene}" "${video_root3}${target_scene}" \
#     --interval 10 \
#     --output "${video_root2}concat${target_scene}"
# done

### tufl for city video
# for scene in 'stuttgart_00' 'stuttgart_01' 'stuttgart_02'
# do
#     video_root1="/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/leftImg8bit_demoVideo/leftImg8bit/demoVideo/"
#     video_root2="/home/ywh/Documents/paper_writing/media/video_demo/${scene}/"
#     python concat_video.py \
#     --inputs "${video_root1}${scene}.mp4" "${video_root2}tufl_source.mp4" "${video_root2}tufl_base2.mp4" "${video_root2}tufl_base.mp4" "${video_root2}tufl_best.mp4" "${video_root2}tufl_best_ms.mp4" \
#     --interval 10 \
#     --output "${video_root2}concat.mp4" \
#     --resize 512 256 \
#     --columns 2
# done

### daformer for city video
method="daformer"
video_root1="/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/leftImg8bit_demoVideo/leftImg8bit/demoVideo"
for scene in "stuttgart_00" "stuttgart_01" "stuttgart_02"
do
    video_root2="/home/ywh/Documents/paper_writing/media/video_demo/${scene}/${method}"
    python concat_video.py \
    --inputs "${video_root1}/${scene}.mp4" "${video_root2}/da_source_color.mp4" "${video_root2}/da_base_color.mp4" "${video_root2}/da_best_color.mp4" \
    --interval 10 \
    --output "${video_root2}/concat.mp4" \
    --resize 512 256 \
    --columns 2
done