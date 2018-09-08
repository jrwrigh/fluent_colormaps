# fluent_colormaps
Here are tools that allow users to use different color maps in ANSYS Fluent without having to enter then in manually or have them buried in a settings file. It includes a scheme file that allows simple import/export of colormaps as well as some selected colormaps.

The scheme script for importing the color maps to Fluent is taken from [this](http://www.cadfamily.com/download-pdf/FLUENT12/AutoUGM03_fluent_tips.pdf) pdf presentation. It is also included in this repository for archiving purposes.

The example colormaps (other than `thermacam.colormap` which came from the presentation linked above) are taken from [Kenneth Moreland's webpage](https://www.kennethmoreland.com/color-advice/) on color map advice.

I've also written up a simple Python script that will translate CSV's into the correct format for this process. It is commented with instructions.

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


