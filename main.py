from gui import displayGUI
from cards import Cards
import cv2
import numpy as np


class main:
    # SETUP

    # Data loader from .txt files made with help from:
    # https://www.earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/numpy-arrays/import-txt-csv-files-numpy-arrays/
    dataLoader = np.genfromtxt('origins.txt', dtype='str')
    for lines in range(len(dataLoader)):
        print(dataLoader[lines])

    # DISPLAY CARDS
    b = displayGUI()

    # SHOP
