import csv
import os
import sys

input_dir = sys.argv[1]
output_file = sys.argv[2]

fnames = os.listdir(input_dir)
fnames = [input_dir + '/' + fname for fname in fnames]

with open(output_file, 'w', newline='') as out:
    writer = csv.writer(out, delimiter=',')
    with open(fnames[0], 'r') as i:
        reader = csv.reader(i)
        writer.writerow(next(reader))

    for i in fnames:
        with open(i, 'r') as r:
            reader = csv.reader(r)
            next(reader)
            for row in reader:
                writer.writerow(row)

