# python color_trainid.py \
# --source_folder "/media/ywh/1/yanweihao/dataset/DensePASS/gtFine/val" \
# --gt_suffix ".png" \
# --save_folder "/media/ywh/1/yanweihao/dataset/DensePASS/gtFine/val_color" \

data_root="/media/ywh/1/yanweihao/projects/uda/Trans4PASS/adaptations/pseudo_DensePASS_Trans4PASS_v2_ms"
output_root="/media/ywh/1/yanweihao/projects/uda/Trans4PASS/adaptations/pseudo_DensePASS_Trans4PASS_v2_ms_color"
for folder in 'Canberra' 'Melbourne' 'Nottingham' 'Amsterdam' 'Manila' 'Capetown' 'Edinburgh' 'Jakarta' 'Zagreb' 'Auckland' 'Bangkok' 'Osaka' 'Saopaulo' 'Florence' 'Yokohama' 'Chicago' 'Glasgow' 'Helsinki' 'Turin' 'Singapore' 'Toronto' 'Oslo' 'Seoul' 'Barcelona' 'Lisbon' 'Sandiego' 'Buenosaires' 'Dublin' 'Moscow' 'Athens' 'Copenhagen' 'Montreal' 'Istanbul' 'Mexicocity' 'Stockholm' 'Marseille' 'Brussel' 'Bremen' 'Zurich' 'Hochiminhcity'
do
    python color_trainid.py \
    --source_folder "${data_root}/${folder}" \
    --gt_suffix "_labelTrainIds.png" \
    --save_folder "${output_root}/${folder}"
done


