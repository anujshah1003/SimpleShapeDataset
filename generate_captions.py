# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 00:23:06 2023

@author: uid38717
"""
from helpers import *
import pandas as pd

class GenerateCaptions:
    def __init__(self,get_shape=True,get_position=False,get_width=False,get_height=False,
                 get_center=False,get_area=False,get_perimeter=False,num_captions=2):
        
        self.get_shape=get_shape
        self.get_position=get_position
        self.get_width=get_width 
        self.get_height=get_height
        self.get_center=get_center
        self.get_area=get_area 
        self.get_perimeter=get_perimeter
        self.num_captions=num_captions
        self.num_types=["num","words"]

        
    def get_caption(self,shape="triangle",position=None,width=None,height=None,
                 center=None,area=None,perimeter=None):
        captions=[]
        for i in range(self.num_captions):
            num_type=self.num_types[i]

            used_of=False
            caption="a {}".format(shape)
            
            if self.get_width and width:
                
                if num_type=="words":
                    width_=convert_to_words(str(width))
                else:
                    width_=width
                
                if not used_of:
                    caption+=" of width {} pixels".format(width_)
                    used_of=True
                else:
                    caption+=", width {} pixels".format(width_)
    
            if self.get_height and height:
                if num_type=="words":
                    height_=convert_to_words(str(height))
                else:
                    height_=height
                if not used_of:
                    caption+=", of height {} pixels".format(height_)
                    used_of=True
                else:
                    caption+=", height {} pixels".format(height_)
                    
            if self.get_area and area:
                if num_type=="words":
                    area_=convert_to_words(str(area))
                else:
                    area_=area                
                
                if not used_of:
                    caption+=", of area {} pixels".format(area_)
                    used_of=True
                else:
                    caption+=", area {} pixels".format(area_)   
                    
            if self.get_perimeter and perimeter:
                if num_type=="words":
                    perimeter_=convert_to_words(str(perimeter))
                else:
                    perimeter_=perimeter             
                
                if not used_of:
                    caption+=", of perimeter {} pixels".format(perimeter_)
                    used_of=True
                else:
                    caption+=", perimeter {} pixels".format(perimeter_)
                    
            if self.get_position and position:
                caption+=", located at {} position".format(position)
                    
            if self.get_center and center:
                
                caption+=", with center at {}".format(center)
                
            caption+="."
            captions.append(caption)
        
        return captions
        
    def update_df(self,df):
        """
        A function that takes a annotation dataframe and add a caption column 
        for each image

        Parameters
        ----------
        df : pd.DataFrame
            DESCRIPTION.

        Returns
        -------
        None.

        """
        # Iterate all rows using DataFrame.iterrows()
        df["captions"]=""
        for index, row in df.iterrows():
            shape=row["shape"]
            position=row["position"]
            width=row["width"]
            height=row["height"]
            area=row["area"]
            perimeter=row["perimeter"]
            center_x=row["center_x"]
            center_y=row["center_y"]
            center="({},{})".format(center_x,center_y)

            captions=self.get_caption(shape=shape,position=position,width=width,height=height,
                 center=center,area=area,perimeter=perimeter)
            #df.loc[index,['captions']] = captions
            df.at[index,"captions"]=captions
        return df
        
if __name__=="__main__":
    caption_generator = GenerateCaptions(get_shape=True,get_position=True,
                                         get_width=True,get_height=True,
                 get_center=True,get_area=True,get_perimeter=True,num_captions=2)

    #caption1=caption_generator.get_caption(shape="triangle",position="top_left",
     #                                      width=None,height=None,center=None,
     #                                      area=None,perimeter=None)
    
    caption3=caption_generator.get_caption(shape="triangle",position="top_left",width="36",height="45",
                 center="(150,45)",area="400",perimeter="600")
        
    #print(caption1)
    print(caption3)
    
    ann_path=r"D:/pet_projects/datasets/SimpleShapeDataset/train/train_ann.csv"
    dest_ann_path=ann_path[:-4]+"_captions1.csv"
    ann_df=pd.read_csv(ann_path)
    df_=caption_generator.update_df(ann_df)
    df_.head()
    df_.to_csv(dest_ann_path)
    
    