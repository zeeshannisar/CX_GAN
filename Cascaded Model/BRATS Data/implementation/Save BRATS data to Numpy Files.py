# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:08:06 2020

@author: ZeeshanNisar
"""

from keras.preprocessing.image import load_img, img_to_array
from tqdm import tqdm as tqdm
import os
import numpy as np

img_rows = 256
img_cols = 256
channels = 1

os.chdir('/content/drive/My Drive/GitHub Repositories')
baseDir = './Research Paper Contribution/Cascaded Model/BRATS'

trainDir = os.path.join(baseDir, 'dataset',  'train')
validDir = os.path.join(baseDir, 'dataset',  'test')

trainfolders = os.listdir(trainDir)
imgs_A = []
imgs_B = []
for folder in trainfolders:
  if folder=='infected':
    for img_name in tqdm(os.listdir(os.path.join(trainDir, folder))):
      img = load_img(os.path.join(trainDir, folder, img_name), color_mode='grayscale')
      imgs_A.append(img_to_array(img)/127.5-1)
  if folder=='normal':
    for img_name in tqdm(os.listdir(os.path.join(trainDir, folder))):
      img = load_img(os.path.join(trainDir, folder, img_name), color_mode='grayscale')
      imgs_B.append(img_to_array(img)/127.5-1)

imgs_A = np.asarray(imgs_A).reshape(-1, img_rows, img_cols, channels)
np.save(os.path.join(trainDir, 'infected_images'), imgs_A)
imgs_B = np.asarray(imgs_B).reshape(-1, img_rows, img_cols, channels)
np.save(os.path.join(trainDir, 'normal_images'), imgs_B)
