import glob
import os

from utils.utils import *

# directory of images to resize
dir = '/Users/glennjocher/downloads/app/screenshots/'

# Formats: iPhone 8, iPhone XS, iPad Pro 12.9
formats = ['5_5', '5_8', '12_9']  # (inches)
size_x = [1242, 1125, 2048]
size_y = [2208, 2436, 2732]


def main():
    new_dir = 'screenshots'
    images = glob.glob(dir + '/*.*')

    os.system('rm -rf ' + dir + new_dir)
    os.system('mkdir ' + dir + new_dir)
    for image in images:
        img = cv2.imread(image)
        print(image)

        for i, format in enumerate(formats):
            img_resized = resize_image(img, height=size_y[i], width=size_x[i], mode='Fit')  # i.e. mode = 'Pad'
            cv2.imwrite(dir + new_dir + '/' + format + '_' + image.split('/')[-1], img_resized)


if __name__ == '__main__':
    main()
