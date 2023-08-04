
for scene in "stuttgart_00" "stuttgart_01" "stuttgart_02"
do
    for mode in "da_source" "da_base" "da_best"
    do
        python color_trainid.py \
        --source_folder "/home/ywh/Documents/paper_writing/media/video_demo/${scene}/daformer/${mode}" \
        --gt_suffix ".png" \
        --save_folder "/home/ywh/Documents/paper_writing/media/video_demo/${scene}/daformer/${mode}_color"
    done
done