import os
from editor.resize import resize_image
from editor.crop import crop_image
from editor.filters import apply_filter

def main():
    print("Welcome to the Image Editor!")
    print("Options:")
    print("1. Resize Image")
    print("2. Crop Image")
    print("3. Apply Filter")
    choice = int(input("Enter your choice: "))

    input_path = input("Enter the input image path: ")
    output_path = input("Enter the output image path: ")

    if not os.path.exists(input_path):
        print("Input file does not exist.")
        return

    if choice == 1:
        width = int(input("Enter the width: "))
        height = int(input("Enter the height: "))
        resize_image(input_path, output_path, width, height)
    elif choice == 2:
        left = int(input("Enter the left coordinate: "))
        top = int(input("Enter the top coordinate: "))
        right = int(input("Enter the right coordinate: "))
        bottom = int(input("Enter the bottom coordinate: "))
        crop_image(input_path, output_path, left, top, right, bottom)
    elif choice == 3:
        filter_name = input("Enter the filter (BLUR, CONTOUR, DETAIL): ")
        apply_filter(input_path, output_path, filter_name)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
