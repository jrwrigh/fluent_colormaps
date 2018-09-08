import csv
from pathlib import Path
import os
scriptpath = Path(os.path.dirname(os.path.abspath(__file__)))

## Inputs
csv_path = scriptpath / './original_csvs/extended-kindlmann-table-float-0128.csv'
colormapfilename = scriptpath / 'kindlmann_extended.colormap'
colormapname = 'kindlmann-extended'
csv_has_header = True

# Other stuff:

header = f'("{colormapname}"\n'

with csv_path.open() as csvfile:
    csvreader = csv.reader(csvfile)
    # if csv_has_header: fiel
    with open(colormapfilename, 'w+') as file:
        file.write(header)
        for line in csvreader:
            try:
                # if first entry fails to convert to float, skip the line
                float(line[0])
            except:
                pass
            else:
                n = [float(x) for x in line]
                line_to_write = f'({n[0]} {n[1]} {n[2]} {n[3]})'
                file.write(line_to_write + '\n')
