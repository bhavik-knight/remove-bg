# Remove Background from your Photos
This script takes an image as input and removes the background from the image
The output image will be a PNG format with a transparent background

---

## Steps to run

### 1. Clone the project
git clone https://github.com/bhavik-knight/remove-bg.git

### 2. Add the required libraries
uv sync

### 3. Run the script `remove_bg.py`
uv run remove_bg.py <input_image_path>

The script takes exactly one command-line argument - the path to your image file from which you want to remove the background. 

The output image file will have `removed_bg` prefix on your current filename, and it will be in the same directory as your input file.


## 
Coded by: [Bhavik](https://bhavikbhagat.netlify.app/)
