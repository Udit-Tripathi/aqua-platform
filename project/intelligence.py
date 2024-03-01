import numpy as np 
import pandas as pd
import skimage

r=[255,0,0]
g=[0,255,0]
b=[0,0,255]

def find_red_pixels(*args,**kwargs):
    """Your documentation goes here""" 
    upper_threshold=100 
    lower_threshold=50 
    map_filename=skimage.io.imread('./data/map.png')
    map_filename = skimage.color.rgba2rgb(map_filename) 
    map_filename= np.asarray(map_filename)
    new_image = []  
    for row in map_filename:
        temp_row=[]
        for r,g,b in row:
            r = r*255
            g = g*255
            b = b*255
            if r>upper_threshold and g<lower_threshold and b<lower_threshold:
                temp_row.append([255,255,255])
            else:
                temp_row.append([0,0,0])
        new_image.append(temp_row)
    new_image = np.array(new_image).astype(float)
    map_filename=skimage.io.imsave("map-red-pixels.jpg",new_image)
               



    



def find_cyan_pixels(*args,**kwargs):
    """Your documentation goes here"""
    upper_threshold=100 
    lower_threshold=50 
    map_filename=skimage.io.imread('./data/map.png')
    map_filename = skimage.color.rgba2rgb(map_filename) 
    map_filename= np.asarray(map_filename)
    new_image = []  
    for row in map_filename:
        temp_row=[]
        for r,g,b in row:
            r = r*255
            g = g*255
            b = b*255
            if g>upper_threshold and r<lower_threshold and b>upper_threshold:
                temp_row.append([255,255,255])
            else:
                temp_row.append([0,0,0])
        new_image.append(temp_row)
    new_image = np.array(new_image).astype(float)
    map_filename=skimage.io.imsave("map-cyan-pixels.jpg",new_image)



