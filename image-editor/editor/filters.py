from PIL import Image, ImageFilter

def apply_filter(input_path, output_path, filter_name):
    with Image.open(input_path) as img:
        if filter_name == "BLUR":
            filtered_img = img.filter(ImageFilter.BLUR)
        elif filter_name == "CONTOUR":
            filtered_img = img.filter(ImageFilter.CONTOUR)
        elif filter_name == "DETAIL":
            filtered_img = img.filter(ImageFilter.DETAIL)
        else:
            print("Filter not recognized. Using original image.")
            filtered_img = img
        filtered_img.save(output_path)
        print(f"Filter applied and saved to {output_path}")
