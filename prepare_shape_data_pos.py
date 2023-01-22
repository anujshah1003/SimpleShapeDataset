# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 19:17:05 2023

@author: uid38717
"""

import os
import numpy as np
import cv2
import random
import math
import pandas as pd

from shape_data_pos import *

# Get the configs

data_split="train"
num_images=100
img_size=200
dest_path=r"D:\pet_projects\datasets\SimpleShapeDataset/{}".format(data_split)
dest_csv_path=os.path.join(dest_path,"{}_ann.csv".format(data_split))

shapes=["triangle","rectangle","square","circle"]
for dir_ in shapes:
    dest_dir=os.path.join(dest_path,dir_)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        

positions=["top_left","top_right","center","bottom_left","bottom_right"]
# get the image center

img_center=img_size/2
center_offset=20

center_minus=int(img_size/2)-center_offset
center_plus=int(img_size/2)+center_offset


def prepare_image(shape="triangle",pos="center"):
    img=np.zeros((img_size,img_size))
    img_w,img_h=img.shape 
    if shape=="triangle":
        img_with_shape,img_attr=get_triangle_pos(img,img_w,img_h,center_minus,center_plus,pos)
    elif shape=="rectangle":
        img_with_shape,img_attr=get_rectangle_pos(img,img_w,img_h,center_minus,center_plus,pos)
    elif shape=="square":
        img_with_shape,img_attr=get_square_pos(img,img_w,img_h,center_minus,center_plus,pos)
    elif shape=="circle":
        img_with_shape,img_attr=get_circle_pos(img,img_w,img_h,center_minus,center_plus,pos)
    return img_with_shape,img_attr

columns=["image","shape","width","height","area","perimeter","num_sides"]
df=pd.DataFrame(columns=columns)
for shape in shapes:
    for pos in positions:
        output_path=os.path.join(dest_path,shape,pos)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        for i in range(num_images):
            output_file_name = shape + "_"+pos+'_{:05d}'.format(i) + '.png'
            file_path=os.path.join(output_path,output_file_name)
            img,attr=prepare_image(shape,pos)
            cv2.imwrite(file_path,img)
            df=df.append({"image":output_file_name,"shape":shape,"width":attr["width"],"center_x":attr["center_x"],
                          "center_y":attr["center_y"],"position":attr["position"],"height":attr["height"],"area":attr["area"],
                           "perimeter":attr["perimeter"],"num_sides":attr["num_sides"]},ignore_index=True)
df.to_csv(dest_csv_path)