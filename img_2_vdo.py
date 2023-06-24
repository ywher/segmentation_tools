import os
import cv2
import argparse
import tqdm

def images_to_video(image_folder, image_suffix, video_output, frame_rate):
    # 获取文件夹中的所有图像文件
    image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(image_suffix)])

    # 获取第一张图像的宽度和高度
    first_image = cv2.imread(os.path.join(image_folder, image_files[0]))
    height, width, _ = first_image.shape

    # 创建视频编码器
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(video_output, fourcc, frame_rate, (width, height))

    # 逐个将图像写入视频
    bar = tqdm.tqdm(total=len(image_files))
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        image = cv2.imread(image_path)
        video.write(image)
        bar.update(1)
    bar.close()

    # 释放资源
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert images to video")
    parser.add_argument("--image_folder", help="Path to the image folder")
    parser.add_argument("--image_suffix", default='.png',help="Suffix of the images")
    parser.add_argument("--video_output", help="Output video path")
    parser.add_argument("--frame_rate", type=int, help="Frame rate of the output video")

    args = parser.parse_args()

    images_to_video(args.image_folder, args.image_suffix, args.video_output, args.frame_rate)
