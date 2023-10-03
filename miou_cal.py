import numpy as np
import argparse
import json
from PIL import Image
from os.path import join
import os
import time
import datetime
from get_iou import get_iou_data

#设标签宽W，长H，计算一张图片的hist矩阵
def fast_hist(label, predict, num_classes):
    #label 是转化成一维数组的标签，形状(H×W,)；
    #predict 是转化成一维数组的标签，形状(H×W,)；
    #num_classes 是类别数目，实数（在这里为19）
    '''
	核心代码
	'''
    keep = np.logical_not(label == 255)#keep是一个一维bool数组，形状(H×W,)；目的是找出标签中需要计算的类别（去掉了背景）
    # keep = np.logical_and((label >= 0), (label < num_classes))#keep是一个一维bool数组，形状(H×W,)；目的是找出标签中需要计算的类别（去掉了背景）
    # keep = (label >= 0) & (label < num_classes)#keep是一个一维bool数组，形状(H×W,)；目的是找出标签中需要计算的类别（去掉了背景）
    label = label[keep].astype(np.uint16)
    predict = predict[keep].astype(np.uint16)
    merge = label * num_classes + predict
    hist = np.bincount(merge, minlength=num_classes ** 2)#np.bincount计算了从0到n**2-1这n**2个数中每个数出现的次数，返回值形状(n, n)
    hist = hist.reshape((num_classes, num_classes))#将返回值变形为(n, n)
    return hist

#计算类别级的mIoU
def per_class_iu(hist):#分别为每个类别（在这里是19类）计算mIoU，hist的形状(n, n)
    '''
	核心代码
	'''
    num = np.diag(hist)
    den = (np.sum(hist, axis=1) + np.sum(hist, axis=0) - np.diag(hist))
    #对den中为0的项赋值为1，避免出现除以0的情况
    den = np.where(den == 0, 1, den)
    return num / den#矩阵的对角线上的值组成的一维数组/矩阵的所有元素之和，返回值形状(n,)

#类别级的recall
def classRecall(hist):
    return np.diag(hist) / (np.sum(hist, axis=1))

#类别级的precision
def classPrecision(hist):
    return np.diag(hist) / (np.sum(hist, axis=0))

#像素级的pixel accuracy
def pixelAccuracy(hist):
    return np.diag(hist).sum() / hist.sum()

def label_mapping(input, mapping):#主要是因为CityScapes标签里面原类别太多，这样做把其他类别转换成算法需要的类别（共19类）和背景（标注为255）
    output = np.copy(input)#先复制一下输入图像
    for ind in range(len(mapping)):
        output[input == mapping[ind][0]] = mapping[ind][1]#进行类别映射，最终得到的标签里面之后0-18这19个数加255（背景）
    return np.array(output, dtype=np.int64)#返回映射的标签
'''
compute_mIoU函数是以CityScapes图像分割验证集为例来计算mIoU值的
由于作者个人贡献的原因，本函数除了最主要的计算mIoU的代码之外，还完成了一些其他操作，
比如进行数据读取，因为原文是做图像分割迁移方面的工作，因此还进行了标签映射的相关工作，在这里笔者都进行注释。
大家在使用的时候，可以忽略原作者的数据读取过程，只需要注意计算mIoU的时候每张图片分割结果与标签要配对。
主要留意mIoU指标的计算核心代码即可。
'''
def compute_mIoU(gt_dir, pred_dir, num_classes, synthia, save_path, devkit_dir=''):#计算mIoU的函数
    """
    Compute IoU given the predicted colorized images and 
    """
    with open(join(devkit_dir, 'info.json'), 'r') as fp: #读取info.json，里面记录了类别数目，类别名称，标签映射方式等等。
      info = json.load(fp)
    num_classes = num_classes
    # num_classes = int(info['classes'])#读取类别数目，这里是19类，详见博客中附加的info.json文件
    print('Num classes', num_classes)#打印一下类别数目
    name_classes = info['label']#读取类别名称，详见博客中附加的info.json文件
    mapping = info['label2train']#读取标签映射方式，详见博客中附加的info.json文件
    hist = np.zeros((num_classes, num_classes), dtype=np.float32)#hist初始化为全零，在这里的hist的形状是[19, 19]

    #读取gt_dir和pred_dir中的图片路径
    gt_imgs = os.listdir(gt_dir)#获取gt_dir中所有图片的名称
    gt_imgs.sort()
    gt_imgs = [join(gt_dir, x) for x in gt_imgs]#获得验证集标签路径列表，方便直接读取
    
    pred_imgs = os.listdir(pred_dir)#获取pred_dir中所有图片的名称
    pred_imgs.sort()
    pred_imgs = [join(pred_dir, x) for x in pred_imgs]#获得验证集图像分割结果路径列表，方便直接读取
    
    assert len(gt_imgs) == len(pred_imgs)#确保验证集图片数量和验证集标签数量一致
    print(len(gt_imgs))#打印一下验证集图片数量

    # image_path_list = join(devkit_dir, 'val.txt')#在这里打开记录验证集图片名称的txt
    # label_path_list = join(devkit_dir, 'label.txt')#在这里打开记录验证集标签名称的txt
    # gt_imgs = open(label_path_list, 'r').read().splitlines()#获得验证集标签名称列表s
    # pred_imgs = open(image_path_list, 'r').read().splitlines()#获得验证集图像分割结果名称列表
    
    start_time = time.time()
    total_iterations = len(gt_imgs)
    for ind in range(total_iterations):#读取每一个（图片-标签）对
        pred = np.array(Image.open(pred_imgs[ind]))#读取一张图像分割结果，转化成numpy数组
        label = np.array(Image.open(gt_imgs[ind]))#读取一张对应的标签，转化成numpy数组
        # label = label_mapping(label, mapping)#进行标签映射（因为没有用到全部类别，因此舍弃某些类别），可忽略
        if len(label.flatten()) != len(pred.flatten()):#如果图像分割结果与标签的大小不一样，这张图片就不计算
            print('Skipping: len(gt) = {:d}, len(pred) = {:d}, {:s}, {:s}'.format(len(label.flatten()), len(pred.flatten()), gt_imgs[ind], pred_imgs[ind]))
            continue
        hist += fast_hist(label.flatten(), pred.flatten(), num_classes)#对一张图片计算19×19的hist矩阵，并累加
        # hist += fast_hist(label, pred, num_classes)
        if ind > 0 and ind % 100 == 0:#每计算100张就输出一下目前已计算的图片中所有类别平均的mIoU值
            eta = int((time.time() - start_time) / (ind + 1) * (total_iterations - ind - 1))
            eta_str = str(datetime.timedelta(seconds=eta))
            ious = per_class_iu(hist) #计算所有验证集图片的逐类别mIoU值
            if synthia:
                # 0-8, 10-13, 15, 17, 18
                miou = np.sum(ious[[0,1,2,3,4,5,6,7,8,10,11,12,13,15,17,18]]) / 16 * 100
            else:
                miou = np.mean(ious) * 100
            print('{:d} / {:d}, mIoU: {:0.2f}, eta: {}'.format(ind, len(gt_imgs), miou, eta_str))
    
    mIoUs = per_class_iu(hist)#计算所有验证集图片的逐类别mIoU值
    # print('mIoU', mIoUs)
    CRecalls=classRecall(hist)
    CPrecisions=classPrecision(hist)
    PA=pixelAccuracy(hist)
    
    
    if synthia:
        classes_index = [0,1,2,3,4,5,6,7,8,10,11,12,13,15,17,18]
        mIoUs = mIoUs[classes_index]
        CRecalls = CRecalls[classes_index]
        CPrecisions = CPrecisions[classes_index]
        num_classes = 16
        name_classes = name_classes[:9] + name_classes[10:14] + name_classes[15:16] + name_classes[17:19]
    #按照类别一次输出一下mIoU值和mRecall值
    for ind_class in range(num_classes):#逐类别输出一下IoU值
        cls_name = name_classes[ind_class] if len(name_classes[ind_class]) <= 4 else name_classes[ind_class][:4]
        print('Iou===>' + cls_name + ':\t' + str(round(mIoUs[ind_class] * 100, 2)))
    print('===> mIoU: ' + str(round(np.mean(mIoUs) * 100, 2)))#在所有验证集图像上求所有类别平均的mIoU值，计算时忽略NaN值
    print('')
    for ind_class in range(num_classes):#逐类别输出一下CRecall值
        cls_name = name_classes[ind_class] if len(name_classes[ind_class]) <= 4 else name_classes[ind_class][:4]
        print('CRecall===>' + cls_name + ':\t' + str(round(CRecalls[ind_class] * 100, 2)))
    print('===> mCRecall: ' + str(round(np.mean(CRecalls) * 100, 2)))
    print('')
    for ind_class in range(num_classes):#逐类别输出一下CPrecision值
        cls_name = name_classes[ind_class] if len(name_classes[ind_class]) <= 4 else name_classes[ind_class][:4]
        print('CPrecision===>' + cls_name + ':\t' + str(round(CPrecisions[ind_class] * 100, 2)))
    print('===> mCRecall: ' + str(round(np.mean(CPrecisions) * 100, 2)))
    print('')
    print('===> PA: ' + str(round(PA * 100, 2)))
    
    # check save_path exists
    if not os.path.exists(os.path.dirname(save_path)):
        os.makedirs(os.path.dirname(save_path))
        
    ##保存mIoU值，CPA值，PA值
    with open(save_path, 'w') as f:
        f.write('===> mIoU: ' + str(round(np.mean(mIoUs) * 100, 2)) + '\n')
        for cls in range(num_classes):
            cls_name = name_classes[cls] if len(name_classes[cls]) <= 4 else name_classes[cls][:4]
            f.write('===> ' + cls_name + ':\t' + str(round(mIoUs[cls] * 100, 2)) + '\n')
        f.write('\n')
        
        f.write('===> mRecall: ' + str(round(np.mean(CRecalls) * 100, 2)) + '\n')
        for cls in range(num_classes):
            cls_name = name_classes[cls] if len(name_classes[cls]) <= 4 else name_classes[cls][:4]
            f.write('===> ' + cls_name + ':\t' + str(round(CRecalls[cls] * 100, 2)) + '\n')
        f.write('\n')
        
        f.write('===> mPrecision: ' + str(round(np.mean(CPrecisions) * 100, 2)) + '\n')
        for cls in range(num_classes):
            cls_name = name_classes[cls] if len(name_classes[cls]) <= 4 else name_classes[cls][:4]
            f.write('===> ' + cls_name + ':\t' + str(round(CPrecisions[cls] * 100, 2)) + '\n')
        f.write('\n')
        
        f.write('===> PA: ' + str(round(PA * 100, 2)) + '\n')
        for cls in range(num_classes):
            cls_name = name_classes[cls] if len(name_classes[cls]) <= 4 else name_classes[cls][:4]
            f.write('===> ' + cls_name + ':\t' + str(round(PA * 100, 2)) + '\n')
    f.close()
    return mIoUs


def main(args):
    compute_mIoU(args.gt_dir, args.pred_dir, args.num_classes, args.synthia, args.save_path, args.devkit_dir)  # 执行计算mIoU的函数
    get_iou_data(args.save_path, args.synthia)  # 将保存的结果输出到csv文件中

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--gt_dir', type=str, help='directory which stores CityScapes val gt images',
                        default='/media/yons/pool1/ywh/dataset/cityscapes/gtFine/train_all')#设置gt_dir参数，存放验证集分割标签的文件夹
    parser.add_argument('--pred_dir', type=str, help='directory which stores CityScapes val pred images',
                        default='/media/yons/pool1/ywh/dataset/cityscapes/gtFine/train_all')#设置pred_dir参数，存放验证集分割结果的文件夹
    parser.add_argument('--devkit_dir', type=str, help='base directory of cityscapes',
                        default='/media/yons/pool1/ywh/projects/Segmentation/tools/utils')#设置devikit_dir文件夹，里面有记录图片与标签名称及其他信息的txt文件
    parser.add_argument('--num_classes', type=int, default=19, help='number of classes')
    parser.add_argument('--save_path', type=str, default='./eval_result.txt', help='path to save result txt file')
    parser.add_argument('--synthia', action='store_true', help='whether to evaluate on synthia')
    args = parser.parse_args()
    main(args)#执行主函数
