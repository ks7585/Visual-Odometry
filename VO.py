import itertools
import matplotlib.pyplot as plt
import numpy as np
import cv2
import matplotlib.animation as animation
import tensorflow as tf
import keras
from mpl_toolkits.mplot3d import Axes3D



import pykitti


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
gray = iter(dataset.gray)
cam1 = iter(dataset.cam1)
rgb = iter(dataset.rgb)
cam2 = iter(dataset.cam2)
#velo = iter(itertools.islice(dataset.velo, 2, None))
for i in range(0,1000,1): 
# Grab some data
# second_pose = next(pose)
 first_gray = next(gray)
 first_cam1 = next(cam1)
 first_rgb = next(rgb)
 first_cam2 = next(cam2)
# third_velo = next(velo)


 #Display some of the data

 np.set_printoptions(precision=4, suppress=True)
 print('\nSequence: ' + str(dataset.sequence))
 print('\nFrame range: ' + str(dataset.frames))

 print('\nGray stereo pair baseline [m]: ' + str(dataset.calib.b_gray))
 print('\nRGB stereo pair baseline [m]: ' + str(dataset.calib.b_rgb))

 print('\nFirst timestamp: ' + str(dataset.timestamps[0]))
# print('\nSecond ground truth pose:\n' + str(second_pose))

 f, ax = plt.subplots(2, 2, figsize=(15, 5))
 ax[0, 0].imshow(first_gray[0], cmap='gray')
 ax[0, 0].set_title('Left Gray Image (cam0)')

 ax[0, 1].imshow(first_cam1, cmap='gray')
 ax[0, 1].set_title('Right Gray Image (cam1)')

 ax[1, 0].imshow(first_cam2)
 ax[1, 0].set_title('Left RGB Image (cam2)')

 ax[1, 1].imshow(first_rgb[1])
 ax[1, 1].set_title('Right RGB Image (cam3)')

 f2 = plt.figure()
 ax2 = f2.add_subplot(111, projection='3d')
# Plot every 100th point so things don't get too bogged down
# velo_range = range(0, third_velo.shape[0], 100)
# ax2.scatter(third_velo[velo_range, 0],
#             third_velo[velo_range, 1],
#             third_velo[velo_range, 2],
#             c=third_velo[velo_range, 3],
#             cmap='gray')
# ax2.set_title('Third Velodyne scan (subsampled)')

 plt.show()