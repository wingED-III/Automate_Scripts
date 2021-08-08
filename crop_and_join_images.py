import cv2
import numpy as np

import os


def main():
    concat_img = None

    files = os.listdir()
    part = 6
    divider = len(files) // part
    for count, img in enumerate(files):
        if img[-4:] != ".png":
            continue

        print(img)

        img = cv2.imread(img)
        img = crop(img)

        if concat_img is None:
            concat_img = img
        else:
            concat_img = cv2.vconcat([concat_img, img])

        if (count+1) % divider == 0 or count == len(files)-1:
            cv2.imwrite('name'+str(count-divider)+"-" +
                        str(count)+'.png', concat_img)
            concat_img = None

    # cv2.imwrite('all.png', concat_img)
    # cv2.imshow("concat", concat_img)
    # cv2.waitKey(0)

    # img = cv2.imread("0000000002.png")
    # # 0000000222.png
    # # print(img.shape)

    # img = crop(img)
    # # cv2.imshow("crop", crop_img)

    # img2 = cv2.imread("0000000003.png")
    # img2 = crop(img2)

    # concat_img = cv2.vconcat([img, img2])

    # cv2.imshow("concat", concat_img)


def crop(image):
    return image[:90, :1920]


if __name__ == "__main__":
    main()
