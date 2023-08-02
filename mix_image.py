import cv2
import argparse

def blend_images(img_path1, img_path2, alpha, output_path):
    img1 = cv2.imread(img_path1)
    img2 = cv2.imread(img_path2)

    if img1.shape != img2.shape:
        raise ValueError("Input images must have the same dimensions.")

    blended_img = cv2.addWeighted(img1, alpha, img2, 1 - alpha, 0)

    cv2.imwrite(output_path, blended_img)
    print(f"Blended image saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Blend two images based on a blending coefficient.")
    parser.add_argument("--image1_path", type=str, default="/home/ywh/Documents/paper_writing/media/first_img/selected_samples/sample_3/fusion3.png")
    parser.add_argument("--image2_path", type=str, default="/home/ywh/Documents/paper_writing/media/first_img/selected_samples/sample_3/img.png")
    parser.add_argument("--blending_coefficient", type=float, default=0.5, help="Blending coefficient (between 0 and 1)")
    parser.add_argument("--output_path", type=str, default="/home/ywh/Documents/paper_writing/media/first_img/selected_samples/sample_3/fusion3_mix.png")
    args = parser.parse_args()

    # Check if the blending coefficient is within the valid range [0, 1]
    if not 0 <= args.blending_coefficient <= 1:
        raise ValueError("Blending coefficient must be between 0 and 1.")

    blend_images(args.image1_path, args.image2_path, args.blending_coefficient, args.output_path)
