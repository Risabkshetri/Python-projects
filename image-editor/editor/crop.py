from PIL import Image

def crop_image(input_path, output_path, left, top, right, bottom):
    with Image.open(input_path) as img:
        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.save(output_path)
        print(f"Image cropped and saved to {output_path}")
