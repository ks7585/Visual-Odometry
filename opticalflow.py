# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 10:19:01 2017

@author: ks7585
"""


 #optical_flow
import os
import cv2
from glob import glob
import numpy as np

def opt_flow(old_img, new_img):
    old_gray = cv2.cvtColor(old_img, cv2.COLOR_RGB2GRAY)
    new_gray = cv2.cvtColor(new_img, cv2.COLOR_RGB2GRAY)
    hsv = np.zeros_like(old_img)
    hsv[...,1] = cv2.cvtColor(new_img, cv2.COLOR_RGB2HSV)[...,1]
    flow = cv2.calcOpticalFlowFarneback(old_gray, new_gray, 
                                        None, 0.5, 3, 15, 
                                        3, 5, 1.2, 0)
    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
    hsv[...,0] = ang*180/np.pi/2
    hsv[...,2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
    bgr = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
    return bgr




   
if __name__ == '__main__':
    img_dir = '/home/ks7585/kitti/dataset/sequences/00/image_0/'
    out_dir = '/home/ks7585/kitti/op_rgb/'
    img_files = sorted(glob(img_dir + '/*'))
    for idx in range(len(glob(img_dir + '/*')) - 1):
        old = cv2.imread(img_files[idx])
        new = cv2.imread(img_files[idx + 1])
        flow = opt_flow(old, new)
        print(idx)
        cv2.imwrite(os.path.join(out_dir, '0%05d.png' %idx), flow)
 