from PIL import Image
import cv2
def paste_color_from_image(source_path, color_path, color_list, output_path):
    # Open the images
    try:
        source_img = cv2.imread(source_path)
        color_img = cv2.imread(color_path)
        source_img = cv2.cvtColor(source_img, cv2.COLOR_BGR2RGB)
        color_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB)
        # source_img = Image.open(source_path)
        # color_img = Image.open(color_path)
    except FileNotFoundError as e:
        print("Error: One or both input images not found.")
        return
    
    # tar_img = cv2.imread(color_path)
    # tar_img = cv2.cvtColor(tar_img, cv2.COLOR_BGR2RGB)
    
    # Check if images have the same dimensions
    if source_img.shape != color_img.shape:
        color_img = cv2.resize(color_img, (source_img.shape[1], source_img.shape[0]))
        # print("Error: The two images must have the same dimensions.")
        # return

    # Create a list of RGB tuples from the color_list input
    rgb_colors = [tuple(map(int, color.split(','))) for color in color_list]
    
    for color in rgb_colors:
        print(color, 'begin')
        mask = (color_img == color).all(axis=-1)
        source_img[mask] = color
    source_img = cv2.cvtColor(source_img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_path, source_img)

    # Iterate over each pixel in the color image and paste it onto the source image
    # for x in range(source_img.width):
    #     for y in range(source_img.height):
    #         # Get the color of the current pixel in the color image
    #         color_pixel = color_img.getpixel((x, y))
    #         print(color_pixel)

    #         # Check if the color of the current pixel matches any color in the provided color list
    #         if color_pixel in rgb_colors:
    #             # Get the corresponding pixel from the source image
    #             source_pixel = source_img.getpixel((x, y))

    #             # Paste the color pixel onto the source image at the same position
    #             source_img.putpixel((x, y), color_pixel)

    # Save the result
    # source_img.save(output_path)
    print("Result saved successfully!")

# Example usage
if __name__ == "__main__":
    input_image_path = "ps.png"
    color_image_path = "pt.png"
    selected_colors = ["0,0,142", "250,170,30", "220,220,0"]  # Replace with your desired RGB color list
    output_image_path = "mix.png"

    paste_color_from_image(input_image_path, color_image_path,
                           selected_colors, output_image_path)
