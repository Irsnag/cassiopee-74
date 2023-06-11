# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 12:34:31 2023

@author: 33606
"""

import numpy as np

def list_filtrage(label):
    """
    Filter a label list and return the indices of images with all-zero labels.

    Args:
        label (numpy.ndarray): List of labels with shape (num_images, height, width).

    Returns:
        list: List of indices corresponding to images with all-zero labels.
    """

    # Calculate the number of images
    nb_images = np.shape(label)[0]

    # Get the dimensions of the label
    dim = np.shape(label)[1], np.shape(label)[2]

    # Initialize an empty list
    L = []

    # Reshape the label array
    M_bis = np.reshape(label, (nb_images, dim[0], dim[1], 1))

    # Iterate over the images
    for i in range(nb_images):
        # Check if any value in the image is non-zero
        if not np.any(M_bis[i, :, :, :]):
            # Append the index to the list
            L.append(i)

    return L


def filtrage(data, label, L):
    """
    Filter data and labels based on the indices to keep.

    Args:
        data (numpy.ndarray): Data array with shape (num_images, height, width).
        label (numpy.ndarray): Label array with shape (num_images, height, width).
        L (list): List of indices to keep.

    Returns:
        numpy.ndarray: Filtered data array.
        numpy.ndarray: Filtered label array.
    """

    # Calculate the number of images
    nb_images = np.shape(label)[0]

    # Get the dimensions of the label
    dim = np.shape(label)[1], np.shape(label)[2]

    # Reshape the label array
    label = np.reshape(label, (nb_images, dim[0], dim[1]))

    # Initialize new arrays for filtered data and labels
    data_f = np.zeros((nb_images - len(L), dim[0], dim[1]))
    label_f = np.zeros((nb_images - len(L), dim[0], dim[1]))

    # Initialize a counter
    j = 0

    # Iterate over the images
    for i in range(nb_images):
        # Check if the index is not in the list of indices to exclude
        if i not in L:
            # Copy the data and label to the filtered arrays
            data_f[j, :, :] = data[i, :, :]
            label_f[j, :, :] = label[i, :, :]
            j += 1

    return data_f, label_f

#data=np.load('')
#label=np.load('')
#L=list_filtrage(label)
#data_f, label_f=filtrage(data, label, L)
