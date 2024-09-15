# sjtu images
# for i in 1 2 7 9
# do
#     python img_2_vdo.py \
#     --image_folder "/media/ywh/1/yanweihao/dataset/sjtu/image/train/sjtu"$i \
#     --image_suffix ".png" \
#     --video_output "/media/ywh/1/yanweihao/dataset/sjtu/image/train/sjtu"$i".mp4" \
#     --frame_rate 30 
# done


# tufl s1
# TEST_ROOT="/media/ywh/1/yanweihao/projects/uda/BiSeNet-uda/outputs/CityScapes_SJTU_BiSeNet_20kunsup_focal_0.8_0.05_paste_mode_Single_1/pred_train_20k/pred_color/"
# for i in 1 2 7 9
# do
#     python img_2_vdo.py \
#     --image_folder "${TEST_ROOT}sjtu${i}" \
#     --image_suffix ".png" \
#     --video_output "${TEST_ROOT}sjtu${i}.mp4" \
#     --frame_rate 30 
# done

# cityscapes video0
# video_root='/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/leftImg8bit_demoVideo/leftImg8bit/demoVideo'
# for target_scene in 'stuttgart_00' 'stuttgart_01' 'stuttgart_02'
# do 
#     echo $target_scene 'begin'
#     python img_2_vdo.py \
#     --image_folder "${video_root}/${target_scene}" \
#     --image_suffix ".png" \
#     --frame_rate 30 \
#     --video_output "${video_root}/${target_scene}.mp4"
# done

# tufl for city video
# video_root='/home/ywh/Documents/paper_writing/media/video_demo/city_v1'
# for target_scene in 'tufl_source' 'tufl_base' 'tufl_best' 'tufl_best_ms'
# do 
#     echo $target_scene 'begin'
#     python img_2_vdo.py \
#     --image_folder "${video_root}/${target_scene}/color" \
#     --image_suffix ".png" \
#     --frame_rate 30 \
#     --video_output "${video_root}/${target_scene}.mp4"
# done

for scene in "sjtu9_fusion"  #  "sjtu2_fusion" "sjtu7_fusion" 
do
    python img_2_vdo.py \
    --image_folder "/media/cyber-fx/ywh_disk/projects/SAM4UDASS/outputs/${scene}/horizontal" \
    --image_suffix ".png" \
    --frame_rate 30 \
    --video_output "/media/cyber-fx/ywh_disk/projects/SAM4UDASS/outputs/${scene}/horizontal.mp4"
done

