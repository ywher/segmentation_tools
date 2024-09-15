import os
import argparse
import cv2
import pandas as pd


class ImageViewer:
    def __init__(self, args):
        self.arg = args
        self.gt_folder = args.gt_folder
        self.pred_folder1 = args.pred_folder1
        self.pred_folder2 = args.pred_folder2
        self.gt_suffix = args.gt_suffix
        self.pred_suffix1 = args.pred_suffix1
        self.pred_suffix2 = args.pred_suffix2
        self.iou_info_file = args.iou_info_file
        self.record_file = args.record_file
        self.resolution = args.resolution  # [512, 1024]
        # print('self.resolution', self.resolution)  # [512, 1024]
        
        self.record_data = []
        self.image_names = []
        self.iou_changes = []
        self.current_index = 0

    def read_iou_info(self):
        df = pd.read_excel(self.iou_info_file)
        #df按照第四列的值从大到小进行排序
        df = df.sort_values(by=df.columns[4], ascending=False)
        self.image_names = df.iloc[:, 0].tolist()  # 自动忽略首行的内容
        # print(self.image_names[0])
        self.iou_changes = df.iloc[:, 4].tolist()

    def check_resolution(self, image):
        if image.shape[0] != self.resolution[0] or image.shape[1] != self.resolution[1]:  #h, w
            image = cv2.resize(image, (self.resolution[1], self.resolution[0]))  #w, h
        return image

    def show_images(self):
        # cv2.namedWindow("Image Viewer")
        while True:
            image_name = self.image_names[self.current_index]
            iou_change = self.iou_changes[self.current_index]
            iou_change = '{:.2f}'.format(iou_change)
            image_path = os.path.join(self.gt_folder, image_name + self.gt_suffix)
            pred_path1 = os.path.join(self.pred_folder1, image_name + self.pred_suffix1)
            pred_path2 = os.path.join(self.pred_folder2, image_name + self.pred_suffix2)

            gt_image = cv2.imread(image_path)
            gt_image = self.check_resolution(gt_image)
            pred_image1 = cv2.imread(pred_path1)
            pred_image1  = self.check_resolution(pred_image1)
            pred_image2 = cv2.imread(pred_path2)
            pred_image2 = self.check_resolution(pred_image2)

            combined_image = cv2.hconcat([gt_image, pred_image1, pred_image2])
            text = f'{image_name}   IoU Change: {iou_change}'
            cv2.putText(combined_image, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            
            cv2.imshow('combine', combined_image)

            key = cv2.waitKey(0)
            if key == ord("a"):
                self.current_index = max(0, self.current_index - 1)
            elif key == ord("d"):
                self.current_index = min(self.current_index + 1, len(self.image_names) - 1)
            elif key == 13:  # Enter key
                self.record_data.append([image_name, iou_change])
                # self.record_iou_change(image_name, iou_change)
            elif key == 27:  # Esc key
                break

        cv2.destroyAllWindows()
        if len(self.record_data) > 0:
            self.save_record()

    def save_record(self):
        record_df = pd.DataFrame(self.record_data, columns=['Image Name', 'IoU Change'])
        record_df.to_csv(self.record_file, index=False)
        print('Record saved to ', self.record_file)
    
    # def record_iou_change(self, image_name, iou_change):
    #     record_file = "record.csv"
    #     with open(record_file, "a") as file:
    #         file.write(f"{image_name},{iou_change}\n")
    #     print(f"Record saved: {record_file}")


def main():
    parser = argparse.ArgumentParser(description="Image Viewer with IoU Changes")
    parser.add_argument("--gt_folder", type=str, help="Path to ground truth image folder")
    parser.add_argument("--pred_folder1", type=str, help="Path to prediction result 1 folder")
    parser.add_argument("--pred_folder2", type=str, help="Path to prediction result 2 folder")
    parser.add_argument("--gt_suffix", type=str, help="Suffix of ground truth image files")
    parser.add_argument("--pred_suffix1", type=str, help="Suffix of prediction result 1 image files")
    parser.add_argument("--pred_suffix2", type=str, help="Suffix of prediction result 2 image files")
    parser.add_argument("--iou_info_file", type=str, help="Path to the IOU information Excel file")
    parser.add_argument("--record_file", type=str, default='iou_per_image/record.csv', help="Path to the record file")
    parser.add_argument("--resolution", type=int, nargs=2, help="Resolution of the images")
    args = parser.parse_args()

    image_viewer = ImageViewer(args)
    image_viewer.read_iou_info()
    image_viewer.show_images()


if __name__ == "__main__":
    main()
