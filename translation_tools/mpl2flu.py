from matplotlib.pyplot import colormaps
from matplotlib import cm
import numpy as np
import os

def normalize(x,min_value=None,max_value=None):
    '''Normalize value or array
    
    Parameters
    ----------
    x: Sequence or Numeric (float,int,datetime)
        Required: Input data to normalize.
    min_value: Numeric
        Optional: Force a minimum value from which to normalize. Ie 0
        Default: None
    max_value: Numeric
        Optional: Force a maximum value from which to normalize. Ie. 255
        Default: None
    Returns
    ----------
    xn: Normalized value(s) of x
    mx: Coefficient matrix
    mb: Intercept matrix
    
    Where x = xm*xn + b
    Ie.
        | xn1 |   | xn1 |   | b1 |
        | xn3 |   | xn2 |   | b2 |
        | xn2 |   | xn3 |   | b3 |
    x = |  .  | * |  .  | + |  . |
        |  .  |   |  .  |   |  . |
        |  .  |   |  .  |   |  . |
    '''
    if not isinstance(x,np.ndarray):
        x = np.array(x)
    mn = np.min(x,axis=0)
    mx = np.max((x-mn),axis=0)
    if min_value is None:
        return (x-mn)/mx, mx, mn
    else:
        return (x-min_value)/max_value, min_value, max_value
def rgba_to_rgb(rgba,bg_rgb=(1,1,1)):
    '''Convert RGBA values to RGB
    
    Parameters
    ----------
    rgba : Sequence, Nx4 or 4xN
        Required: Input list or array of [R,G,B,A] values to convert
    bg_rgb : Sequence, (1,3)
        Optional: Background rgb color values.
        Default: (1,1,1)
    '''
    if not isinstance(rgba,np.ndarray):
        rgba = np.array(rgba)
    if 4 not in rgba.shape:
        print('RGBA must be an Nx4 or 4xN iterable')
        raise()
    if rgba.shape[0] != 4:
        rgba = rgba.T
    r_i,g_i,b_i,a_i = rgba
    r_b,g_b,b_b = bg_rgb
    # Converts RGBA values to RGB values for a specific RGB Background
    # https://stackoverflow.com/questions/2049230/convert-rgba-color-to-rgb
    r_o = ((1 - a_i) * r_b) + (a_i * r_i)
    g_o = ((1 - a_i) * g_b) + (a_i * g_i)
    b_o = ((1 - a_i) * b_b) + (a_i * b_i)
    return np.array([r_o,g_o,b_o]).T

def mpl2flu(cmap_len=15, cmap_names='all', name_with_num=False, warn=True):
    '''Generate Fluent importable Colormaps from Matplotlib

    Parameters
    ----------
    cmap_len :  Int
        Optional: Number of colors in the map to generate.
        Default: 15.
    cmap_names : Sequence or String
        Optional: Name of the cmap to create.
        Default: 'all'
    name_with_num : Bool
        Optional: Adds the map length to the end of the filename. 
        Default: False
    warn : Bool
        Optional: Prints a warning about colormap size if the size > 32.
        Default: True
    '''
    
    if cmap_names == 'all':
        cmap_names = colormaps()
    else:
        if isinstance(cmap_names,str):
            cmap_names = [cmap_names]
        
    cmap_len = round(cmap_len)
    
    if (cmap_len >= 32) & (warn):
        print(map_size_warning)
    
    # Make sure the subfolder exists:
    if not os.path.exists('colormaps'):
        os.mkdir('colormaps')
        print('Creating directory for colormaps:')
        print(os.path.realpath('colormaps'))
    
    for cmap_name in cmap_names:
        cmap = cm.get_cmap(cmap_name.lower(),cmap_len)
        
        # Add the length of the cmap to the filename
        if name_with_num:
            cmap_name = cmap_name+str(cmap_len)
        filename = 'colormaps/'+cmap_name+'.colormap'
        
        # Convert from RGBA to RGB
        rgb = rgba_to_rgb(cmap(np.arange(0,cmap_len)))
        
        # Write to file
        write_cmap(rgb,filename,cmap_name)

def read_data(filename,delimiter=None,dtype=None):
    '''Read data in from text file, url, or input string
    '''
    # Read filename or url
    try:
        return np.genfromtxt(filename)
    # Try to read input as a string
    except (FileNotFoundError, OSError):
        from io import StringIO
        import re
        
        string = filename.replace('#','')
        
        # Try to determine the delimiter
        if not delimiter:
            delimiters = (' ',',','\t')
            delimiter = delimiters[
                np.argmax(
                    [len(filename.split(delim)) for delim in delimiters]
                )
            ]
        # Try to determine dtype
        check_string = string.split('\n')[0].split(delimiter)[0].lower()
        if (re.search('[a-f]',check_string) is not None) & (len(check_string)==6):
            # Convert hex values
            string = string.split(delimiter)
            rgb,_,_ = normalize(
                x = np.array([[np.array(int(s[n:n+2],16)) for n,hex in zip(range(0,6,2),s)] for s in string]),
                min_value = 0,
                max_value = 255,
            )
            return rgb
        else:
            try:
                ary = np.genfromtxt(
                    StringIO(string),
                    delimiter=delimiter,
                    dtype=dtype,
                )
                return ary
            except Exception as e:
                print('Could not parse string. Recieved Error:\n',e)
                print('\nTry including a delimiter or dtype')

def write_cmap(rgb,filename,cmap_name=None):
    '''Colormap writing function
    
    Parameters
    ----------
    rgb : Sequence, Nx3 or 3xN
        Required: Iterable input of [R,G,B] values to write to colormap file
    filename : String
        Required: Output file name, preferably with *.colormap extension.
    cmap_name : String
        Optional: Name of colormap which fluent will use. If no name is
        provided, a name will be generated from the filename.
        Default: None
    '''
    if not cmap_name:
        root, fname = os.path.split(filename)
        cmap_name, ext = os.path.splitext(fname)
    
    if not isinstance(rgb,np.ndarray):
        rgb = np.array(rgb)
    
    # Make sure rgb is normalized
    rgb,_,_ = normalize(rgb)
    
    # Add Column of Floats from 0 to 1
    nrgb = np.c_[
        np.linspace(0,1,len(rgb)),
        rgb,
    ]
 
    with open(filename,'wt') as file:
        # Write Name of Color Map
        file.write('("'+cmap_name+'"\n')
        # Format nrgb as (1.6f 1.6f 1.6f 1.6f)
        formatted_data = np.apply_along_axis(
            func1d = lambda x: ('\t('+3*'{:.6f} '+'{:.6f})\n').format(*x),
            axis = 1,
            arr = nrgb)
        formatted_data = ''.join(formatted_data)
        file.write(formatted_data)
        # Close Parenthesis
        file.write(')')

map_size_warning = '''   
 WARNING:
 TLDR: Use cmap_len = N for a number of colors you actually want. Supress 
 this warning with warn = False if you really want more than 32 colors.
 
 It appears Fluent interpolates color by placing 2 values at the 
 right (high end) that are similar, then adds from the left 
 (as viewing in the EDIT menu in Fluent). This doesn't work well for 
 diverging maps with a central color like RdYlBu (or any really).
 
 Better to create the map of the size you actually want using cmap_len.
 I'm sure there's a way to fix this, but I haven't figured it out.

 Eg:
 A pseudo map from Red to white:
  ____________________________________________
 |-R4-|-R3-|-R2-|-R1-|-N0-|-W1-|-W2-|-W3-|-W4-|
  `````````````````````````````````````````````
 Interpolating this down you'd expect something like:
  ________________________
 |-R4-|-R2-|-N0-|-W2-|-W4-|
  `````````````````````````
 But instead Fluent creates something like:
  ________________________
 |-R4-|-R3-|-W2-|-W3-|-W4-|
  `````````````````````````
'''