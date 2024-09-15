import os
import cv2
import argparse
from tqdm import tqdm
import numpy as np

def create_polygon_mask(image_shape, polygon_points):
    mask = np.zeros(image_shape, dtype=np.uint8)
    cv2.fillPoly(mask, [np.array(polygon_points)], 255)
    return mask

def apply_polygon_to_images(input_folder, polygon_points, label_id, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    # 创建多边形掩码
    image = cv2.imread(os.path.join(input_folder, os.listdir(input_folder)[0]), cv2.IMREAD_GRAYSCALE)
    mask = create_polygon_mask(image.shape, polygon_points)
    for image_file in tqdm(os.listdir(input_folder), desc="Processing images"):
        if image_file.endswith(".png"):  # 根据您的需要更改文件扩展名
            image_path = os.path.join(input_folder, image_file)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # 将标签ID应用于多边形内的像素
            image[mask == 255] = label_id

            # 保存结果图像
            output_path = os.path.join(output_folder, image_file)
            cv2.imwrite(output_path, image)

def main():
    parser = argparse.ArgumentParser(description="Apply a polygon to semantic label images.")
    parser.add_argument("--input_folder", type=str, help="Path to the folder containing original semantic label images")
    parser.add_argument("--polygon_points", type=int, nargs="+", help="Polygon points (x1 y1 x2 y2 ... xn yn)")
    parser.add_argument("--label_id", type=int, help="Semantic label ID to apply within the polygon")
    parser.add_argument("--output_folder", type=str, help="Path to the output folder")

    args = parser.parse_args()
    polygon_points = [(int(args.polygon_points[i]), int(args.polygon_points[i + 1])) for i in range(0, len(args.polygon_points), 2)]
    print("Polygon points: {}".format(polygon_points))

    apply_polygon_to_images(args.input_folder, polygon_points, args.label_id, args.output_folder)

if __name__ == "__main__":
    main()
