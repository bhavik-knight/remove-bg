import re
import sys
from pathlib import Path

from PIL import Image
from rembg import remove


def main():
    current_path: Path = Path(__file__)

    file_path: str = None
    if len(sys.argv) == 2:
        file_path = str.strip(sys.argv[1])
    else:
        print("Usage: uv run remove_bg.py <path_to_image_file>")
        sys.exit(1)

    # print(f"Path: {type(file_path)} -> {file_path}")

    file_name: str = None
    path: str = None

    splitted_values: list[str] = re.split("[./]", file_path)
    path = str(current_path.parent) + "/".join(splitted_values[:-2])
    # print(f">>> Path: {path}")

    file_name = splitted_values[-2:-1][0]
    output_file_name_ext = "removed_bg" + "_" + file_name + ".png"
    output_path = path + "/" + output_file_name_ext

    # print(f"OP file name: {output_file_name_ext}, OP Path: {output_path}")
    remove_background(file_path, output_path)


def remove_background(input_path: str, output_path: str) -> None:
    input_image = Image.open(input_path)
    output_image = remove(input_image)
    output_image.save(output_path)
    print("Background removed...")
    print(f"Path of the new image with removed background:\n{output_path}")


if __name__ == "__main__":
    main()
