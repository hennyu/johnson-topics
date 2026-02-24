#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import glob
from os.path import join
from os.path import basename
from os import rename


'''
# move all xml files to data directory
for file in glob.glob(join(wdir, "TEI/**/*.xml")):
	print(file)
	rename(file, join(wdir,"data/letters-leipzig", basename(file)))

print("done")
'''


# change the filenames of the plain text files to idno values

wdir = "/home/ulrike/Git/johnson-topics"
data_dir = "data/letters-leipzig-txt"

'''
md = pd.read_csv(join(wdir, "data/letters-leipzig-metadata.csv"), sep=",", index_col=0, header=0)

for file in glob.glob(join(wdir, "data/letters-leipzig-txt/*.txt")):
	filename = basename(file)[0:-4]
	idno = md.loc[md["filename"] == filename + ".xml"].index[0]
	rename(join(wdir, data_dir, filename  + ".txt"), join(wdir, data_dir, idno + ".txt"))
'''	

# move files of reduced corpus to new folder

md = pd.read_csv(join(wdir, "data/letters-leipzig-metadata_reduced.csv"), sep=",", index_col=0, header=0)

for file in glob.glob(join(wdir, data_dir, "*.txt")):
	file_name = basename(file)
	file_id = file_name[:6]
	if file_id in md.index.values:
		print(file_id)
		rename(file, join(wdir, "out", file_name))

	
print("done")
