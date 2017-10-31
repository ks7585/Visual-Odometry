import itertools
import matplotlib.pyplot as plt
import numpy as np
import cv2
import matplotlib.animation as animation
import tensorflow as tf
import keras
from mpl_toolkits.mplot3d import Axes3D



import pykitti

__author__ = "Lee Clement"
__email__ = "lee.clement@robotics.utias.utoronto.ca"

# Change this to the directory where you store KITTI data
basedir = '/home/ks7585/kitti/dataset'

# Specify the dataset to load
sequences = '00'

# Load the data. Optionally, specify the frame range to load.
# Passing imformat='cv2' will convert images to uint8 and BGR for
# easy use with OpenCV.frames=range(0, 20, 5)
# dataset = pykitti.odometry(basedir, sequence)
dataset = pykitti.odometry(basedir, sequences, frames=range(0,1000,1), imformat='cv2')

# dataset.calib:      Calibration data are accessible as a named tuple
# dataset.timestamps: Timestamps are parsed into a list of timedelta objects
# dataset.poses:      Generator to load ground truth poses T_w_cam0
# dataset.camN:       Generator to load individual images from camera N
# dataset.gray:       Generator to load monochrome stereo pairs (cam0, cam1)
# dataset.rgb:        Generator to load RGB stereo pairs (cam2, cam3)
# dataset.velo:       Generator to load velodyne scans as [x,y,z,reflectance]
#pose = iter(itertools.islice(dataset.poses, 1, None))

cam2 = iter(dataset.cam2)
cam2_list = []

#velo = iter(itertools.islice(dataset.velo, 2, None))
for i in range(0,10,1): 
# Grab some data
# second_pose = next(pose)
 first_cam2 = next(cam2)
 cam2_list.append(first_cam2)
# third_velo = next(velo)