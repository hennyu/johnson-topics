#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: my_tmw.py
# Author: #cf
# Version 0.2.0 (2015-08-27)


import postprocess
from os.path import join

### Set the general working directory.
wdir = "/home/ulrike/Git/johnson-topics/"

### the different runs of topic models
textmodes = ["no-lemmas", "no-lemmas-NE", "NNE", "N", "NNEVAdj", "NVAdj"]
numtopics = [20,40,60,80,100]

for mode in textmodes:
	for nt in numtopics:
		### Set parameters as used in the topic model
		NumTopics = nt
		NumIterations = 5000
		OptimizeIntervals = 100
		param_settings = str(NumTopics) + "tp-" + str(NumIterations) + "it-" + str(OptimizeIntervals) + "in"

		### create_mastermatrix
		### Creates the mastermatrix with all information in one place.
		if mode in ["no-lemmas", "no-lemmas-NE"]:
			corpuspath = join(wdir, "data/letters-leipzig-txt", "*.txt")
		else:
			corpuspath = join(wdir, "data/letters-leipzig-lemmata-" + mode, "*.txt")
		
		if mode == "no-lemmas":
			outfolder = join(wdir, "tm-results/aggregates", param_settings)
			MalletFolder = join(wdir, "tm-results/mallet")
		elif mode == "no-lemmas-NE":
			outfolder = join(wdir, "tm-results/aggregates-NE", param_settings)
			MalletFolder = join(wdir, "tm-results/mallet-NE")
		else:
			outfolder = join(wdir, "tm-results/aggregates-" + mode, param_settings)
			MalletFolder = join(wdir, "tm-results/mallet-" + mode)
		
		mastermatrixfile = "mastermatrix.csv"
		metadatafile = join(wdir, "data/letters-leipzig-metadata_reduced.csv")

		topics_in_texts = join(MalletFolder, "topics-in-texts_" + param_settings + ".csv")
		number_of_topics = NumTopics
		useBins = False
		binDataFile = join(wdir, "3_bins", "segs-and-bins.csv")
		version  = "208+" # which MALLET version is in use?
		#postprocess.create_mastermatrix(corpuspath, outfolder, mastermatrixfile, metadatafile, topics_in_texts, number_of_topics, useBins, binDataFile, version)

		### calculate_averageTopicScores
		### Based on the mastermatrix, calculates various average topic score datasets.
		mastermatrixfile = join(outfolder, "mastermatrix.csv")
		# targets: one or several, depending on available metadata
		targets = ["idno","sender_norm","receiver_norm","year"]
		#postprocess.calculate_averageTopicScores(mastermatrixfile, targets, outfolder)


		''' this was not used 
		### build_gephitable
		target = "subgenre"
		aggregationfile = join(wdir, "data", "7_aggregates", param_settings, "avgtopicscores_by-" + target + ".csv")
		gephifile = join(wdir, "model", "aggregates", param_settings, "gephi-input-" + "target" + ".csv")
		#postprocess.build_gephitable(aggregationfile, gephifile, target)
		'''

		### save_firstWords
		### Saves the first words of each topic to a separate file.
		topicWordFile = join(MalletFolder, "topics-with-words_" + param_settings + ".csv")
		filename = "firstWords.csv"
		#postprocess.save_firstWords(topicWordFile, outfolder, filename)

		### Save topic ranks
		topicWordFile = join(MalletFolder, "topics-with-words_" + param_settings + ".csv")
		filename = "topicRanks.csv"
		#postprocess.save_topicRanks(topicWordFile, outfolder, filename)

		''' this was not used 
		### Average topic scores for two criteria (binID + subgenre)
		mastermatrixfile = join(wdir, "8_aggregates", param_settings, "mastermatrix.csv")
		targets = ["binID", "subgenre"]
		outfolder = join(wdir, "8_aggregates", param_settings)
		#postprocess.calculate_complexAverageTopicScores(mastermatrixfile, targets, outfolder)
		'''
