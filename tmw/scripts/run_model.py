#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: run_model.py
# Author: #cf
# Version 0.1.0 (2016-10-17)

"""
Parameter file for model.py. 
"""

import model
from os.path import join


### Set the general working directory.
wdir = "/home/ulrike/Git/johnson-topics/"


### Shared parameters
MalletPath = "/home/ulrike/Programs/mallet-2.0.8/bin/mallet"

textmodes = ["no-lemmas", "no-lemmas-NE", "NNE", "N", "NNEVAdj", "NVAdj"]

for mode in textmodes:
	if mode in ["no-lemmas", "no-lemmas-NE"]:
		TextFolder = join(wdir, "data/letters-leipzig-txt")
	else:
		TextFolder = join(wdir, "data/letters-leipzig-lemmata-" + mode)
	if mode == "no-lemmas":
		MalletFolder = join(wdir, "tm-results/mallet")
	elif mode == "no-lemmas-NE":
		MalletFolder = join(wdir, "tm-results/mallet-NE")
	else:
		MalletFolder = join(wdir, "tm-results/mallet-" + mode)

	CorpusFile = join(MalletFolder, "ub.mallet")


	### Import parameters (call_mallet_import)
	if mode == "no-lemmas":
		StoplistProject = join(wdir, "data/stopwords_names.txt")
	else:
		StoplistProject = join(wdir, "data/stopwords.txt")
	
	model.call_mallet_import(MalletPath, TextFolder, MalletFolder, CorpusFile, StoplistProject)


	### Modeling parameters (call_mallet_model)
	NumTopics = [20,40,60,80,100]
	NumIterations = [5000]
	OptimizeIntervals = [100]
	NumRepetitions = 1
	NumTopWords = 50
	NumThreads = 4

	model.call_mallet_modeling(MalletPath, CorpusFile, MalletFolder, NumTopics, NumIterations, OptimizeIntervals, NumRepetitions, NumTopWords, NumThreads)
