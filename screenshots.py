import glob
import os
from pathlib import Path

from PIL import Image

from utils.utils import *

# directory of images to resize
dir = '/Users/glennjocher/Downloads/'

# Formats: iPhone 8, iPhone XS, iPad Pro 12.9
formats = ['5_5', '5_8', '12_9', '6_5']  # (inches)
size_x = [1242, 1125, 2048, 1242]
size_y = [2208, 2436, 2732, 2688]


def main():
    new_dir = 'screenshots'
    images = glob.glob(dir + '/*.*')

    os.system('rm -rf ' + dir + new_dir)
    os.system('mkdir ' + dir + new_dir)
    for image in images:
        img = cv2.imread(image)
        print(image)

        for i, format in enumerate(formats):
            img_resized = resize_image(img, height=size_y[i], width=size_x[i], mode='Fill')  # i.e. mode = 'Pad'

            new_name = dir + new_dir + '/' + format + '_' + image.split('/')[-1]

            # cv2.imwrite(new_name.replace('.PNG', '.jpg').replace('.png', '.jpg'), img_resized)  # cv2 save
            Image.fromarray(img_resized[..., ::-1]).save(new_name.replace(Path(new_name).suffix, '.jpg'))  # PIL save


if __name__ == '__main__':
    main()
