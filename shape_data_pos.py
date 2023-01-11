# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 19:24:07 2023

@author: uid38717
"""
import os
import numpy as np
import cv2
import random
import math

def dist(pt1,pt2):
    return np.sqrt((pt2[0]-pt1[0])**2+(pt2[1]-pt1[1])**2)

def get_triangle_pos(img,img_w,img_h,center_minus,center_plus,pos):
    try:
        if pos=="center":
            center_x = np.random.randint(center_minus,center_plus)
            center_y = np.random.randint(center_minus,center_plus)
            height = np.random.randint(20, max(21,(img_h-center_y-10)*2))
            width = np.random.randint(20, max(21,(img_w-center_x-10)*2))

        elif pos=="top_left":
            center_x = np.random.randint(20,center_minus)
            center_y = np.random.randint(20,center_minus)
            height = np.random.randint(20, max(21,(center_y-10)*2))
            width = np.random.randint(20, max(21,(center_x-10)*2))

        elif pos=="top_right":
            center_x = np.random.randint(center_plus,img_w-20)
            center_y = np.random.randint(20,center_minus)
            height = np.random.randint(20, max(21,(center_y-10)*2))
            width = np.random.randint(20, max(21,(img_w-center_x-10)*2))

        elif pos=="bottom_left":
            center_x = np.random.randint(20,center_minus)
            center_y = np.random.randint(center_plus,img_h-20)
            height = np.random.randint(20, max(21,(img_h-center_y-10)*2))
            width = np.random.randint(20, max(21,(center_x-10)*2))

        elif pos=="bottom_right":
            center_x = np.random.randint(center_plus,img_w-20)
            center_y = np.random.randint(center_plus,img_h-20)
            height = np.random.randint(20, max(21,(img_h-center_y-10)*2))
            width = np.random.randint(20, max(21,(img_w-center_x-10)*2))

    except Exception as e:
        print(pos,center_x,center_y)#,width,height)
        print("the error: ",e)  

    pt1=(center_x-int(width/2),center_y+int(height/2))
    pt2=(center_x+int(width/2),center_y+int(height/2))
    pt3=(center_x,center_y-int(height/2))
    
    vertices = np.array([pt1, pt2, pt3], np.int32)
    pts = vertices.reshape((-1, 1, 2))
    
    area=0.5*(width*height)
    area=int(np.round(area))
    
    centroid_x=(pt1[0]+pt2[0]+pt3[0])/3
    centroid_y=(pt1[1]+pt2[1]+pt3[1])/3
    
    centroid_x=int(np.round(centroid_x))
    centroid_y=int(np.round(centroid_y))

    #euclidean distance
    perimeter=dist(pt1,pt2)+dist(pt1,pt3)+dist(pt2,pt3)
    perimeter=int(np.round(perimeter))
    
    caption="A triangle of {} pixels width, {} pixels height, an area of {} and perimeter of {}".format(width,height,area,perimeter)
    
    attributes={"num_sides":3,"width":width,"height":height,"center_x":centroid_x,"center_y":centroid_y,
                "position":pos,"area":int(area),"perimeter":int(perimeter),"caption":caption}
    
    img_new=cv2.fillPoly(img.copy(), [pts], color=(255, 255, 255))
    
    return img_new,attributes

def get_circle_pos(img,img_w,img_h,center_minus,center_plus,pos):
    
    try:
        if pos=="center":
            center_x = np.random.randint(center_minus,center_plus)
            center_y = np.random.randint(center_minus,center_plus)

        elif pos=="top_left":
            center_x = np.random.randint(20,center_minus)
            center_y = np.random.randint(20,center_minus)

        elif pos=="top_right":
            center_x = np.random.randint(center_plus,img_w-20)
            center_y = np.random.randint(20,center_minus)

        elif pos=="bottom_left":
            center_x = np.random.randint(20,center_minus)
            center_y = np.random.randint(center_plus,img_h-20)

        elif pos=="bottom_right":
            center_x = np.random.randint(center_plus,img_w-20)
            center_y = np.random.randint(center_plus,img_h-20)

    except Exception as e:
        print(pos,center_x,center_y)#,width,height)
        print("the error: ",e)  
        
    max_left=center_x-20
    max_right=img_w-center_x-20
    max_top=center_y-20
    max_bot=img_h-center_y-20
    radius_lim=min(max_left,max_right,max_top,max_bot)
    radius = np.random.randint(20, max(21,radius_lim))    

    #radius=int(diameter/2)
    width = height = 2*radius
    pt1 = (center_x,center_y)
        
    area=math.pi*radius*radius
    area=int(np.round(area))    

    perimeter=2*math.pi*radius
    perimeter=int(np.round(perimeter))

    caption="A circle of {} pixels diameter with an area of {} and perimeter of {}".format(width,area,perimeter)

    
    attributes={"num_sides":0,"width":width,"height":height,"center_x":center_x,"center_y":center_y,
                "position":pos,"area":int(area),"perimeter":int(perimeter),"caption":caption}
    
    img_new=cv2.circle(img.copy(), pt1, radius, (255,255,255), -1)
    
    return img_new,attributes

def get_rectangle_pos(img,img_w,img_h,center_minus,center_plus,pos):
    
    try:
        if pos=="center":
            center_x = np.random.randint(center_minus,center_plus)
            center_y = np.random.randint(center_minus,center_plus)

        elif pos=="top_left":
            center_x = np.random.randint(20,center_minus)
            center_y = np.random.randint(20,center_minus)

        elif pos=="top_right":
            center_x = np.random.randint(center_plus,img_w-20)
            center_y = np.random.randint(20,center_minus)

        elif pos=="bottom_left":
            center_x = np.random.randint(20,center_minus)
            center_y = np.random.randint(center_plus,img_h-20)

        elif pos=="bottom_right":
            center_x = np.random.randint(center_plus,img_w-20)
            center_y = np.random.randint(center_plus,img_h-20)

    except Exception as e:
        print(pos,center_x,center_y)#,width,height)
        print("the error: ",e)  
    max_left=center_x-20
    max_right=img_w-center_x-20
    max_top=center_y-20
    max_bot=img_h-center_y-20
    
    height_lim=min(max_top,max_bot)
    width_lim=min(max_left,max_right)

    height_hf = np.random.randint(20, max(21,height_lim))
    width_hf = np.random.randint(20, max(21,width_lim))
    height=height_hf*2
    width=width_hf*2
     
    pt1 = (center_x-width_hf,center_y-height_hf)
    pt2=(pt1[0]+width,pt1[1]+height)
    
    area=width*height
    area=int(np.round(area))

    perimeter=2*(width+height)
    perimeter=int(np.round(perimeter))
    
    caption="A rectangle of {} pixels width, {} pixels height, an area of {} and perimeter of {}".format(width,height,area,perimeter)


    attributes={"num_sides":4,"width":width,"height":height,"center_x":center_x,"center_y":center_y,
                "position":pos,"area":area,"perimeter":perimeter,"caption":caption}
    
    img_new=cv2.rectangle(img.copy(), pt1, pt2, (255,255,255), -1)
    
    return img_new,attributes

def get_square_pos(img,img_w,img_h,center_minus,center_plus,pos):
    
    try:
        if pos=="center":
            center_x = np.random.randint(center_minus,center_plus)
            center_y = np.random.randint(center_minus,center_plus)

        elif pos=="top_left":
            center_x = np.random.randint(20,center_minus)
            center_y = np.random.randint(20,center_minus)

        elif pos=="top_right":
            center_x = np.random.randint(center_plus,img_w-20)
            center_y = np.random.randint(20,center_minus)

        elif pos=="bottom_left":
            center_x = np.random.randint(20,center_minus)
            center_y = np.random.randint(center_plus,img_h-20)

        elif pos=="bottom_right":
            center_x = np.random.randint(center_plus,img_w-20)
            center_y = np.random.randint(center_plus,img_h-20)

    except Exception as e:
        print(pos,center_x,center_y)#,width,height)
        print("the error: ",e)  
    max_left=center_x-20
    max_right=img_w-center_x-20
    max_top=center_y-20
    max_bot=img_h-center_y-20
    
    side_lim=min(max_left,max_right,max_top,max_bot)    
    
    side_hf = np.random.randint(20, max(21,side_lim))
    side=side_hf*2
     
    width=height=side

    pt1 = (center_x-side_hf,center_y-side_hf)
    pt2=(pt1[0]+width,pt1[1]+height)

    area=width*height
    area=int(np.round(area))

    perimeter=2*(width+height)
    perimeter=int(np.round(perimeter))

    caption="A square of {} pixels side dimension with an area of {} and perimeter of {}".format(width,area,perimeter)


    attributes={"num_sides":4,"width":width,"height":height,"center_x":center_x,"center_y":center_y,
                "position":pos,"area":area,"perimeter":perimeter,"caption":caption}
    
    img_new=cv2.rectangle(img.copy(), pt1, pt2, (255,255,255), -1)
    
    return img_new,attributes