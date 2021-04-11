# import common modules
import numpy as np
np.set_printoptions(precision=4)  # print arrays to 4DP
import matplotlib.pyplot as plt
# gray colormap and nearest neighbor interpolation by default
plt.rcParams['image.cmap'] = 'gray'
plt.rcParams['image.interpolation'] = 'nearest'

from scipy.ndimage import affine_transform
from rotations import x_rotmat  # from rotations.py
from rotations import y_rotmat  # from rotations.py
from rotations import z_rotmat  # from rotations.py

import nibabel as nib
img = nib.load('test.nii')
nii_data = img.get_fdata()
I = nii_data[..., 0]  # I is the first volume
i = 0
if (len(nii_data.shape) == 3):
    for slice_Number in range(nii_data.shape[2]):
        print(type(nii_data[:, :, slice_Number]))
        plt.imshow(nii_data[:, :, slice_Number])
        plt.show()
if (len(nii_data.shape) == 4):
    for frame in range(nii_data.shape[3]):
        for slice_Number in range(nii_data.shape[2]):
            # rotation matrix for rotation of 0.2 radians around x axis
            M = y_rotmat(0.1)
            translation = [1, 2, 3]  # Translation from I to J

            # order=1 for linear interpolation
            K = affine_transform(nii_data[...,0], M, translation, output_shape=I.shape, order=1)
            print(K.shape)
            plt.imshow(K[ :, i])
            plt.show()
            i = i + 1




