# translation_tools

Collection of tools used to take raw colormap data and convert it to be compatible with the Fluent colormap read function.

## `mpl2flu`

Module to for creating colormap files from `matplotlib` colormaps and also for other sources. See module and `minimum-working-example.*` for more and instruction. Credit to Devin Prescott for creating the module

## `csv2flu_colormaptranslation.py` (HISTORICAL)

This is the original script used to translate the csv's from Kenneth Moreland's site (see `README.md`).
It's hard coded to only be compatible with those specific CSVs and is kept for that purpose only. **Recommendation to use `mpl2flu` for all other uses.**

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

