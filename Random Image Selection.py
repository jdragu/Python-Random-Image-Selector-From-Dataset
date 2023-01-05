#!/usr/bin/env python
# coding: utf-8

# # Random Image Selection: Book of Beasts

# ## Read the data

# In[60]:


# import the modules
import os
from os import listdir
 
# get the path/directory
folder_dir = "Bestiary/"
for images in os.listdir(folder_dir):
 
    # check if the image ends with jpeg
    if (images.endswith(".jpeg")):
        print(images)


# ## Random Image Selector

# In[76]:


import os, random

folder="Bestiary/"

a=random.choice(os.listdir(folder))
print(a)

#os.open(a, os.O_RDWR)
from PIL import Image
file = folder+a
Image.open(file)

