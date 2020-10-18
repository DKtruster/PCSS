import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

cardImg = []
shopImg = []
assetsImg = []

# LOADING IMAGES
bg1 = Image.open("Assets/backgroundBoard3.jpg")
assetsImg.append(bg1)
textBut = Image.open("Assets/testButtonTexture.jpg")
assetsImg.append(bg1)

CDviking1 = Image.open("Assets/viking1low.jpg")
cardImg.append(CDviking1)
SPviking1 = Image.open("Assets/viking1shop.jpg")
shopImg.append(SPviking1)

CDroman1 = Image.open("Assets/roman1lowUI.jpg")
cardImg.append(CDroman1)
SProman1 = Image.open("Assets/roman1shop.jpg")
shopImg.append(SProman1)

CDchinese1 = Image.open("Assets/chinese1lowUI.jpg")
cardImg.append(CDchinese1)
SPchinese1 = Image.open("Assets/chinese1shop.jpg")
shopImg.append(SPchinese1)

CDchinese2 = Image.open("Assets/chinese2lowUI.jpg")
cardImg.append(CDchinese2)
SPchinese2 = Image.open("Assets/chinese2shop.jpg")
shopImg.append(SPchinese2)

CDchinese3 = Image.open("Assets/chinese3lowUI.jpg")
cardImg.append(CDchinese3)
SPchinese3 = Image.open("Assets/chinese3shop.jpg")
shopImg.append(SPchinese3)

CDchinese4 = Image.open("Assets/chinese4lowUI.jpg")
cardImg.append(CDchinese4)
SPchinese4 = Image.open("Assets/chinese4shop.jpg")
shopImg.append(SPchinese4)

CDchinese5 = Image.open("Assets/chinese5lowUI.jpg")
cardImg.append(CDchinese5)
SPchinese5 = Image.open("Assets/chinese5shop.jpg")
shopImg.append(SPchinese5)

CDunknown = Image.open("Assets/unknown1low.jpg")
assetsImg.append(bg1)