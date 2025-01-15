# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

import glob
import os

from utils.utils import *

# directory of images to resize
dir = "/Users/glennjocher/downloads/app/styles/"

# Formats: square
formats = ["512"]  # (pixels)
size_x = [512]
size_y = [512]


def main():
    """Resize and save images from a directory into a new sub-directory using specified format and dimensions."""
    new_dir = "square"
    images = glob.glob(f"{dir}/*.*")

    os.system(f"rm -rf {dir}{new_dir}")
    os.system(f"mkdir {dir}{new_dir}")
    for image in images:
        img = cv2.imread(image)
        print(image)

        for i, format in enumerate(formats):
            img_resized = resize_image(img, height=size_y[i], width=size_x[i], mode="Fill")
            cv2.imwrite(dir + new_dir + "/" + image.split("/")[-1], img_resized)


if __name__ == "__main__":
    main()
