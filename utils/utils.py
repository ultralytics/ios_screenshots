import cv2


def resize_image(img, height=416, width=416, mode='Fill', color=(255, 255, 255)):
    # mode Fill resizes + clips a rectangular image to a square
    # mode Fit resizes a rectangular image to a padded square

    shape = img.shape[:2]  # shape = [height, width]
    ratio_h, ratio_w = float(height) / shape[0], float(width) / shape[1]

    if mode == 'Fill':
        ratio = max(ratio_h, ratio_w)
    else:  # 'Fit'
        ratio = min(ratio_h, ratio_w)

    new_shape = [round(shape[0] * ratio), round(shape[1] * ratio)]
    dw = width - new_shape[1]  # width padding
    dh = height - new_shape[0]  # height padding
    top, bottom = dh // 2, dh - (dh // 2)
    left, right = dw // 2, dw - (dw // 2)
    img = cv2.resize(img, (new_shape[1], new_shape[0]), interpolation=cv2.INTER_AREA)

    if (dw > 0) or (dh > 0):  # add border
        return cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
    else:  # crop to [height, width]
        return img[abs(top):img.shape[0] - abs(bottom), abs(left):img.shape[1] + abs(left)]
