#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from natsort import natsorted



# In[6]:


with open('Masks/part1.json', 'r') as f:
    D = json.load(f)

"""
# In[7]:


np.array([ 1,  4,  6,  9, 11, 15, 16, 17, 22, 24, 27, 28, 29, 30, 34, 35, 37,38, 40, 41, 42, 44, 46, 52, 54, 57, 63, 68, 71, 75, 76, 79, 80, 81,82, 84, 89, 96])


# In[ ]:


i = 0
"""

names = ["car","bus","truck"]

for frame in D:
#     print(frame['filename'],frame['filename'].split('/')[4])
    
    folder_name = frame['filename'].split('/')[7]
    
    
    file1 = open("Masks/" +folder_name + ".txt","a")
#         print(frame['filename'])
    for bound in frame['objects']:
        if bound['name'] in names:
            frame_n = frame['filename'].split('/')[8].split('.')[0].split('_')[0]
#                 print(frame_n)
            a = -1
            b = bound['relative_coordinates']['center_x']*800
            c = bound['relative_coordinates']['center_y']*410
            d = bound['relative_coordinates']['width']*800
            e = bound['relative_coordinates']['height']*410
            f = bound['confidence']
            g = -1
            h = -1
            j = -1
            line = [frame_n,a,b,c,d,e,f,g,h,j]
            
            for l in line:
                file1.write(str(l)+",")
            file1.write("\n")
    file1.close()
        