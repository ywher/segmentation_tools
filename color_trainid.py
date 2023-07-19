from cityscapesscripts.helpers.labels import trainId2label as trainid2label
import numpy as np
import os
import cv2
import tqdm


def color_segmentation(segmentation):
    # get the color segmentation result, initial the color segmentation result with black (0,0,0)
    # input: segmentation [h, w]
    color_segmentation = np.zeros((segmentation.shape[0], segmentation.shape[1], 3), dtype=np.uint8)
    train_ids = np.unique(segmentation)
    for train_id in train_ids:
        color_segmentation[segmentation == train_id] = trainid2color(train_id)
    return color_segmentation


def trainid2color(trainid):
    '''
    function: convert trainID to color in cityscapes
    input: trainid
    output: color
    '''
    # if the input is a number in np.uint8, it means it is a trainid
    if type(trainid) == np.uint8:
        label_object = trainid2label[trainid]
        return label_object.color[::-1]
    else:
        color_mask = np.zeros((trainid.shape[0], 3), dtype=np.uint8)
        for i in range(trainid.shape[0]):
            label_object = trainid2label[trainid[i]]
            color_mask[i] = label_object.color[::-1]
        return color_mask


def main(source_folder, gt_suffix, save_folder):
    source_files = os.listdir(source_folder)
    source_files = [file for file in source_files if file.endswith(gt_suffix)]
    source_files.sort()
    if not os.path.exists(save_folder):
        os.makedirs(save_folder, exist_ok=True)

    bar = tqdm.tqdm(total=len(source_files))
    for file in source_files:
        segmentation = cv2.imread(os.path.join(source_folder, file), cv2.IMREAD_GRAYSCALE)
        color_segmentation_ = color_segmentation(segmentation)
        cv2.imwrite(os.path.join(save_folder, file.replace(gt_suffix, '.png')), color_segmentation_)
        bar.update(1)
    print('Done')


if __name__ == '__main__':
    source_folder = '/media/ywh/1/yanweihao/projects/uda/MIC/seg/work_dirs/local-exp80/230716_1343_gtaHR2csHR_1024x1024_dacs_a999_fdthings_rcs001-20_cpl2_m64-07-spta_hrda1-512-01_daformer_sepaspp_sl_mitb5_poly10warm_s0_ea911/pred_trainid'
    # gt_suffix = '_labelTrainIds.png'
    gt_suffix = '.png'
    save_folder = '/media/ywh/1/yanweihao/projects/uda/MIC/seg/work_dirs/local-exp80/230716_1343_gtaHR2csHR_1024x1024_dacs_a999_fdthings_rcs001-20_cpl2_m64-07-spta_hrda1-512-01_daformer_sepaspp_sl_mitb5_poly10warm_s0_ea911/pred_trainid_color'
    main(source_folder, gt_suffix, save_folder)  # 00001_labelTrainIds.png
