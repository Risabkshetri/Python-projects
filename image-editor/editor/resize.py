from PIL import Image

def resize_image(input_path, output_path, width, height):
    with Image.open(input_path) as img:
        resized_img = img.resize((width, height))
        resized_img.save(output_path)
        print(f"Image resized and saved to {output_path}")
