from matplotlib.pyplot import colormaps
from matplotlib import cm
import os

def rgba_to_rgb(rgba,bg_rgb=(1,1,1)):
    r_i,g_i,b_i,a_i = rgba
    r_b,g_b,b_b = bg_rgb
    # Converts RGBA values to RGB values for a specific RGB Background
    # https://stackoverflow.com/questions/2049230/convert-rgba-color-to-rgb
    r_o = ((1 - a_i) * r_b) + (a_i * r_i)
    g_o = ((1 - a_i) * g_b) + (a_i * g_i)
    b_o = ((1 - a_i) * b_b) + (a_i * b_i)
    return (r_o,g_o,b_o)

def mpl2flu(cmap_len=15, cmap_names='all', name_with_num=False):
    """Generate Fluent importable Colormaps from Matplotlib

    Paraneters
    ----------
    cmap_len :  Int
        Number of colors in the map to generate.
    cmap_names : Sequence or String
        Name of the cmap to create. Default is all. 
    name_with_num : Bool
        Adds the map length to the end of the filename.
    """
    
    if cmap_names == 'all':
        cmap_names = colormaps()
    else:
        if isinstance(cmap_names,str):
            cmap_names = [cmap_names]
        
    cmap_len = round(cmap_len)
    
    # Make sure the subfolder exists:
    if not os.path.exists('colormaps'):
        os.mkdir('colormaps')
        print('Creating directory for colormaps:')
        print(os.path.realpath('colormaps'))
    
    for cmap_name in cmap_names:
        cmap = cm.get_cmap(cmap_name,cmap_len)
        # Add the length of the cmap to the filename
        if name_with_num:
            cmap_name = cmap_name+str(cmap_len)
        filename = 'colormaps/'+cmap_name+'.colormap'
        with open(filename,'wt') as file:
            file.write('("'+cmap_name+'"\n')
            for n in range(0,cmap_len):
                # Convert from RGBA to RGB
                rgb = rgba_to_rgb(cmap(n))
                fmt_str = '\t({0:.6f} {1:.6f} {2:.6f} {3:.6f})\n'
                file.write(fmt_str.format(n/(cmap_len-1),*rgb))
            file.write(')')

# NOTE:
# It appears Fluent interpolates color by placing 2 values at the 
# right (high end) that are similar, then adds from the left 
# (as viewing in the EDIT menu in Fluent). This doesn't work well for 
# diverging maps with a central color like RdYlBu (or any really).
# Better to create the map of the size you actually want using cmap_len.
# I'm sure there's a way to fix this, but I haven't figured it out.

# Eg:
# A pseudo map from Red to white:
#  ____________________________________________
# |-R4-|-R3-|-R2-|-R1-|-N0-|-W1-|-W2-|-W3-|-W4-|
#  `````````````````````````````````````````````
# Interpolating this down you'd expect something like:
#  ________________________
# |-R4-|-R2-|-N0-|-W2-|-W4-|
#  `````````````````````````
# But instead Fluent creates something like:
#  ________________________
# |-R4-|-R3-|-W2-|-W3-|-W4-|
#  `````````````````````````