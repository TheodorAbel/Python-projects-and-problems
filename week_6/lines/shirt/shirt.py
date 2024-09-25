import sys
from PIL import Image, ImageOps
import os

if len(sys.argv) != 3:
    sys.exit("Expected two command line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    valid_extensions = ['.jpeg', '.jpg', '.png']

    ext1 = os.path.splitext(input_file)[1].lower()
    ext2 = os.path.splitext(output_file)[1].lower()

    if ext1 not in valid_extensions:
        raise FileNotFoundError("Incorrect file extension for input file")

    if ext1 != ext2:
        raise FileNotFoundError("File extensions do not match")

    if not os.path.exists(input_file):
        sys.exit("The first file does not exist")

    with Image.open(input_file) as beforeimg, Image.open("shirt.png") as shirt:
        # Resize the input image to match the size of shirt.png
        size = shirt.size
        beforeimg = ImageOps.fit(beforeimg, size)

        # Ensure transparency is handled correctly
        beforeimg.paste(shirt, (0, 0), shirt)
        beforeimg.save(output_file)

except FileNotFoundError as e:
    sys.exit(str(e))
except Exception as e:
    sys.exit(f"An error occurred: {e}")
