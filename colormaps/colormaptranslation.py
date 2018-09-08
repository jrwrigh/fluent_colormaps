import csv
from pathlib import Path
import os
    # get path of the script
scriptpath = Path(os.path.dirname(os.path.abspath(__file__)))

## Inputs:
    # Path to the CSV file
csv_path = scriptpath / './original_csvs/extended-kindlmann-table-float-0128.csv'
    # Name and location for the colormap to be created
colormapfilename = scriptpath / 'kindlmann_extended.colormap'
    # Name that Fluent uses to reference the colormap
fluentcolormapname = 'kindlmann-extended'
    # Does CSV have header?
csv_has_header = True

## Translation:

header = f'("{fluentcolormapname}"\n'

with csv_path.open() as csvfile:
    csvreader = csv.reader(csvfile)
    # if csv_has_header: fiel
    with open(colormapfilename, 'w+') as file:
        file.write(header)
        for line in csvreader:
            if csv_has_header:
                try:
                    # if first entry fails to convert to float, skip the line
                    float(line[0])
                except:
                    pass
                else:
                    n = [float(x) for x in line]
                    line_to_write = f'({n[0]} {n[1]} {n[2]} {n[3]})'
                    file.write(line_to_write + '\n')
            else:
                n = [float(x) for x in line]
                line_to_write = f'({n[0]} {n[1]} {n[2]} {n[3]})'
                file.write(line_to_write + '\n')
