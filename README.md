# fluent_colormaps
#### Working in ANSYS CFD Post or CFX? Check out [cfdpost_colormaps](https://github.com/u2berggeist/cfdpost_colormaps)!
[![Say Thanks!](https://img.shields.io/badge/Say-Thanks&#33;-orange.svg?longCache=true&style=flat-square)](https://saythanks.io/to/u2berggeist)

Here are tools that allow users to use different color maps in ANSYS Fluent without having to enter then in manually or have them buried in a settings file. It includes a scheme file that allows simple import/export of colormaps as well as some selected colormaps.

The scheme script for importing the color maps to Fluent is taken from [this](http://www.cadfamily.com/download-pdf/FLUENT12/AutoUGM03_fluent_tips.pdf) pdf presentation. It is also included in this repository for archiving purposes.

The example colormaps (other than `thermacam.colormap` which came from the presentation linked above) are taken from [Kenneth Moreland's webpage](https://www.kennethmoreland.com/color-advice/) on color map advice*.

I've also written up a simple Python script that will translate CSV's into the correct format for this process. It is commented with instructions.

\*Note that the "Extended Black Body" colormap used to be posted on Kenneth's website. It is no longer there and is replaced by the "Inferno" colormap. The "Extended Black Body" and "Inferno" are not quite the same, with "Inferno" being more muted in it's color pallette which I personally don't like. I'm currently (2018-11-07) contacting Kenneth to get his comment on the matter.

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

