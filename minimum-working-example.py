#!/usr/bin/env python
# coding: utf-8

# # Creating New Colormaps

# In[ ]:


import numpy as np
from mpl2flu import *


# ### Write Colormap from an RGB Text File
# This is the colorblind safe version of Viridis from cmaputil.

# In[ ]:


url = 'https://github.com/pnnl/cmaputil/raw/master/colormaps/cividis.txt'
rgb = read_data(url)
filename = 'colormaps/cividis.colormap'
write_cmap(rgb,filename);


# ### Write Inferno Colormap from Matplotlib
# We'll choose a size of 32. This should produce a warning; 32 colors is just an 
# arbitrary cutoff, but hopefully this message is helpful.
# 
# We'll also name the filename with the colormap append length.

# In[ ]:


mpl2flu(cmap_len=32, cmap_names='inferno',name_with_num=True)


# We'll try that again, with `warn=off`, and leaving out the colormap length.

# In[ ]:


mpl2flu(cmap_len=128, cmap_names='inferno',warn=False);


# To add all the colormaps from matplotlib, you can use `cmap_names='all'`, which is the default.

# mpl2flu();

# ### Other Input Types
# Let's try some colors from https://gka.github.io/palettes/

# In[ ]:


colors = '#ffffe0 #ffd59b #ffa474 #f47461 #db4551 #b81b34 #8b0000'
rgb = read_data(colors)


# In[ ]:


write_cmap(rgb,filename='colormaps/chromajs.colormap');


# There's also http://colorbrewer2.org/  All these should be available from matplotlib, but we'll try the hard way here just because. This is copy-pasted from the website.

# In[ ]:


colors = '''
215,48,39
244,109,67
253,174,97
254,224,144
255,255,191
224,243,248
171,217,233
116,173,209
69,117,180
'''
rgb = read_data(colors)
write_cmap(rgb,filename='colormaps/rdylbu.colormap');

