4#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: my_tmw.py
# Author: #cf
# Version 0.2.0 (2015-08-27)


import visualize
from os.path import join

### Set the general working directory.
wdir = "/home/ulrike/Git/johnson-topics/"

### the different runs of topic models
textmodes = ["no-lemmas", "no-lemmas-NE", "NNE", "N", "NNEVAdj", "NVAdj"]
numtopics = [60] #20,40,60,80,100

for mode in textmodes:
	for nt in numtopics:

		### Set parameters as used in the topic model
		NumTopics = nt
		NumIterations = 5000
		OptimizeIntervals = 100
		param_settings = str(NumTopics) + "tp-" + str(NumIterations) + "it-" + str(OptimizeIntervals) + "in"
		
		### Mallet folder and outfolder
		if mode == "no-lemmas":
			outfolder = join(wdir, "tm-results/visuals", param_settings)
			AggregatesFolder = join(wdir, "tm-results/aggregates", param_settings)
			MalletFolder = join(wdir, "tm-results/mallet")
		elif mode == "no-lemmas-NE":
			outfolder = join(wdir, "tm-results/visuals-NE", param_settings)
			AggregatesFolder = join(wdir, "tm-results/aggregates-NE", param_settings)
			MalletFolder = join(wdir, "tm-results/mallet-NE")
		else:
			outfolder = join(wdir, "tm-results/visuals-" + mode, param_settings)
			AggregatesFolder = join(wdir, "tm-results/aggregates-" + mode, param_settings)
			MalletFolder = join(wdir, "tm-results/mallet-" + mode) 

		### make_wordle_from_mallet
		### Creates a wordle for each topic.
		word_weights_file = join(MalletFolder, "word-weights_" + param_settings + ".csv")
		words = 40
		outfolder_wordles = join(outfolder, "wordles")
		font_path = join(wdir, "data", "AlegreyaSans-Regular.otf")
		dpi = 300
		num_topics = NumTopics
		TopicRanksFile = join(AggregatesFolder, "topicRanks.csv")
		#visualize.make_wordle_from_mallet(word_weights_file, num_topics, words, TopicRanksFile, outfolder_wordles, dpi) # ggf. font_path

		''' this was not used
		### crop_images
		### Crops the wordle image files, use if needed.
		inpath = join(wdir, "8_visuals", param_settings, "wordles", "*.png")
		outfolder = join(wdir, "8_visuals", param_settings, "wordles")
		left = 500 # image start at the left
		upper = 50 # image start at the top
		right = 3400 # image end on the right
		lower = 2350 # image end at the bottom
		#visualize.crop_images(inpath, outfolder, left, upper, right, lower)
		'''
		
		### plot_topTopics
		### For each item from a category, creates a barchart of the top topics.
		averageDatasets = join(AggregatesFolder, "avg*.csv") 
		firstWordsFile = join(AggregatesFolder, "firstWords.csv")
		numberOfTopics = NumTopics # must be actual number of topics modeled.
		targetCategories = ["idno"]
		# one or several: "author-name", "author-gender", "decade", "subgenre", "title"
		topTopicsShown = 30 
		fontscale = 1.0
		height = 0 # 0=automatic and variable
		dpi = 300
		outfolder_topTopics = join(outfolder, "topTopics")
		TTmode = "normalized" # normalized, absolute
		visualize.plot_topTopics(averageDatasets, firstWordsFile, numberOfTopics, targetCategories, TTmode, topTopicsShown, fontscale, height, dpi, outfolder_topTopics)

		''' this was not used
		### plot_topItems
		### For each topic, creates a barchart with top items from a category. 
		averageDatasets = join(wdir, "tm/aggregates_N", param_settings, "avg*.csv") 
		outfolder = join(wdir, "tm/visuals_N", param_settings, "topItems")
		firstWordsFile = join(wdir, "tm/aggregates_N", param_settings, "firstWords.csv")
		numberOfTopics = NumTopics # must be actual number of topics modeled. 
		targetCategories = ["idno"]
		# choose one or several from: author-name, decade, subgenre, gender, idno, title, segmentID
		topItemsShown = 20 
		fontscale = 0.8
		height = 0 # 0=automatic and flexible
		dpi = 300
		#visualize.plot_topItems(averageDatasets, outfolder, firstWordsFile, numberOfTopics, targetCategories, topItemsShown, fontscale, height, dpi)
		'''


		''' this was not used
		### plot_distinctiveness_heatmap
		### For each category, make a heatmap of most distinctive topics. 
		averageDatasets = join(wdir, "tm/aggregates", param_settings, "avg*.csv") 
		firstWordsFile = join(wdir, "tm/aggregates", param_settings, "firstWords.csv")
		outfolder = join(wdir, "tm/visuals", param_settings, "distinctiveness")
		targetCategories = ["month"] 
		# one or several: "author-name", "decade", "subgenre", "gender", "idno", "title"
		numberOfTopics = NumTopics # must be actual number of topics modeled.
		topTopicsShown = 20 
		mode = "zscores" # meannorm|mediannorm|zscores|absolute
		sorting = "std"
		fontscale = 1.0
		dpi = 300
		#visualize.plot_distinctiveness_heatmap(averageDatasets, firstWordsFile, outfolder, targetCategories, numberOfTopics, topTopicsShown, mode, sorting, fontscale, dpi)
		'''

		''' this was not used
		### plot_topicsOverTime
		### Creates lineplots or areaplots for topic development over time.
		#averageDatasets = wdir+"/7_aggregates/avgtopicscores_by-decade.csv" 
		#firstWordsFile = wdir+"/7_aggregates/firstWords.csv"
		#outfolder = wdir+"/8_visuals/overTime/"
		#numberOfTopics = 250 # must be actual number of topics modeled.
		#fontscale = 1.0
		#dpi = 300
		#height = 0 # for lineplot; 0=automatic
		#mode = "line" # area|line for areaplot or lineplot
		#topics = ["48","67","199"] # list of one or several topics
		#tmw.plot_topicsOverTime(averageDatasets, firstWordsFile, outfolder, numberOfTopics, fontscale, dpi, height, mode, topics)
		'''
