#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import argparse

import cv2 as cv
import numpy as np
import gui.cvui as cvui

from XDoG import XDoG_filter

WINDOW_NAME = 'XDoG Sample'


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--device", type=int, default=0)
    parser.add_argument("--width", help='cap width', type=int, default=960)
    parser.add_argument("--height", help='cap height', type=int, default=540)

    parser.add_argument("--file", type=str, default=None)

    args = parser.parse_args()

    return args


def draw_gui(
    gray_image,
    kernel_size,
    sigma,
    k_sigma,
    epsilon,
    phi,
    gamma,
):
    image_width, image_height = gray_image.shape[1], gray_image.shape[0]

    cvuiframe = np.zeros((image_height, int(image_width * 1.3), 3), np.uint8)
    cvuiframe[:] = (49, 52, 49)

    display_image = cv.cvtColor(gray_image, cv.COLOR_GRAY2BGR)
    cvui.image(cvuiframe, 0, 0, display_image)

    # kernel_size
    cvui.text(cvuiframe, int(image_width * 1.02), 10,
              'kernel size(Gaussian Blur)')
    options = cvui.TRACKBAR_DISCRETE | cvui.TRACKBAR_HIDE_SEGMENT_LABELS
    cvui.trackbar(cvuiframe, int(image_width * 1.01), 25,
                  int(image_width * 0.29), kernel_size, 0, 25, 3, '%.0Lf',
                  options, 1)
    kernel_size[0] = max(
        0, kernel_size[0] if (kernel_size[0] % 2) == 1 else
        (kernel_size[0] - 1))

    # sigma
    cvui.text(cvuiframe, int(image_width * 1.02), 90, 'sigma')
    cvui.trackbar(cvuiframe, int(image_width * 1.01), 105,
                  int(image_width * 0.29), sigma, 0.1, 5.)

    # k_sigma
    cvui.text(cvuiframe, int(image_width * 1.02), 170, 'k_sigma')
    cvui.trackbar(cvuiframe, int(image_width * 1.01), 185,
                  int(image_width * 0.29), k_sigma, 0.1, 5.)

    # epsilon
    cvui.text(cvuiframe, int(image_width * 1.02), 250, 'epsilon')
    cvui.trackbar(cvuiframe, int(image_width * 1.01), 265,
                  int(image_width * 0.29), epsilon, 0.0, 25.)

    # phi
    cvui.text(cvuiframe, int(image_width * 1.02), 330, 'phi')
    options = cvui.TRACKBAR_DISCRETE | cvui.TRACKBAR_HIDE_SEGMENT_LABELS
    cvui.trackbar(cvuiframe, int(image_width * 1.01), 345,
                  int(image_width * 0.29), phi, 0, 50, 3, '%.0Lf', options, 1)

    # gamma
    cvui.text(cvuiframe, int(image_width * 1.02), 410, 'gamma(*0.1)')
    options = cvui.TRACKBAR_DISCRETE | cvui.TRACKBAR_HIDE_SEGMENT_LABELS
    cvui.trackbar(cvuiframe, int(image_width * 1.01), 425,
                  int(image_width * 0.29), gamma, 0.01, 10., 1, '%.1Lf',
                  cvui.TRACKBAR_DISCRETE, 0.1)

    return cvuiframe


def main():
    args = get_args()
    device = args.device
    cap_width = args.width
    cap_height = args.height

    filepath = args.file

    if filepath is None:
        cap = cv.VideoCapture(device)
        cap.set(cv.CAP_PROP_FRAME_WIDTH, cap_width)
        cap.set(cv.CAP_PROP_FRAME_HEIGHT, cap_height)

    cvui.init(WINDOW_NAME)

    kernel_size = [0]
    sigma = [1.4]
    k_sigma = [1.6]
    epsilon = [0.0]
    phi = [10]
    gamma = [9.8]

    while True:
        if filepath is None:
            ret, frame = cap.read()
            if not ret:
                continue
        else:
            frame = cv.imread(filepath)
        original_frame = copy.deepcopy(frame)

        gray_image = cv.cvtColor(original_frame, cv.COLOR_BGR2GRAY)
        gray_image = XDoG_filter(
            gray_image,
            kernel_size[0],
            sigma[0],
            k_sigma[0],
            epsilon[0],
            phi[0],
            gamma[0] * 0.1,
        )

        cvuiframe = draw_gui(
            gray_image,
            kernel_size,
            sigma,
            k_sigma,
            epsilon,
            phi,
            gamma,
        )

        cvui.update()
        cvui.imshow(WINDOW_NAME, cvuiframe)
        key = cv.waitKey(1)
        if key == 27:  # ESC
            break
    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
