#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2 as cv


def XDoG_filter(image,
                kernel_size=0,
                sigma=1.4,
                k_sigma=1.6,
                epsilon=0,
                phi=10,
                gamma=0.98):
    """XDoG(Extended Difference of Gaussians)を処理した画像を返す

    Args:
        image: OpenCV Image
        kernel_size: Gaussian Blur Kernel Size
        sigma: sigma for small Gaussian filter
        k_sigma: large/small for sigma Gaussian filter
        eps: threshold value between dark and bright
        phi: soft threshold
        gamma: scale parameter for DoG signal to make sharp

    Returns:
        Image after applying the XDoG.
    """
    epsilon /= 255
    dog = DoG_filter(image, kernel_size, sigma, k_sigma, gamma)
    dog /= dog.max()
    e = 1 + np.tanh(phi * (dog - epsilon))
    e[e >= 1] = 1
    return e.astype('uint8') * 255


def DoG_filter(image, kernel_size=0, sigma=1.4, k_sigma=1.6, gamma=1):
    """DoG(Difference of Gaussians)を処理した画像を返す

    Args:
        image: OpenCV Image
        kernel_size: Gaussian Blur Kernel Size
        sigma: sigma for small Gaussian filter
        k_sigma: large/small for sigma Gaussian filter
        gamma: scale parameter for DoG signal to make sharp

    Returns:
        Image after applying the DoG.
    """
    g1 = cv.GaussianBlur(image, (kernel_size, kernel_size), sigma)
    g2 = cv.GaussianBlur(image, (kernel_size, kernel_size), sigma * k_sigma)
    return g1 - gamma * g2


if __name__ == '__main__':
    sample_image = cv.imread('sample.jpg')
    gray_image = cv.cvtColor(sample_image, cv.COLOR_BGR2GRAY)

    result_image = XDoG_filter(gray_image)

    cv.imshow('Before', sample_image)
    cv.imshow('After', result_image)
    cv.waitKey(-1)
