# fluent_colormaps
#### Working in ANSYS CFD Post or CFX? Check out [cfdpost_colormaps](https://github.com/u2berggeist/cfdpost_colormaps)!
[![Say Thanks!](https://img.shields.io/badge/Say-Thanks&#33;-orange.svg?longCache=true&style=flat-square)](https://saythanks.io/to/u2berggeist)

## Why Colormaps?

Because rainbow is bad. 

To start, what are colormaps for? They're a visualization tool. They attempt to communicate a change in numerical value from a sample set by changing color. The "greater" the change in color, the greater the change in numerical value. 

The rainbow is a linear scale of light wavelengths. *However*, how humans percieve a rainbow scale is **not** linear. In fact, the correlation between the percieved color change in a rainbow colormap and the actual numerical change is quite poor. 

There are several instances where professionals have made incorrect conclusions from rainbow-based visualizations. Doctors have been found to make better diagnoses by using alternate colormaps:

> In tests, diagnostic accuracy, as measured by the proportion of diseased areas identified, increased dramatically with the new color scheme. [Source](https://phys.org/news/2011-10-heart-disease-visualization-experts-simpler.html)

and climate scientists have misinterpreted their own data by using rainbow colormaps:

>  The same sub-tropical ‘front’ is apparent in rainbow, but far less clear in the sequential scheme.... [the sub-tropical 'front'] is a mirage, an artefact of the choice of colour scale. [Source](http://www.climate-lab-book.ac.uk/2016/why-rainbow-colour-scales-can-be-misleading/)

See [this article](https://matplotlib.org/users/colormaps.html) from matplotlib that details more about the issues in colormaps. In particular, compare the plots of perceptualy uniform colormaps and the more common colormaps from the same page (the lower plot in particular). These are ploted based on percieved brightness, so linear is the goal. As you can see, rainbow and the like are quite poor.

![perceptualy uniform colormaps](https://matplotlib.org/users/plotting/colormaps/lightness_00.png)

![more common colormaps](https://matplotlib.org/users/plotting/colormaps/lightness_05.png)

Bottom line: don't use rainbow. \#endrainbow

## Ok, so what is this repository?

Here are tools that allow users to use different color maps in ANSYS Fluent without having to enter then in manually or have them buried in a settings file. It includes a scheme file that allows simple import/export of colormaps as well as some selected colormaps.

The scheme script for importing the color maps to Fluent is taken from [this](http://www.cadfamily.com/download-pdf/FLUENT12/AutoUGM03_fluent_tips.pdf) pdf presentation. It is also included in this repository for archival purposes.

The example colormaps (other than `thermacam.colormap` which came from the presentation linked above) are taken from [Kenneth Moreland's webpage](https://www.kennethmoreland.com/color-advice/) on color map advice*.

Examples of the different colormap options are in [`Examples.md`](./Examples.md) or [this imgur album](https://imgur.com/a/hL35KCY). This is an axisymmetric CFD simulation with flow going right to left. Notice the differences in the appearance of turbulence.

I've also written up a simple Python script that will translate CSV's into the correct format for this process. It is commented with instructions.

\*Note that the "Extended Black Body" colormap used to be posted on Kenneth's website (though it is still available on [GitHub](https://github.com/kennethmoreland-com/kennethmoreland-com.github.io/tree/master/color-advice)). After discussion with Kenneth over email, it was dropped in favor of "Inferno" as they're both very similar to each other. 
"Inferno" is an interpolation over the [CIELAB colorspace](https://en.wikipedia.org/wiki/CIELAB_color_space) which is calibrated to correlate between the numerical change vs human-percieved change. "Extended Black Body" on the other hand is simply an interpolation between a few hues that is corrected for brightness (ie. not as rigorous). That said, "Extended Black Body" isn't bad, its just not as good as "Inferno", but is definitely better than rainbow!

## Use:

In Fluent TUI:
```
> (load "rw_colormap.scm")
Loading ".\.\rw_colormap.scm"
Done.
#f
```
This will add `read-colormap` and `write-colormap` functions to the `/file` menu in the TUI:

```
> file/read-colormap "kindlmann_extended.colormap"
```

After you do that, the color map will be available for use.

## Color Map Format

```
("fluent_name"
(fraction1 R1 G1 B1)
(fraction2 R2 G2 B2)
)
```
The color map file is parenthetically delimited. First item is the string that Fluent uses to reference the colormap. 
After that, each color point is enclosed in parentheses and is made of 4 items: the fraction value (ie. what the color represents in a scale from 0 → 1) and the RGB code normalized from 0 → 1.

Here's an example from `kindlmann.colormap`:

```
("kindlmann"
(0.0 0.0 0.0 0.0)
(0.00787401574803 0.0361829637519 0.00175999531726 0.0321710772612)
(0.0157480314961 0.0666376124681 0.00324511662403 0.0631800420914)
.
.
.
(0.992125984252 0.999169719339 0.988946878303 0.98599754002)
(1.0 1.0 1.0 1.0)
)
```

## Make Fluent load colormaps automatically

To do this, you simply need to edit/create the `.fluent` in your home directory (`~` for Linux, `C:\Users\[your account username]`). The `.fluent` file is loaded whenever you start Fluent. The file will look like this:

```scheme
(load "[Path to fluent_colormaps]/rw_colormap.scm")

(ti-menu-load-string "file/read-colormap [Path to fluent_colormaps]/colormaps/blackbody_extended.colormap")
(ti-menu-load-string "file/read-colormap [Path to fluent_colormaps]/colormaps/inferno.colormap")
```

The first line loads the read/write colormap commands while the last 3 load the "Extended Blackbody" and "Inferno" into Fluent. You can add in more of the colormaps simply by copy/pasting the line again.

